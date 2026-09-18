# Лабораторная работа №1 — HTML

Веб-сайт «АвтоПрестиж» — автосалон на Django.

## Страницы

### Главная (`content/templates/content/home.html`, view: `content/views.py:home`)
- [x] Логотип компании
- [x] Реклама компании в виде баннера (несколько картинок)
- [x] Каталог товаров/услуг
- [x] Наименование и краткая информация о последней опубликованной статье
- [x] Список компаний-партнёров с логотипами и ссылками на их сайты
- [x] Таблица партнёров в базе данных (`main/models.py:Partner`)

### Страница товара (`main/templates/main/product_detail.html`, view: `main/views.py:product_detail`)
- [x] Открывается при клике на товар из каталога
- [x] Информация об объекте (микроразметка `itemscope itemtype="http://schema.org/Product"`)
- [x] Значок «Добавить в корзину»

### Корзина (`main/templates/main/cart.html`, view: `main/views.py:cart_view`)
- [x] Список добавленных объектов
- [x] Значок «Оплатить»
- [x] Значок «Удалить из корзины»
- [x] Значок «Увеличить количество»
- [x] Значок «Уменьшить количество»

### Страница оплаты (`main/templates/main/checkout.html`, view: `main/views.py:checkout`)
- [x] Форма оплаты с выбором способа (`input type="radio"`)
- [x] Контактные данные с валидацией (`pattern` для телефона)
- [x] Сохранение заказа в БД (`Order.objects.create`)

### О компании (`content/templates/content/about.html`, view: `content/views.py:about`)
- [x] Информация о компании (`main/models.py:CompanyInfo`)
- [x] Видео о компании (`<video>` + `<source>`)
- [x] Логотип
- [x] История компании по годам (`main/models.py:HistoryEvent`)
- [x] Реквизиты
- [x] Сертификат (текст)

### Новости (`content/templates/content/news_list.html`, view: `content/views.py:news_list`)
- [x] Список статей из базы данных (`main/models.py:Article`)
- [x] Заголовок
- [x] Краткое содержание (одно предложение)
- [x] Картинка
- [x] Кнопка «Читать далее» (`content/templates/content/news_detail.html`)

### Словарь терминов (`content/templates/content/faq_list.html`, view: `content/views.py:faq_list`)
- [x] Список вопросов из базы данных (`main/models.py:FAQ`)
- [x] Дата добавления на сайт (`<time datetime="...">`)
- [x] Разворачивающийся ответ (`<details>` / `<summary>`)

### Контакты (`main/templates/main/contact_list.html`, view: `main/views.py:contact_list`)
- [x] Фото сотрудников (`main/models.py:Contact`, `main/models.py:Employee`)
- [x] Описание выполняемых работ
- [x] Телефоны (ссылка `tel:`)
- [x] Почта (ссылка `mailto:`)
- [x] Должность

### Политика конфиденциальности (`content/templates/content/privacy.html`, view: `content/views.py:privacy`)
- [x] Текст политики в соответствии с тематикой сайта (`main/models.py:PrivacyPolicy`)

### Вакансии (`content/templates/content/vacancies_list.html`, view: `content/views.py:vacancies_list`)
- [x] Список вакансий из базы данных (`content/models.py:Vacancy`)
- [x] Описание каждой вакансии

### Отзывы (`content/templates/content/reviews_list.html`, view: `content/views.py:reviews_list`)
- [x] Список отзывов из базы данных (`content/models.py:Review`)
- [x] Имя (логин) автора (`review.display_name`)
- [x] Оценка (choices 1–5)
- [x] Текст отзыва
- [x] Дата (`<time datetime="...">`)
- [x] Кнопка «Добавить отзыв» (`content/templates/content/add_review.html`)
- [x] Кнопка ведёт на форму (view: `content/views.py:add_review`)
- [x] Кнопка «Отправить» сохраняет отзыв в базе

### Промокоды (`content/templates/content/promocodes.html`, view: `content/views.py:promocodes`)
- [x] Список действующих промокодов (`main/models.py:PromoCode` с `is_active=True`)
- [x] Архив промокодов (`is_active=False`)

---

## Технические требования HTML

### Метаданные и микроразметка
- [x] Микро-данные — `main/templates/main/product_detail.html` (`itemscope itemtype="http://schema.org/Product"`, `itemprop="name"`, `itemprop="price"`, `itemprop="description"`)
- [x] Метаданные документа — `templates/base.html` (`<meta name="description">`, `keywords`, `author`, `robots`, `viewport`)
- [x] Favicon — `templates/base.html` (`<link rel="icon">`)
- [ ] Проверка на W3C Validator — **скриншот `screenshots/16-validator.png`**

### Семантическая вёрстка
- [x] `<header>`, `<nav>`, `<main>`, `<footer>` — `templates/base.html`
- [x] `<section>`, `<article>`, `<aside>` — `templates/base.html` (aside с вертикальной навигацией), `content/templates/content/home.html` (section с баннерами)
- [x] `<figure>` и `<figcaption>` — `main/templates/main/product_detail.html`, `content/templates/content/news_list.html`

### Семантическое выделение текста
- [x] `<strong>`, `<em>` — `content/templates/content/home.html`
- [x] `<mark>` — `content/templates/content/home.html` («с 1998 года»), `content/templates/content/faq_list.html`
- [x] `<small>`, `<s>` — `content/templates/content/promocodes.html` (архивные коды)
- [x] `<sub>`, `<sup>` — `content/templates/content/faq_list.html`
- [x] `<code>`, `<var>`, `<samp>`, `<kbd>` — `content/templates/content/faq_list.html`
- [x] `<abbr>` — `content/templates/content/faq_list.html` (CMS)
- [x] `<dfn>` — `content/templates/content/faq_list.html`
- [x] `<q>`, `<blockquote>`, `<cite>` — `content/templates/content/faq_list.html`
- [x] `<time datetime="...">` — `content/templates/content/news_list.html`, `content/templates/content/reviews_list.html`, `content/templates/content/faq_list.html`

### Глобальные атрибуты
- [x] `id`, `class` — везде
- [x] `title` — `templates/base.html` (nav-ссылки), `content/templates/content/faq_list.html`
- [x] `lang` — `templates/base.html` (`<html lang="ru">`)
- [x] `accesskey` — `templates/base.html` (`accesskey="h"` на главной)
- [x] `tabindex` — `content/templates/content/faq_list.html`
- [x] `hidden` — `templates/base.html`
- [x] `data-*` — `main/templates/main/product_list.html` (`data-product-id`, `data-product-name`, `data-product-price`)
- [x] `contenteditable` — `content/templates/content/about.html` (блок «Заметки администратора»)

### Специальные элементы
- [x] Листинг кода — `content/templates/content/faq_list.html` (`<pre><code>`)
- [x] Четверостишие с `<br>` — `content/templates/content/faq_list.html`
- [x] Слово с `<wbr>` — `content/templates/content/faq_list.html`
- [x] Якоря — `content/templates/content/faq_list.html` (`<a href="#faq-end">`)
- [x] Ссылки `<a href="...">` — `templates/base.html` (nav)
- [x] `tel:` — `templates/base.html` (footer), `main/templates/main/contact_list.html`
- [x] `mailto:` — `templates/base.html`, `main/templates/main/contact_list.html`
- [x] Ссылка для скачивания — `content/templates/content/news_list.html` (`download="news-banner.jpg"`)

### Структурные элементы
- [x] `<ul>` — `templates/base.html` (навигация)
- [x] `<ol reversed>` — `content/templates/content/about.html` (история компании)
- [x] `<dl>/<dt>/<dd>` — `main/templates/main/product_detail.html`
- [x] Навигация горизонтальная — `templates/base.html` (`<header><nav>`)
- [x] Навигация вертикальная — `templates/base.html` (`<aside><nav>`)
- [x] `<div>`, `<span>` — везде

### Таблицы
- [x] `<th>` — `main/templates/main/contact_list.html`, `main/templates/main/product_list.html`
- [x] `<caption>` — `main/templates/main/contact_list.html`
- [x] `<thead>/<tbody>/<tfoot>` — `main/templates/main/cart.html`, `main/templates/main/checkout.html`
- [x] `colspan` — `main/templates/main/cart.html` (итоговая строка)
- [x] `headers` — `main/templates/main/contact_list.html` (`headers="h-name"`)
- [x] Числовые и текстовые данные

### Формы и элементы управления
- [x] `<form method="post">` — `content/templates/content/add_review.html`
- [x] `input type="text"` — регистрация (`users/templates/registration/signup.html`)
- [x] `input type="email"` — регистрация, чекаут
- [x] `input type="password"` — `users/templates/registration/login.html`
- [x] `input type="number"` — `main/templates/main/product_detail.html` (количество)
- [x] `input type="date"` — регистрация (дата рождения)
- [x] `input type="radio"` — `content/templates/content/reviews_list.html` (оценка), `main/templates/main/checkout.html`
- [x] `input type="checkbox"` — формы Django
- [x] `input type="submit"` / `reset` — `content/templates/content/reviews_list.html`
- [x] `<textarea>` — `content/templates/content/reviews_list.html`, `main/templates/main/checkout.html`
- [x] `<select>` / `<option>` — в админке, плюс `main/templates/main/cart.html` (выбор количества)
- [x] `<button>` — `main/templates/main/cart.html`
- [x] `<fieldset>` / `<legend>` — `content/templates/content/reviews_list.html`, `main/templates/main/checkout.html`
- [x] `<label>` — везде с формами
- [x] Валидация: `required`, `min`, `max`, `maxlength`, `pattern`, `type="email"` — регистрация, чекаут

### Мультимедиа
- [x] `<img>` с `alt` — везде
- [x] `<picture>`, `<source>`, `srcset` — `content/templates/content/home.html` (баннеры), `main/templates/main/product_detail.html`
- [x] Адаптив: разные картинки для разных ширин — `content/templates/content/home.html` (`<source media="(max-width: 600px)">`) **+1 балл**
- [x] `<video>` + `<source>` — `content/templates/content/about.html`
- [x] `<audio>` + `<source>` — `content/templates/content/about.html`
- [x] `<iframe>` — `content/templates/content/about.html` (карта, сертификат)

---

## Запуск

```bash
py -m pip install -r requirements.txt
py manage.py migrate
py manage.py runserver
```

Открыть: http://localhost:8000/