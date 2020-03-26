from .common import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('TEST_DATABASE_NAME', '--'),
        'USER': os.environ.get('TEST_DATABASE_USER', 'postgres'),
        'PASSWORD': os.environ.get('TEST_DATABASE_PASSWORD', 'admin'),
        'HOST': os.environ.get('TEST_DATABASE_HOST', 'postgres'),
        'PORT': os.environ.get('TEST_DATABASE_PORT', '5432'),
    }
}

INSTALLED_APPS = INSTALLED_APPS + THIRD_PARTY_APPS + LOCAL_APPS
