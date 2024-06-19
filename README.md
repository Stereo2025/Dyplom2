## Описание

Это REST API проект на базе Django и Django REST Framework, который позволяет пользователям создавать, редактировать и удалять объявления. Кроме того, пользователи могут оставлять отзывы под объявлениями. API также поддерживает функционал авторизации и аутентификации пользователей с распределением ролей (пользователь и администратор). Администраторы могут управлять любыми объявлениями, в то время как пользователи могут управлять только своими объявлениями. Также реализован поиск объявлений по названию.

## Основной функционал

- Авторизация и аутентификация пользователей с использованием JWT (JSON Web Tokens).
- Распределение ролей (пользователь и администратор).
- CRUD операции для объявлений.
- Пользователь может оставлять отзывы под объявлениями.
- Поиск объявлений по названию.
- Пагинация списка объявлений (не более 4 объектов на странице).

## Используемые технологии

- Django
- Django REST Framework
- PostgreSQL
- Simple JWT
- Djoser
- drf-spectacular
- django-cors-headers
- django-filter

## Требования

- Python 3.8+
- PostgreSQL

## Запуск проекта

### Шаг 1. Клонирование репозитория

```sh
git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name
```

### Шаг 2. Установка зависимостей

Рекомендуется использовать виртуальное окружение для установки зависимостей. 

```sh
python -m venv venv
source venv/bin/activate  # для Windows используйте `venv\Scripts\activate`
pip install -r requirements.txt
```

### Шаг 3. Настройка базы данных

Создайте базу данных в PostgreSQL и настройте соединение в `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'your_db_host',
        'PORT': 'your_db_port',
    }
}
```

### Шаг 4. Применение миграций

```sh
python manage.py makemigrations
python manage.py migrate
```

### Шаг 5. Создание суперпользователя

```sh
python manage.py createsuperuser
```

Следуйте инструкциям на экране, чтобы создать суперпользователя.

### Шаг 6. Запуск сервера разработки

```sh
python manage.py runserver
```

Перейдите в браузере по адресу [http://localhost:8000](http://localhost:8000) для проверки работы приложения.

### Шаг 7. Просмотр документации API

Вы можете просмотреть документацию API по следующим URL:

- Swagger: [http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/)
- Redoc: [http://localhost:8000/api/schema/redoc/](http://localhost:8000/api/schema/redoc/)

## Дополнительные настройки

### Подключение CORS

Для корректной работы с фронтенд-приложениями, настройте CORS в `settings.py`:

```python
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',  # укажите ваш фронтенд адрес, если он отличается
]
```

### Настройка отправки email для восстановления пароля

Настройте параметры email в `settings.py` для отправки писем с восстановлением пароля:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
```

### Ссылки на документацию

- [Django REST Framework](https://www.django-rest-framework.org/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [Djoser](https://djoser.readthedocs.io/en/latest/)
- [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/)
- [django-cors-headers](https://pypi.org/project/django-cors-headers/)
- [django-filter](https://django-filter.readthedocs.io/en/stable/)