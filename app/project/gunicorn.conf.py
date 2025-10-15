import multiprocessing

# Базовые настройки
bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "uvicorn.workers.UvicornWorker"

# Таймауты
timeout = 60
graceful_timeout = 30
keepalive = 5

# Логи
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Дополнительно
# preload_app = True  # загружать приложение до форка (ускоряет старты)
# max_requests = 1000  # перезапуск воркера после N запросов
# max_requests_jitter = 50  # добавляет случайность к перезапускам
