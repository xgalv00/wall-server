from .base import rel


# logging
LOG_FILES_DIR = rel('logs')
LOG_FILE = LOG_FILES_DIR.child('app.log')
LOG_FILE_CELERY = LOG_FILES_DIR.child('celery.log')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'mail_admins': {
            'level': 'WARN',
            'filters': ['require_debug_false',],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'logfile': {
            'level': 'DEBUG',
            'filters': ['require_debug_false'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_FILE,
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard'
        },
        'logfile_celery': {
            'level': 'WARN',
            'filters': [],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_FILE_CELERY,
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['console', 'logfile'],
            'propagate': True,
            'level': 'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'celery': {
            'handlers': ['console', 'logfile_celery'],
            # 'handlers': ['console', 'logfile_celery', 'mail_admins'],
            'level': 'WARN',
            'propagate': True,
        }
    }
}
