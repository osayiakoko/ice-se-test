from .common import *


DEBUG = False


ALLOWED_HOSTS = [
    'projectzap.tk',
]


CORS_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = []


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('AWS_DB_NAME'),
        'USER': env('AWS_DB_USER'),
        'PASSWORD': env('AWS_DB_PASSWORD'),
        'HOST': env('AWS_DB_HOST'),
        'PORT': '5432',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')

AWS_S3_FILE_OVERWRITE = False
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_CUSTOM_DOMAIN = 'dcy0w1iq7775c.cloudfront.net'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}


STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
STATICFILES_STORAGE = 'config.storage_backends.StaticStorage'

MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
DEFAULT_FILE_STORAGE = 'config.storage_backends.MediaStorage'
