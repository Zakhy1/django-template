# Project

**Project** — Краткое описание проекта

---

## Оглавление

- [Описание](#описание)
- [Функциональность](#функциональность)
- [Технологический стек](#технологический-стек)
- [Архитектура](#архитектура)
- [Установка и запуск](#установка-и-запуск)
- [Переменные окружения](#переменные-окружения)
- [Структура проекта](#структура-проекта)

---

## Описание

В чем суть проекта, какие проблемы решает, назначение

---

## Функциональность

1. [ ] Хранить что нибудь
2. [ ] Генерировать мильон рублей в наносек 

## Технологический стек

Ниже приведена таблица, отображающая технологический стек на проект.

| Компонент             | Используемая технология               |
|-----------------------|---------------------------------------|
| Язык программирования | **Python 3.12**                       |
| Backend               | **Django 5.2**, Django REST Framework |
| Frontend              | SPA и/или Django templates            |
| База данных           | **PostgreSQL 17**                     |
| Очереди / задачи      | Celery + Redis                        |
| Контейнеризация       | Docker / Docker Compose               |
| Мониторинг            | Prometheus + Grafana (опционально)    |

## Архитектура
Здесь надо описать архитектуру приложения

## Установка и запуск

## Переменные окружения
[Файл](example.env), на основе которого можно создать .env
[Файл](local.env), с которым можно вести локальную разработку

Список и назначение переменных окружения:
```dotenv
# Postgres variables
POSTGRES_PASSWORD=password
POSTGRES_USER=user
POSTGRES_DB=db
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

# Redis variables
REDIS_HOST=redis
REDIS_PORT=6379

# Django variables
PROJECT_ENV=production # Имя окружения (local, production)
SECRET_KEY=sample-key  # Секретный ключ для шифрования сессий
DEBUG=0                # Состояние отладки

LOG_LEVEL=INFO         # Минимальный уровень логирования
LOG_TARGET=file        # Куда писать логи (console, file)
LOG_JSON=1             # JSON формат логов (1,0)
LOG_DIR=log            # Каталог, куда писать логи (от app/)

TZ=Asia/Krasnoyarsk    # Временная зона приложения
```

## Структура проекта

```
├── 📂 app
│   ├── 📁 log
│   ├── 📁 media
│   ├── 📁 static
│   ├── 📂 project
│   │   ├── 📄 __init__.py
│   │   ├── 📄 asgi.py
│   │   ├── 📄 celery.py
│   │   ├── 📂 config
│   │   │   ├── 📄 __init__.py
│   │   │   ├── 📄 app_info.py
│   │   │   ├── 📄 celery_settings.py
│   │   │   ├── 📄 local.py
│   │   │   ├── 📄 logging.py
│   │   │   └── 📄production.py
│   │   ├── 📄 gunicorn.conf.py
│   │   ├── 📄 settings.py
│   │   ├── 📄 urls.py
│   │   └── 📄 wsgi.py
│   ├── 📄 Dockerfile
│   ├── 📄 manage.py
│   ├── 📄 pyproject.toml
│   └── 📄 uv.lock
├── 📂 nginx
│   ├── 📂 configs
│   │   └── 📄 site.conf
│   └── 📄 nginx.conf
├── 📄 local.env
├── 📄 example.env
├── 📄 docker-compose.yml
├── 📄 ruff.toml
└── 📄 README.md
```
