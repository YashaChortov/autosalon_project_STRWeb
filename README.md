# IGI_LabWork5

Проект — сайт автосалона «АвтоПрестиж» на Django.

## Стек
- Python 3.12
- Django 4.2
- SQLite
- HTML5 + CSS3 

## Запуск

    py -m venv venv
    venv\Scripts\activate
    py -m pip install -r requirements.txt
    py manage.py migrate
    py manage.py runserver

Открыть http://localhost:8000/

---

# ЛР1 — HTML

## Страницы
- [x] Главная: логотип, баннеры, каталог, последняя статья, партнёры
- [x] Страница товара с кнопкой «Добавить в корзину»
- [x] Корзина (оплатить, удалить, изменить количество)
- [x] Страница оплаты
- [x] О компании (логотип, видео, история, реквизиты, сертификат)
- [x] Новости (заголовок, краткое содержание, картинка, «Читать далее»)
- [x] Словарь терминов (раскрывающиеся ответы)
- [x] Контакты (фото, должность, телефон, почта)
- [x] Политика конфиденциальности
- [x] Вакансии (список с описанием)
- [x] Отзывы (имя, оценка, текст, дата, форма добавления)
- [x] Промокоды (действующие + архив)

## HTML-требования
- [x] Микроразметка (itemscope, itemtype, itemprop)
- [x] Метаданные документа (description, keywords, author, robots)
- [x] Favicon
- [x] Семантические теги (header, nav, main, footer, section, article, aside)
- [x] figure / figcaption
- [x] Семантическое выделение (strong, em, mark, small, s, sub, sup)
- [x] Специальные элементы (code, var, samp, kbd, abbr, dfn, q, cite, time)
- [x] Глобальные атрибуты (id, class, title, lang, accesskey, tabindex, hidden, data-*)
- [x] contenteditable
- [x] Листинг кода (<pre><code>)
- [x] Четверостишие с <br>, слово с <wbr>
- [x] Якоря
- [x] Ссылки tel:, mailto:, download
- [x] Списки ul, ol, dl
- [x] Таблицы с заголовочными ячейками, caption, thead/tbody/tfoot, colspan, headers
- [x] Формы и все виды input, textarea, select, button, fieldset, label
- [x] Валидация форм (required, min, max, maxlength, pattern)
- [x] Изображения, адаптивные изображения (picture, srcset)
- [x] Видео и аудио
- [x] iframe (карта, сертификат)
- [x] Проверка на W3C Validator
- [x] Проверка на HTML5 Outliner

---

# ЛР2 — CSS

Стили вынесены в один файл `static/css/style.css`, подключён в `base.html`.
Тема — тёмная (графит + бордово-красные акценты).

## Селекторы
- [x] Элементов (h2, article p, table)
- [x] Классов (.lead, .review, .product-grid)
- [x] Атрибутов:
    - [x] начинается с подстроки — a[href^="http"]
    - [x] заканчивается подстрокой — a[href$=".pdf"]
    - [x] точное значение — a[target="_blank"]
- [x] Комбинации AND — article.review, header nav > ul > li > a
- [x] Селектор потомков — article p
- [x] Селектор дочерних — main > p

## Псевдоклассы
- [x] Динамические состояния ссылок: :link, :visited, :hover, :active, :focus
- [x] Положение в списке/таблице: :first-child, :last-child, :nth-child(odd/even)
- [x] Состояния формы: :required, :optional, :disabled, :valid, :invalid, :in-range, :out-of-range, :checked
- [x] Кавычки по языку: q:lang(ru/en/de/fr)

## Псевдоэлементы
- [x] ::first-letter — первая буква абзаца
- [x] ::first-line — капитель первой строки
- [x] ::before / ::after — контекст в начале и конце фрагмента
- [x] ::before — маркеры-юникод в списке (★)
- [x] ::selection — стиль выделенного текста

## Шрифты
- [x] Основной шрифт из Google Fonts (Montserrat)
- [x] Альтернативный (Arial)
- [x] Семейство (sans-serif)
- [x] Шрифт для заголовков (Roboto Slab, serif)

## Медиа-запросы
- [x] По ширине (900px, 480px)
- [x] По ориентации и высоте (landscape + max-height)
- [x] Для печати (@media print)

## Текст
- [x] Отступы и поля (margin, padding)
- [x] text-transform (uppercase для заголовков)
- [x] Красная строка (text-indent)
- [x] Межстрочный интервал (line-height)
- [x] Капитель (font-variant: small-caps)
- [x] Интервал между словами (word-spacing)
- [x] Интервал между символами (letter-spacing)
- [x] Перенос и разрыв слов (hyphens, overflow-wrap)
- [x] Шрифты и выравнивание текста
- [x] Задний фон сайта (radial-gradient)

## Раскладка
- [x] CSS Grid Layout для каталога товаров (.product-grid)
- [x] CSS Grid для общего макета (sidebar + main)
- [x] Flexbox для контактов (.contacts-flex)
- [x] Flexbox для партнёров (.partners)
- [x] Круглые блоки партнёров: ширина, цвет, тень (border-radius: 50%, box-shadow)
- [x] Шрифт и кернинг для названия компании (font-kerning, letter-spacing)
- [x] Позиционирование для последней статьи (.latest-article — position: relative)
- [x] Навигация фиксируется при прокрутке (position: sticky)

## Страницы по отдельности

### О компании
- [x] Трансформация логотипа (rotate + scale при наведении)
- [x] Границы сертификата из графического файла (border-image + вендорные префиксы)
- [x] Градиент на сертификате
- [x] Слоистость (z-index)
- [x] История по годам списком
- [x] Реквизиты моноширинным шрифтом
- [x] Видео и аудио

### Новости
- [x] Overflow + многоточие для краткого содержания
- [x] Многоколоночный макет (columns: 2 300px)

### Словарь терминов
- [x] Стили для details/summary
- [x] Раскрытие по клику
- [x] Псевдоэлементы ::first-letter, ::first-line для демонстрации

### Контакты
- [x] Flexbox для карточек сотрудников
- [x] Карточки сжимаются/растягиваются (flex: 1 1 260px)

### Вакансии
- [x] Плавающие блоки (float: left)
- [x] Clear для переноса строки (clear: left)
- [x] Раскрывающиеся блоки <details> вместо обрезанного текста
- [x] Убрано зелёное оформление, используем общий бордовый акцент

### Отзывы
- [x] Ключевые слова шрифтов для формы
- [x] Псевдоклассы на элементах формы
- [x] Средний рейтинг считается автоматически
- [x] Убраны буквицы внутри отзывов (чтобы даты и цифры не выделялись)

### Промокоды
- [x] Разные стили для активных и архивных кодов
- [x] Списки оформлены

## Таблицы
- [x] Убраны двойные линии (border-collapse: collapse)
- [x] Заголовок над таблицей (caption-side: top)
- [x] Горизонтальное и вертикальное выравнивание
- [x] Стилизация чётных строк
- [x] Подсветка при наведении
- [x] Фон пустых ячеек (:empty)

## Анимация и трансформация
- [x] Анимация на главной по варианту 12 (автосалон): машина выезжает, брызги, разворот, мигание фарами, появление названия
- [x] Прелоадер внизу страницы (пульсирующие точки)
- [x] Анимация бесконечная (animation-iteration-count: infinite)
- [x] 3D-эффект (perspective + rotateY)
- [x] Трансформация логотипа при наведении

## Прочее
- [x] Изменение курсора при наведении на кнопки (cursor: pointer, cursor: grabbing)
- [x] Виды градиентов: линейный, радиальный, повторяющийся
- [x] Подключение шрифтов через Google Fonts

---

## Структура

    IGI_LabWork5/
    ├── autosalon_project/       # настройки Django
    ├── main/                    # товары, заказы, клиенты, сотрудники
    ├── content/                 # новости, отзывы, вакансии, FAQ
    ├── users/                   # регистрация, роли
    ├── analytics/               # админ-панель
    ├── templates/               # базовые шаблоны
    ├── static/
    │   ├── css/style.css        # все стили
    │   ├── logo.png
    │   └── favicon.ico
    ├── media/                   # загруженные файлы
    └── manage.py
