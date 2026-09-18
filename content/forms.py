from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'content', 'source', 'recommend']
        widgets = {
            'rating': forms.RadioSelect(
                choices=Review._meta.get_field('rating').choices
            ),
            'content': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Ваш отзыв (необязательно)',
            }),
            'source': forms.Select,
            'recommend': forms.TextInput(attrs={
                'list': 'recommend_options',
                'placeholder': 'Начните вводить...',
            }),
        }
        labels = {
            'rating': 'Ваша оценка',
            'content': 'Текст отзыва',
            'source': 'Как вы о нас узнали?',
            'recommend': 'Порекомендуете друзьям?',
        }