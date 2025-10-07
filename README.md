# 🚇 Тестовое задание: ГУП «Московский метрополитен»

Данный проект реализует веб-приложение на **Django + Django REST Framework**, соответствующее макету из тестового задания.  
Приложение включает **бэкенд (API)** и **фронтенд (HTML + Bootstrap + JS)** для отображения данных.

---

## 📌 Функционал

### 🖥 Фронтенд
- **Главная страница**: отображает фото пользователя и его ФИО.
- **Страница «Посты»**: список постов (заголовок + содержание).
- **Страница «Пользователи»**: таблица с ФИО и email; клик по любой строке открывает **модальное окно** с детальной информацией (ФИО, email, адрес).
- Навигация: логотип слева, пункты меню — «Главная», «Посты», «Пользователи».

### 🌐 Бэкенд (REST API)
Поддерживает полный CRUD для сущностей:

#### Пользователи (`/api/users/`)
- `GET /api/users/` — список пользователей  
- `GET /api/users/{id}/` — детализация  
- `POST /api/users/` — создание  
- `PUT /api/users/{id}/` — полное обновление  
- `PATCH /api/users/{id}/` — частичное обновление  
- `DELETE /api/users/{id}/` — удаление  

#### Посты (`/api/posts/`)
- `GET /api/posts/` — список постов  
- `GET /api/posts/{id}/` — детализация  
- `POST /api/posts/` — создание  
- `PUT /api/posts/{id}/` — обновление  
- `DELETE /api/posts/{id}/` — удаление  

> Все URL **должны заканчиваться на `/`** (требование Django при `APPEND_SLASH=True`).

---

## 🛠 Технологии
- **Backend**: Python, Django, Django REST Framework
- **Frontend**: HTML, Bootstrap 5, Vanilla JavaScript
- **База данных**: SQLite (по умолчанию)
- **Файлы**: поддержка загрузки фото пользователей

---

## 🚀 Установка и запуск

1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/dimoniiio/metro_django.git
   cd metro_django
   ```

2. **Создайте и активируйте виртуальное окружение**:
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/macOS:
   source venv/bin/activate
   ```

3. **Установите зависимости**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Выполните миграции**:
   ```bash
   python manage.py migrate
   ```

5. **(Опционально) Создайте суперпользователя**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Запустите сервер**:
   ```bash
   python manage.py runserver
   ```

7. **Откройте в браузере**:
   - Главная: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - Админка: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
   - API: [http://127.0.0.1:8000/api/users/](http://127.0.0.1:8000/api/users/)

---

## 📁 Структура проекта

```
metro_app/
├── users/              # Модель, сериализатор, ViewSet для пользователей
├── posts/              # Модель, сериализатор, ViewSet для постов
├── frontend/           # Шаблоны и views для HTML-страниц
├── static/
│   └── img/
│       └── logo.gif    # Логотип в шапке
├── templates/          # Общие шаблоны (base.html, home.html и др.)
├── media/              # Загруженные фото пользователей
└── manage.py
```

---

## ⚠️ Важно

- Все API-запросы должны использовать **URL со слешем в конце** (например, `/api/users/`).
- Для загрузки фото убедитесь, что папка `media/` доступна (настроена через `MEDIA_URL`).
- В продакшене замените `DEBUG = True` на `False` и настройте статику/медиа правильно.

---


# Контакты 


## Если у вас есть вопросы или предложения, свяжитесь с нами: 

Email: [Дмитрий Иванов](dimoniiio@yandex.ru) 

GitHub: [dimoniiio](https://github.com/dimoniiio)

