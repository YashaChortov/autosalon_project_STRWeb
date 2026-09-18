from django.shortcuts import render
from .models import Product, Order, Client, Contact, FAQ
from users.decorators import employee_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages


def product_list(request):
    products = Product.objects.all()
    return render(request, 'main/product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'main/product_detail.html', {'product': product})

@login_required
def create_order(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    # Только клиент может покупать
    if not request.user.is_client:
        messages.error(request, "Только клиенты могут оформлять заказы.")
        return redirect('main:product_detail', pk=product_id)

    # Получаем профиль клиента
    try:
        client = request.user.client_profile
    except Client.DoesNotExist:
        messages.error(request, "Профиль клиента не найден.")
        return redirect('main:product_detail', pk=product_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        Order.objects.create(
            client=client,
            product=product,
            quantity=quantity,
        )
        messages.success(request, f"Заказ на «{product.name}» оформлен!")
        return redirect('main:my_orders')

    return render(request, 'main/create_order.html', {'product': product})


@login_required
def my_orders(request):
    try:
        client = request.user.client_profile
    except Client.DoesNotExist:
        return render(request, 'main/my_orders.html', {'orders': []})

    orders = Order.objects.filter(client=client).order_by('-order_date')
    return render(request, 'main/my_orders.html', {'orders': orders})

@employee_required
def order_list(request):
    orders = Order.objects.select_related('client', 'product').all()
    return render(request, 'main/order_list.html', {'orders': orders})

@employee_required
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'main/client_list.html', {'clients': clients})

def contact_list(request):
    contacts = Contact.objects.select_related('employee').all()
    return render(request, 'main/contact_list.html', {'contacts': contacts})

def faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, 'main/faq_list.html', {'faqs': faqs})

# для корзины
def cart_add(request, product_id):
    if not request.user.is_client:
        messages.error(request, "Только клиенты могут добавлять в корзину.")
        return redirect('main:product_detail', pk=product_id)
    cart = request.session.get('cart', {})
    qty = int(request.POST.get('quantity', 1))
    cart[str(product_id)] = cart.get(str(product_id), 0) + qty
    request.session['cart'] = cart
    messages.success(request, "Товар добавлен в корзину.")
    return redirect('main:cart')

def cart_view(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0
    for pid, qty in cart.items():
        p = Product.objects.filter(pk=pid).first()
        if p:
            subtotal = p.price * qty
            total += subtotal
            items.append({'product': p, 'qty': qty, 'subtotal': subtotal})
    return render(request, 'main/cart.html', {'items': items, 'total': total})

def cart_remove(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('main:cart')

def cart_update(request, product_id):
    action = request.POST.get('action')
    cart = request.session.get('cart', {})
    pid = str(product_id)
    if pid in cart:
        if action == 'inc':
            cart[pid] += 1
        elif action == 'dec' and cart[pid] > 1:
            cart[pid] -= 1
    request.session['cart'] = cart
    return redirect('main:cart')

"""
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.warning(request, "Корзина пуста.")
        return redirect('main:cart')
    # Здесь логика оформления — можно создать Order
    request.session['cart'] = {}
    messages.success(request, "Заказ оформлен!")
    return redirect('main:product_list')
"""

@login_required
def checkout(request):
    cart = request.session.get('cart', {})

    if not cart:
        messages.warning(request, "Корзина пуста.")
        return redirect('main:cart')

    # Собираем товары для отображения
    items = []
    total = 0
    for pid, qty in cart.items():
        product = Product.objects.filter(pk=pid).first()
        if product:
            subtotal = product.price * qty
            total += subtotal
            items.append({'product': product, 'qty': qty, 'subtotal': subtotal})

    if request.method == 'POST':
        # Здесь по-хорошему — интеграция с платёжной системой.
        # Для лабы: создаём Order и очищаем корзину.
        try:
            client = request.user.client_profile
        except Client.DoesNotExist:
            messages.error(request, "Профиль клиента не найден.")
            return redirect('main:cart')

        for item in items:
            Order.objects.create(
                client=client,
                product=item['product'],
                quantity=item['qty'],
                status='processing',
            )

        request.session['cart'] = {}
        messages.success(request, f"Заказ на сумму {total} BYN оплачен!")
        return redirect('main:my_orders')

    return render(request, 'main/checkout.html', {
        'items': items,
        'total': total,
    })