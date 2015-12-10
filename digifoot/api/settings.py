# -*- coding: utf-8 -*-
"""
Django settings for digifootapi project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
from __future__ import unicode_literals
from datetime import timedelta
import datetime

from django.utils.translation import ugettext_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@z1=#_7#j9icxyu$7_x*5#q*y2oy==o6=67$=pcr-=#d0f!=1o'


# Application definition

INSTALLED_APPS = (
                     'django_extensions',
                     'django.contrib.auth',
                     'django.contrib.contenttypes',
                     'django.contrib.sessions',
                     'django.contrib.messages',
                     'django.contrib.staticfiles',
                     'django.contrib.humanize',
                     'django.contrib.admin',
                     'rest_framework',
                     'digifoot.api.apps.users',
                     'digifoot.api.apps.sparks',
                     'digifoot.api.apps.league',
                 )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'digifoot.api.apps.sparks.middleware.SparkMiddleware',
)

if DEBUG:
    MIDDLEWARE_CLASSES += ('digifoot.lib.middlewares.ErrorHandlingMiddleware', )

ROOT_URLCONF = 'digifoot.api.urls'
WSGI_APPLICATION = 'digifoot.api.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'digifoot', 'api', 'locale'),
)

ugettext = lambda s: s
LANGUAGES = (
    ('en', ugettext('English')),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CASSETTES_DIR = os.path.join(BASE_DIR, 'digifoot', 'cassettes')

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}
SENTRY_AUTO_LOG_STACKS = True

ADMINS = (
    ('Bartosz Hernas', 'b@hern.as'),
    ('Michal Hernas', 'm@hern.as'),
)

AUTH_USER_MODEL = 'users.User'

JWT_AUTH = {
    'JWT_RESPONSE_PAYLOAD_HANDLER': "digifoot.api.apps.users.services.jwt_response_payload_handler",
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=30),
}

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES = {}
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']


DEBUG = True


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^9^o7j-xm1js#$9_$8b9xdpl&(!k60(t=h-$u!g6av_3(lvx_b'


if not DATABASES['default']:
    DATABASES = {
        'default': {
            'ATOMIC_REQUESTS': True,
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'digifoot',
            'USER': 'digifoot',
            'PASSWORD': 'digifoot',
            'HOST': 'localhost',
            'PORT': '',
        }
    }


SERVER_EMAIL = "b@hern.as"


TWITTER_ACCOUNT = {
    'consumer_key': os.environ.get('TWITTER_ACCOUNT_CK', ''),
    'consumer_secret': os.environ.get('TWITTER_ACCOUNT_CS', ''),
    'access_token_key': os.environ.get('TWITTER_ACCOUNT_TK', ''),
    'access_token_secret': os.environ.get('TWITTER_ACCOUNT_TS', ''),
}

SPARK_ACCOUNT = {
    'auth_user': 'spark',
    'auth_password': 'spark',
    'username': os.environ.get('SPARK_ACCOUNT_U', ''),
    'password': os.environ.get('SPARK_ACCOUNT_P', ''),
}
