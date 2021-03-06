from .common import *

DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True

THIRD_PARTY_APPS = THIRD_PARTY_APPS + [
    'django_extensions',
]

INSTALLED_APPS = INSTALLED_APPS + THIRD_PARTY_APPS + LOCAL_APPS
