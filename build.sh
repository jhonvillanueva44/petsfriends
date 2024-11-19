#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Crear un superusuario automáticamente si no existe
echo "Creando superusuario si no existe..."

# Usando el comando de Django para crear un superusuario
python manage.py shell << EOF
from django.contrib.auth.models import User
from django.core.management import call_command
import sys

# Verifica si ya existe un superusuario
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@gmail.com', 'admin')
    print('Superusuario creado con éxito')
else:
    print('El superusuario ya existe')

EOF