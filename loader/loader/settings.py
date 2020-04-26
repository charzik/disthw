import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '123')

DEBUG = os.environ.get('DJANGO_DEBUG', True)

ALLOWED_HOSTS = [
    os.environ.get('INTERNAL_SERVICES_ALLOWED_HOSTS', 'localhost'),
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'rest_framework',
    'items_importer',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'estore_db',
        'USER' : os.environ.get('DJANGO_PG_USER', 'postgres'),
        'PASSWORD' : os.environ.get('DJANGO_PG_PASSWORD', 'password1'),
        'HOST' : os.environ.get('DJANGO_PG_HOST', 'localhost'),
        'PORT' : os.environ.get('DJANGO_PG_PORT', 5432),
    }
}

CELERY_BROKER_URL = 'amqp://%s:%s@%s:%s/%s' % (
    os.environ.get('DJANGO_BROKER_USER', 'disthw'),
    os.environ.get('DJANGO_BROKER_PASSWORD', 'password1'),
    os.environ.get('DJANGO_BROKER_HOST', 'localhost'),
    os.environ.get('DJANGO_BROKER_PORT', 5672),
    os.environ.get('DJANGO_BROKER_VHOST', 'disthw_host'),
)
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

ROOT_URLCONF = 'loader.urls'

WSGI_APPLICATION = 'loader.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
