import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '123')

DEBUG = os.environ.get('DJANGO_DEBUG', False)

ALLOWED_HOSTS = [
    os.environ.get('INTERNAL_SERVICES_ALLOWED_HOSTS', 'localhost'),
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'rest_framework',
    'email_sender',
]

DATABASES = {
    'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': ':memory:'},
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

EMAIL_USER = os.environ.get('EMAIL_USER', '')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD', '')

ROOT_URLCONF = 'notification.urls'

WSGI_APPLICATION = 'notification.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
