import os

AWS_ACCESS_KEY_ID=os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME='althaf-django-k8s'
AWS_S3_ENDPOINT_URL="https://blr1.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
    "ACL": "public-read"
}
AWS_LOCATION="https://althaf-django-k8s.blr1.digitaloceanspaces.com"
DEFAULT_FILE_STORAGE="django_k8s.cdn.backends.MediaRootS3BotoStorage"
STATICFILES_STORAGE="django_k8s.cdn.backends.StaticRootS3BotoStorage"

#With these settings in place, your Django application will store and serve static and media files from DigitalOcean Spaces, and the provided AWS access keys and endpoint URL will be used for authentication and file storage.

