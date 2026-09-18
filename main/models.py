from django.db import models
from django.core.validators import RegexValidator, MinValueValidator
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

from autosalon_project import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class ProductType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    description = models.TextField(blank=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='products')
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Client(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='client_profile'
    )
    #user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(regex=r'^\+375\s\(\d{2}\)\s\d{3}-\d{2}-\d{2}$', message="Телефон должен быть в формате +375 (XX) XXX-XX-XX")
    phone = models.CharField(validators=[phone_regex], max_length=20)
    city = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.full_name

class Employee(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='employee_profile'
    )
    full_name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    phone_regex = RegexValidator(
        regex=r'^\+375\s\(\d{2}\)\s\d{3}-\d{2}-\d{2}$',
        message="Телефон должен быть в формате +375 (XX) XXX-XX-XX"
    )
    phone = models.CharField(validators=[phone_regex], max_length=20)
    email = models.EmailField()
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.full_name} — {self.position}"

"""
class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.full_name} ({self.position})"
"""

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('new', 'Новый'),
            ('processing', 'В обработке'),
            ('delivered', 'Доставлен'),
            ('cancelled', 'Отменён'),
        ],
        default='new',
    )

    def __str__(self):
        return f"Заказ #{self.pk} — {self.product.name}"

"""
class FAQ(models.Model):
    question = models.CharField("Вопрос", max_length=200)
    answer = models.TextField("Ответ")
    created_at = models.DateTimeField("Дата добавления", auto_now_add=True)

    def __str__(self):
        return self.question
"""

class Contact(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='contact',
        verbose_name="Сотрудник",
        null = True,
        blank = True,
    )
    photo = models.ImageField(upload_to='contacts/', blank=True, null=True, verbose_name="Фото")
    description = models.TextField(blank=True, verbose_name="Описание работ")

    def __str__(self):
        return f"Контакт: {self.employee.full_name}"

"""
class Contact(models.Model):
    name = models.CharField("Имя", max_length=100)
    photo = models.ImageField("Фото", upload_to='contacts/')
    job_description = models.TextField("Описание работы")
    email = models.EmailField("Почта")
    phone = models.CharField("Телефон", max_length=20)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.name
"""

class CompanyInfo(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    logo = models.ImageField(upload_to='company/', blank=True)
    video_url = models.URLField(blank=True, verbose_name="Ссылка на видео")
    requisites = models.TextField(blank=True, verbose_name="Реквизиты")
    certificate_text = models.TextField(blank=True, verbose_name="Сертификат")
    def __str__(self):
        return self.name


class HistoryEvent(models.Model):
    company = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE, related_name='history')
    year = models.IntegerField(verbose_name="Год")
    event = models.TextField(verbose_name="Событие")
    class Meta:
        ordering = ['year']
    def __str__(self):
        return f"{self.year}: {self.event[:50]}"


class Partner(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='partners/', blank=True)
    site_url = models.URLField(verbose_name="Сайт")
    def __str__(self):
        return self.name


class Banner(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='banners/')
    link = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ['order']
    def __str__(self):
        return self.title


class Article(models.Model):  # Новости
    title = models.CharField(max_length=250)
    summary = models.CharField(max_length=300, verbose_name="Краткое содержание")
    content = models.TextField(verbose_name="Полный текст")
    image = models.ImageField(upload_to='articles/', blank=True)
    published_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    class Meta:
        ordering = ['-published_at']
    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Вопрос (словарь терминов)"
        verbose_name_plural = "Словарь терминов"
    def __str__(self):
        return self.question


class PromoCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percent = models.PositiveIntegerField(verbose_name="Скидка, %")
    description = models.TextField(blank=True)
    valid_until = models.DateField(verbose_name="Действует до")
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.code


class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=200, default="Политика конфиденциальности")
    text = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title