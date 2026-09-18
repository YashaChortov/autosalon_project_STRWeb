from django.db import models
from autosalon_project import settings

class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    SOURCE_CHOICES = [
        ('search', 'Поисковик'),
        ('social', 'Соцсети'),
        ('friend', 'Друзья'),
        ('ad', 'Реклама'),
        ('dealer', 'Дилер'),
        ('other', 'Другое'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Пользователь"
    )
    content = models.TextField(blank=True, verbose_name="Текст отзыва")
    rating = models.PositiveSmallIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)],
        verbose_name="Оценка",
        default=5,
    )

    source = models.CharField(
        max_length=20,
        choices=SOURCE_CHOICES,
        default='other',
        verbose_name="Как вы о нас узнали",
    )
    recommend = models.CharField(
        max_length=100,
        default='Возможно',
        blank=True,
        verbose_name="Порекомендуете друзьям",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)  # <-- сразу одобряем

    def __str__(self):
        return f"Отзыв от {self.user} ({self.rating}/5)"

    @property
    def display_name(self):
        if self.user:
            return self.user.get_full_name() or self.user.username
        return "Аноним"

"""
class Review(models.Model):
    client_name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Отзыв от {self.client_name}"
"""

class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    url = models.URLField(default="https://example.com")
    published_at = models.DateTimeField(null=True, blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.title