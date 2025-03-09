"""Модуль формирования окружения и загрузки настроек."""

from project.settings.app_info import *  # noqa: F403
from project.settings.base import *  # noqa: F403
import os

# Вызывается при импорте модуля settings

PROJECT_ENV = os.environ.get("PROJECT_ENV", "local")


if PROJECT_ENV == "local":
    from project.settings.local import *  # noqa: F403

    STATICFILES_DIRS = [os.path.join(os.path.dirname(BASE_DIR), "static")]

    print("Загружены локальные настройки")
elif PROJECT_ENV == "production":
    from project.settings.production import *  # noqa: F403

    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")

    print("Загружены боевые настройки")
