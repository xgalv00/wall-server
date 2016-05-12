"""
Django base settings for start a project
"""

# -*- coding: utf-8 -*-
import os
from django.core.urlresolvers import reverse_lazy
# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured

from unipath import Path
# settings.py
from os.path import join, dirname
import dotenv

def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return os.environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)

####### PATH CONFIGURATION ###########
PROJECT_DIR = Path()


def rel(*x):
    return PROJECT_DIR.child(*x)

os.sys.path.insert(0, rel('apps'))

MEDIA_ROOT = os.environ.get('MEDIA_ROOT', rel('public', 'media'))

MEDIA_URL = '/media/'

IMAGE_ROOT = os.path.join(MEDIA_ROOT, 'images')
IMAGE_URL = os.path.join(MEDIA_URL, 'images/')

STATIC_ROOT = os.environ.get('STATIC_ROOT', rel('public', 'static'))
STATIC_URL = '/static/'
STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
######################################

########## ENVIRONMENT SETTINGS ######
dotenv.read_dotenv()

SECRET_KEY = get_env_setting('SECRET_KEY')
ALLOWED_HOSTS = get_env_setting('ALLOWED_HOSTS').split()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('DEBUG', False))
######################################

# Application definition
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'common.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

################### PROJECT ##########################

# celery
BROKER_URL = 'redis://localhost'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERYD_POOL_RESTARTS = True

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    # ]
    'PAGE_SIZE': 10
}

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
)
LOGIN_URL = '/'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None

######################################################