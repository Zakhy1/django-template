# Информация о приложении
import os
import zoneinfo

SITE_TITLE = "Шаблон проекта"
SITE_TITLE_S = "Шаблон проекта"
APP_VERSION = "0.0.00.0"
APP_VEK = "2023 - 2025гг"
APP_COPPIRIGHT = "Шаблон проекта"

KEYWORDS = ""
DESCRIPTION = "Шаблон проекта"
AUTHOR = "#"

# Языковые и временные настройки
LANGUAGE_CODE = "ru"

TIME_ZONE = os.environ.get("TZ", "UTC")
TIME_ZONE_OBJECT = zoneinfo.ZoneInfo(TIME_ZONE)

USE_I18N = True

USE_TZ = True
