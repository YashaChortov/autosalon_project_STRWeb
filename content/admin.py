from django.contrib import admin
from .models import Vacancy, Review, News

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')
    search_fields = ('title',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'rating', 'approved', 'created_at')
    list_filter = ('approved', 'rating')
    search_fields = ('user__username', 'content')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)
    approve_reviews.short_description = "Одобрить выбранные отзывы"

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')
    search_fields = ('title',)