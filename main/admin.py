from django.contrib import admin
from .models import (
    Manufacturer, ProductType, Product, Client, Employee,
    Order, FAQ, Contact
)
from .models import (
    CompanyInfo, HistoryEvent, Partner,
    Banner, Article, PromoCode, PrivacyPolicy,
)


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(HistoryEvent)
class HistoryEventAdmin(admin.ModelAdmin):
    list_display = ('year', 'event', 'company')
    list_filter = ('company', 'year')
    search_fields = ('event',)


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'site_url')
    search_fields = ('name',)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'is_published')
    list_filter = ('is_published', 'published_at')
    search_fields = ('title', 'summary', 'content')
    date_hierarchy = 'published_at'


@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_percent', 'valid_until', 'is_active')
    list_filter = ('is_active', 'valid_until')
    search_fields = ('code',)


@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'manufacturer', 'product_type')
    list_filter = ('manufacturer', 'product_type')
    search_fields = ('name',)

class OrderInline(admin.TabularInline):
    model = Order
    extra = 1

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'city')
    search_fields = ('full_name', 'email', 'phone')
    inlines = [OrderInline]

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'phone', 'email')
    search_fields = ('full_name', 'position')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'product', 'quantity', 'order_date', 'delivery_date')
    list_filter = ('order_date', 'delivery_date')
    search_fields = ('client__full_name', 'product__name')

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'added_at')
    search_fields = ('question', 'answer')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('employee', 'description')
    search_fields = ('employee__full_name',)

"""
from .models import Manufacturer, ProductType, Product, Client, Employee, Order, FAQ, Contact

from django.contrib import admin

admin.site.register(FAQ)



@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'manufacturer', 'product_type', 'created_at')
    list_filter = ('manufacturer', 'product_type')
    search_fields = ['name']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'city', 'birth_date')
    search_fields = ['full_name', 'email', 'city']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'phone', 'email', 'birth_date')
    search_fields = ['full_name', 'position']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'product', 'quantity', 'order_date', 'delivery_date')
    list_filter = ('order_date', 'delivery_date')
    search_fields = ['client__full_name', 'product__name']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo', 'job_description', 'email', 'phone')
    search_fields = ['name']

"""