SECRET_KEY = "django-debug-key"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": "localhost",
        "PORT": "5432",
        "NAME": "db",
        "USER": "user",
        "PASSWORD": "password",
    },
}
