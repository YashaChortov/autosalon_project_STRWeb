from django.shortcuts import render
from main.models import Order, Product, Client
from django.db.models import Count, Sum
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.db.models import Count
from django.shortcuts import render
from main.models import Product
from users.decorators import employee_required

@employee_required
def sales_report(request):
    data = Product.objects.values('product_type__name').annotate(count=Count('id'))
    labels = [item['product_type__name'] for item in data]
    counts = [item['count'] for item in data]

    fig, ax = plt.subplots()
    ax.bar(labels, counts)
    ax.set_title('Распределение товаров по типам')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    chart = base64.b64encode(image_png).decode('utf-8')

    orders = Order.objects.all()
    total_sales = orders.aggregate(total=Sum('product__price'))

    return render(request, 'analytics/sales_report.html', {
        'total_sales': total_sales,
        'chart': chart
    })

@employee_required
def sales_report1(request):
    orders = Order.objects.all()
    total_sales = orders.aggregate(total=Sum('product__price'))
    return render(request, 'analytics/sales_report.html', {'total_sales': total_sales})

@employee_required
def product_popularity(request):
    products = Product.objects.annotate(order_count=Count('order')).order_by('-order_count')
    return render(request, 'analytics/product_popularity.html', {'products': products})

@employee_required
def client_statistics(request):
    clients = Client.objects.annotate(order_count=Count('orders')).order_by('-order_count')
    return render(request, 'analytics/client_statistics.html', {'clients': clients})

