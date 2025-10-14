FROM python:3.12

RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Установка uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh

RUN sh /uv-installer.sh && rm /uv-installer.sh

ENV PATH="/root/.local/bin/:$PATH"

WORKDIR /home/app/

# Установка зависимостей
COPY uv.lock pyproject.toml ./
RUN uv sync

# Копирование приложения
COPY . .
EXPOSE 8000
