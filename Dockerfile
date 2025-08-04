# Usa la imagen base oficial de Python
FROM python:bullseye


# Establece el directorio de trabajo
WORKDIR /app

# Copia los requisitos de la aplicación
COPY requirements.txt .

# ---
## Prepara el entorno del sistema y instala dependencias
# ---
RUN apt-get update && \
    apt-get install -y --no-install-recommends gnupg2 curl ca-certificates && \
    apt-get update && \
    # Instala las dependencias necesarias de la aplicación
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    # Limpia el caché de APT para mantener la imagen ligera
    rm -rf /var/lib/apt/lists/*

# ---
## Instala las dependencias de Python
# ---
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --root-user-action=ignore -r requirements.txt && \
    pip install --root-user-action=ignore gunicorn


# ---
## Copia el código de la aplicación y ejecuta el comando
# ---
COPY . .

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]