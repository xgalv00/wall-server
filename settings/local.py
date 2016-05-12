import sys

from .prod import *


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wall',
        'USER': 'webmaster',
        'PASSWORD': 'test123',
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
}
