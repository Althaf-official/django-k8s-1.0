#!/bin/bash
cd /app/
/opt/venv/bin/python manage.py collectstatic --noinput

#This script is useful for automating the process of collecting static files in a Django project, which is often done before deploying a Django application to a production server to ensure that all necessary static files (such as CSS, JavaScript, and images) are available and organized for serving to clients.
