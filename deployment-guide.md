Test django
'''
python manage.py test
'''

2.Build Container

'''
docker build -f Dockerfile \
    -t registry.digitalocean.com/mask8s/django-k8s-web:latest \
    -t registry.digitalocean.com/mask8s/django-k8s-web:v1 \
    .
'''