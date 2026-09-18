from django.urls import path
from . import views

app_name = 'content'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('news/', views.news_list, name='news_list'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('news/external/', views.news_external, name='news_external'),
    path('faq/', views.faq_list, name='faq_list'),
    path('vacancies/', views.vacancies_list, name='vacancies_list'),
    path('reviews/', views.reviews_list, name='reviews_list'),
    path('reviews/add/', views.add_review, name='add_review'),
    path('promocodes/', views.promocodes, name='promocodes'),
    path('privacy/', views.privacy, name='privacy'),
]