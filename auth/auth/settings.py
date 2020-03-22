import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '123')

DEBUG = os.environ.get('DJANGO_DEBUG', False)

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # django 
    'django.contrib.auth',
    'django.contrib.contenttypes',

    # rest framework
    'rest_framework',
    'rest_framework.authtoken',

    # curtom apps
    'user',
    'proxy',
]

ROOT_URLCONF = 'auth.urls'

WSGI_APPLICATION = 'auth.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'auth_db',
        'USER' : os.environ.get('DJANGO_PG_USER', 'postgres'),
        'PASSWORD' : os.environ.get('DJANGO_PG_PASSWORD', 'password1'),
        'HOST' : os.environ.get('DJANGO_PG_HOST', 'localhost'),
        'PORT' : os.environ.get('DJANGO_PG_PORT', 5432),
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}

AUTH_USER_MODEL = 'user.Account'

PROXY_HOST = os.environ.get('PROXY_HOST', 'localhost')

PROXY_PORT = os.environ.get('PROXY_PORT', 8081)

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

