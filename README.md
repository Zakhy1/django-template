# Project name

**Project name** — short description

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

long description

---

## Функциональность

1. [ ] list functions

## Технологический стек

Ниже приведена таблица, отображающая технологический стек на проект.

| Компонент             | Используемая технология               |
|-----------------------|---------------------------------------|
| Язык программирования | **Python 3.12**                       |
| Backend               | **Django 5.2**, Django REST Framework |
| Frontend              | SPA и/или Django templates            |
| База данных           | **PostgreSQL**                        |
| Очереди / задачи      | Celery + Redis                        |
| Контейнеризация       | Docker / Docker Compose               |
| Мониторинг            | Prometheus + Grafana (опционально)    |

## Архитектура

## Установка и запуск

## Переменные окружения

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
