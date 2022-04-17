from .common import *


DEBUG = True

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': '5432',
    }
}


# REST FRAMEWORK SETTINGS
REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append(
    'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer'
)
REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'].append(
    'rest_framework.authentication.SessionAuthentication'
)


# SWAGGER SETTINGS
SWAGGER_SETTINGS['USE_SESSION_AUTH'] = True
SWAGGER_SETTINGS['SECURITY_DEFINITIONS']['Basic'] = {'type': 'basic'}
