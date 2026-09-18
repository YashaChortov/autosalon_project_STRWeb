from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    is_client = models.BooleanField(default=False, verbose_name="Клиент")
    is_employee = models.BooleanField(default=False, verbose_name="Сотрудник")

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text=None,
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text=None,
        verbose_name='user permissions',
    )
