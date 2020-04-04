from datetime import timedelta
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
    'rest_framework_jwt',
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
        'USER': os.environ.get('DJANGO_PG_USER', 'postgres'),
        'PASSWORD': os.environ.get('DJANGO_PG_PASSWORD', 'password1'),
        'HOST': os.environ.get('DJANGO_PG_HOST', 'localhost'),
        'PORT': os.environ.get('DJANGO_PG_PORT', 5432),
    },
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': 'Bearer',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

AUTH_USER_MODEL = 'user.Account'

PROXY_HOST = os.environ.get('PROXY_HOST', 'localhost')
PROXY_PORT = os.environ.get('PROXY_PORT', 8081)
NOTIFICATION_HOST = os.environ.get('NOTIFICATION_HOST', 'localhost')
NOTIFICATION_PORT = os.environ.get('NOTIFICATION_PORT', 8082)

SERVICE_HOST = os.environ.get('SERVICE_HOST', 'localhost')
SERVICE_PORT = os.environ.get('SERVICE_PORT', 8080)

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
