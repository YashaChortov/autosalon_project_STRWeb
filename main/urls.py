from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'main'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/order/', views.create_order, name='create_order'),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('orders/', views.order_list, name='order_list'),
    path('clients/', views.client_list, name='client_list'),
    path('faq/', views.faq_list, name='faq_list'),
    path('contacts/', views.contact_list, name='contact_list'),
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart/update/<int:product_id>/', views.cart_update, name='cart_update'),
    path('checkout/', views.checkout, name='checkout'),
]
