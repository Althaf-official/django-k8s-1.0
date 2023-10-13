from storages.backends.s3boto3 import S3Boto3Storage

class StaticRootS3BotoStorage(S3Boto3Storage):
    location = "static"

class MediaRootS3BotoStorage(S3Boto3Storage):
    location ='media'

# custom storage classes in your Django project, you can seamlessly serve and store static and media files on Amazon S3, which is a common practice for deploying Django applications to production environments.
