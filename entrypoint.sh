#!/bin/bash


#until pg_isready -h postgres -p 5432 -U postgres; do
 # echo "Esperando a que PostgreSQL esté listo..."
  #sleep 2
#done

# Ejecutar migraciones si tenés (ej: flask db upgrade)

# Crear admin
python create_admin.py

# Lanzar gunicorn
exec gunicorn -w 4 -b 0.0.0.0:5000 "app:create_app()"
