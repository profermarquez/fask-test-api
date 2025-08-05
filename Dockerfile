# Usa la imagen base oficial de Python
FROM python:3.11-slim-bullseye


# Establece el directorio de trabajo
WORKDIR /app

# Copia los requisitos de la aplicación
COPY requirements.txt .

# Crear usuario sin privilegios


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
RUN useradd -m -s /bin/bash appuser

# Establecer permisos del directorio
RUN chown -R appuser:appuser /app

# Cambiar al usuario no-root
USER appuser