import random
import requests
from requests.exceptions import RequestException

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils.dateparse import parse_datetime

# Локальные модели приложения content
from .models import News, Vacancy, Review
from .forms import ReviewForm

# Модели из приложения main
from main.models import (
    Product, Article, Partner, Banner,
    CompanyInfo, HistoryEvent, FAQ,
    PromoCode, PrivacyPolicy,
)


# ============ ГЛАВНАЯ ============
def home(request):
    context = {
        'products': Product.objects.all()[:6],
        'latest_article': Article.objects.filter(is_published=True).first(),
        'partners': Partner.objects.all(),
        'banners': Banner.objects.all(),
    }
    return render(request, 'content/home.html', context)


# ============ О КОМПАНИИ ============
def about(request):
    company = CompanyInfo.objects.first()
    history = HistoryEvent.objects.all() if company else []
    return render(request, 'content/about.html', {
        'company': company,
        'history': history,
    })


# ============ НОВОСТИ (из БД) ============
def news_list(request):
    articles = Article.objects.filter(is_published=True)
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    return render(request, 'content/news_list.html', {
        'articles': paginator.get_page(page),
    })


def news_detail(request, pk):
    article = get_object_or_404(Article, pk=pk, is_published=True)
    return render(request, 'content/news_detail.html', {'article': article})


# ============ НОВОСТИ (внешние API, если нужно) ============
def news_external(request):
    """Загружает новости из NewsAPI + факт о кошках."""
    cat_fact = None
    news_list = []
    error = None

    try:
        cat_response = requests.get('https://catfact.ninja/fact', timeout=5)
        if cat_response.status_code == 200:
            cat_fact = cat_response.json().get('fact')
    except RequestException:
        cat_fact = 'Не удалось загрузить факт о кошках'

    try:
        response = requests.get(
            'https://newsapi.org/v2/everything',
            params={
                'q': 'cryptocurrency',
                'apiKey': '9658ea7e12b944618b3f5569269cb600',
                'pageSize': 50,
            },
            timeout=10,
        )
        if response.status_code == 200:
            articles = response.json().get('articles', [])
            if len(articles) > 5:
                news_list = random.sample(articles, 5)
            else:
                news_list = articles
        else:
            error = 'Ошибка загрузки новостей'
    except RequestException:
        error = 'Ошибка соединения с API новостей'

    return render(request, 'content/news_external.html', {
        'news_list': news_list,
        'error': error,
        'cat_fact': cat_fact,
    })


# ============ СЛОВАРЬ ТЕРМИНОВ ============
def faq_list(request):
    return render(request, 'content/faq_list.html', {
        'faqs': FAQ.objects.all(),
    })


# ============ ВАКАНСИИ ============
def vacancies_list(request):
    vacancies = Vacancy.objects.filter(is_active=True).order_by('-published_at')
    return render(request, 'content/vacancies_list.html', {'vacancies': vacancies})


# ============ ОТЗЫВЫ ============
def reviews_list(request):
    if request.user.is_authenticated:
        reviews = Review.objects.filter(
            Q(approved=True) | Q(user=request.user)
        ).order_by('-created_at')
    else:
        reviews = Review.objects.filter(approved=True).order_by('-created_at')
    return render(request, 'content/reviews_list.html', {'reviews': reviews})


@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.approved = True
            review.save()
            messages.success(request, "Спасибо за отзыв!")
            return redirect('content:reviews_list')
    else:
        form = ReviewForm()
    return render(request, 'content/add_review.html', {'form': form})


# ============ ПРОМОКОДЫ ============
def promocodes(request):
    return render(request, 'content/promocodes.html', {
        'active_promos': PromoCode.objects.filter(is_active=True),
        'archived_promos': PromoCode.objects.filter(is_active=False),
    })


# ============ ПОЛИТИКА КОНФИДЕНЦИАЛЬНОСТИ ============
def privacy(request):
    policy = PrivacyPolicy.objects.first()
    return render(request, 'content/privacy.html', {'policy': policy})