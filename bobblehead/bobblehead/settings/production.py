# production.py

# local.py

"""
Django settings for bobblehead project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

from django.conf import settings

if not settings.DEBUG and not settings.LOCAL_TEST:
    from config import django_secret
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    import os
    # Since we added a level (settings folder), we add a new level of os.path.dirname
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = django_secret.DJANGO_SECRET
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False

    # If DEBUG is off, ALLOWED_HOSTS must have values
    ALLOWED_HOSTS = ['www.nanoprojects.org', 'nanoprojects.org']

    # Application definition

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'projects',
        'user_profile',
        'submissions',
    )

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

    SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

    SESSION_SERIALIZER = "django.contrib.sessions.serializers.PickleSerializer"

    ROOT_URLCONF = 'bobblehead.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

    WSGI_APPLICATION = 'bobblehead.wsgi.application'

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            },
            'logfile': {
                'class': 'logging.handlers.WatchedFileHandler',
                'filename': '/var/log/django/error.log'
            },
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
            'django': {
                'handlers': ['logfile'],
                'level': 'ERROR',
                'propagate': False,
            },
        }
}

    # Database
    # https://docs.djangoproject.com/en/1.8/ref/settings/#databases

    from config import db_settings
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': db_settings.DB_NAME,
            'USER': db_settings.DB_USER,
            'PASSWORD': db_settings.PASSWORD,
            'HOST': db_settings.HOST,
            'PORT': db_settings.POST,
        }
    }

    # Internationalization
    # https://docs.djangoproject.com/en/1.8/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.8/howto/static-files/

    STATIC_URL = '/static/'

    STATIC_ROOT = '/var/www/bobblehead/static_root/'
    # os.path.join(os.path.dirname(BASE_DIR), "static_root")

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static", "bobblehead"),
    )
