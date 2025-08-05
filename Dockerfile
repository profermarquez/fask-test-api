
FROM python:3.12-slim-bullseye
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && \
    apt-get install -y --no-install-recommends gnupg2 curl ca-certificates && \
    apt-get update && \
    # Instala las dependencias necesarias de la aplicación
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    # Limpia el caché de APT para mantener la imagen ligera
    rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --root-user-action=ignore -r requirements.txt && \
    pip install --root-user-action=ignore gunicorn
COPY . .
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
# creo y cambio el usuario por seguridad
RUN useradd -m -s /bin/bash appuser
RUN chown -R appuser:appuser /app
USER appuser