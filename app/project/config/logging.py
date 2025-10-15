import os
import sys

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

LOG_TARGET = os.getenv("LOG_TARGET", "console")  # "console" или "file"
LOG_JSON = os.getenv("LOG_JSON", "0") == "1"  # 1 → JSON формат
LOG_DIR = os.getenv("LOG_DIR", "/var/log/app")  # если выбран file

print(LOG_TARGET)
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
