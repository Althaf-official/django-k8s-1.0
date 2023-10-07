## login with API tocken

'''
docker login registry.digitalocean.com

'''

# build docker image
"""
docker build -t registry.digitalocean.com/mask8s/django-k8s-web:latest -f Dockerfile .

"""

# push your container image
'''
docker push registry.digitalocean.com/mask8s/django-k8s-web --all-tags
'''

