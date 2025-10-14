FROM python:3.12

ENV APP_HOME=/home/app \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends  \
    curl  \
    ca-certificates  && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/*

# Установка uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN chmod +x /uv-installer.sh && \
    UV_INSTALL_DIR=/usr/local/bin sh /uv-installer.sh && \
    rm /uv-installer.sh

ENV PATH="/root/.local/bin/:$PATH"

# Создание пользователя app
RUN mkdir -p /home/app && \
    echo 'app:x:1000:1000::/home/app:/bin/bash' >> /etc/passwd && \
    echo 'app:x:1000:' >> /etc/group && \
    chown 1000:1000 /home/app

WORKDIR $APP_HOME

# Установка зависимостей
COPY --chown=1000:1000 uv.lock pyproject.toml ./
RUN uv sync

# Копирование приложения
USER 1000:1000
COPY --chown=1000:1000 . $APP_HOME
