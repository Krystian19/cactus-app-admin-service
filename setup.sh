#!/bin/sh

# Run migrations
python3 manage.py migrate

# Create a superuser
echo "from django.contrib.auth.models import User; User.objects.create_superuser('$DJANGO_ADMIN_USER', 'admin@example.com', '$DJANGO_ADMIN_PASSWORD')" | python3 manage.py shell

# Run the project
python3 manage.py runserver 0.0.0.0:8000