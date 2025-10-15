import os
import sys
import zoneinfo
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_celery_beat",

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ru"

TIME_ZONE = os.environ.get("TZ", "UTC")
TIME_ZONE_OBJECT = zoneinfo.ZoneInfo(TIME_ZONE)

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Redis: Адрес для подключения
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")
REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}"

# Celery: Настройки брокера
CELERY_BROKER_URL = REDIS_URL
CELERY_RESULT_BACKEND = REDIS_URL

# Celery: Формат данных
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

# Celery: Прочие настройки
CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_DEFAULT_QUEUE = "default"
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = False


LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

LOG_TARGET = os.getenv("LOG_TARGET", "console")  # "console" или "file"
LOG_JSON = os.getenv("LOG_JSON", "0") == "1"  # 1 → JSON формат
LOG_DIR = os.getenv("LOG_DIR", "/var/log/app")  # если выбран file

if LOG_TARGET == "file":
    os.makedirs(LOG_DIR, exist_ok=True)

FORMATTERS = {
    "verbose": {
        "format": "[{asctime}] {levelname} {name}: {message}",
        "style": "{",
    },
    "json": {
        "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
        "fmt": "%(asctime)s %(levelname)s %(name)s %(message)s",
    },
}

HANDLERS = {
    "console": {
        "class": "logging.StreamHandler",
        "stream": sys.stdout,
        "formatter": "json" if LOG_JSON else "verbose",
    },
    "file": {
        "class": "logging.handlers.TimedRotatingFileHandler",
        "filename": os.path.join(LOG_DIR, "django.log"),
        "when": "midnight",  # ротация каждый день
        "backupCount": 30,  # храним 30 дней
        "encoding": "utf-8",
        "formatter": "json" if LOG_JSON else "verbose",
    },
}

active_handler = "file" if LOG_TARGET == "file" else "console"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": FORMATTERS,
    "handlers": {active_handler: HANDLERS[active_handler]},
    "root": {
        "handlers": [active_handler],
        "level": LOG_LEVEL,
    },
    "loggers": {
        "django": {"handlers": [active_handler], "level": LOG_LEVEL, "propagate": False},
        "django.request": {"handlers": [active_handler], "level": LOG_LEVEL,
                           "propagate": False},
        "gunicorn.error": {"handlers": [active_handler], "level": LOG_LEVEL,
                           "propagate": False},
        "gunicorn.access": {"handlers": [active_handler], "level": LOG_LEVEL,
                            "propagate": False},
        "uvicorn": {"handlers": [active_handler], "level": LOG_LEVEL, "propagate": False},
        "uvicorn.error": {"handlers": [active_handler], "level": LOG_LEVEL,
                          "propagate": False},
        "uvicorn.access": {"handlers": [active_handler], "level": LOG_LEVEL,
                           "propagate": False},
    },
}
PROJECT_ENV = os.environ.get("PROJECT_ENV", "local")
if PROJECT_ENV == "local":  # type: ignore
    from project.config.local import *  # noqa: F403

    STATICFILES_DIRS = [BASE_DIR / "static"]

elif PROJECT_ENV == "production":  # type: ignore
    from project.config.production import *  # noqa: F403

    STATIC_ROOT = BASE_DIR / "static"
