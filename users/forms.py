from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.core.validators import RegexValidator
from main.models import Client

class CustomUserCreationForm(UserCreationForm):
    # Поля из Client (кроме full_name — его соберём из имени и фамилии)
    phone = forms.CharField(
        max_length=20,
        label="Телефон",
        widget=forms.TextInput(attrs={
            'id': 'id_phone',
            'placeholder': '+375 (XX) XXX-XX-XX',
            'inputmode': 'numeric',
        })
    )
    city = forms.CharField(max_length=100, label="Город")
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Дата рождения"
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_birth_date(self):
        from datetime import date
        bd = self.cleaned_data['birth_date']
        today = date.today()
        age = today.year - bd.year - ((today.month, today.day) < (bd.month, bd.day))
        if age < 18:
            raise forms.ValidationError("Регистрация только для лиц 18+")
        return bd

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        import re
        if not re.match(r'^\+375\s\(\d{2}\)\s\d{3}-\d{2}-\d{2}$', phone):
            raise forms.ValidationError("Телефон должен быть в формате +375 (XX) XXX-XX-XX")
        return phone

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_client = True
        user.is_employee = False
        if commit:
            user.save()
            full_name = f"{user.last_name} {user.first_name}".strip() or user.username
            Client.objects.create(
                user=user,
                full_name=full_name,
                email=user.email or f"{user.username}@noemail.local",
                phone=self.cleaned_data['phone'],
                city=self.cleaned_data['city'],
                birth_date=self.cleaned_data['birth_date'],
            )
        return user

"""
class CustomUserCreationForm(UserCreationForm):
    # Поля из Client
    full_name = forms.CharField(max_length=200, label="ФИО")
    phone = forms.CharField(max_length=20, label="Телефон (+375 (XX) XXX-XX-XX)")
    city = forms.CharField(max_length=100, label="Город")
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Дата рождения"
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_birth_date(self):
        from datetime import date
        bd = self.cleaned_data['birth_date']
        today = date.today()
        age = today.year - bd.year - ((today.month, today.day) < (bd.month, bd.day))
        if age < 18:
            raise forms.ValidationError("Регистрация только для лиц 18+")
        return bd

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_client = True
        user.is_employee = False
        if commit:
            user.save()
            Client.objects.create(
                user=user,
                full_name=self.cleaned_data['full_name'],
                email=user.email or f"{user.username}@noemail.local",
                phone=self.cleaned_data['phone'],
                city=self.cleaned_data['city'],
                birth_date=self.cleaned_data['birth_date'],
            )
        return user
"""

"""
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # Только то, что должен заполнять сам пользователь
        fields = ('username', 'email', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        # Все, кто регистрируется через сайт — клиенты
        user.is_client = True
        user.is_employee = False
        if commit:
            user.save()
        return user
"""

"""
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'is_client', 'is_employee')
"""