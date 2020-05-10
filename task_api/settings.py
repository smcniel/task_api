"""Django settings for task_api project."""

import os
from decouple import config, Csv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# if DEBUG:
#     INTERNAL_IPS = ['127.0.0.1', ]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'taskapp',
]

# if DEBUG:
#     INSTALLED_APPS += ['debug_toolbar', ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# if DEBUG:
#     MIDDLEWARE += [
#         'debug_toolbar.middleware.DebugToolbarMiddleware',
#     ]

# if DEBUG:
#     DEBUG_TOOLBAR_PANELS = [
#         'debug_toolbar.panels.versions.VersionsPanel',
#         'debug_toolbar.panels.timer.TimerPanel',
#         'debug_toolbar.panels.settings.SettingsPanel',
#         'debug_toolbar.panels.headers.HeadersPanel',
#         'debug_toolbar.panels.request.RequestPanel',
#         'debug_toolbar.panels.sql.SQLPanel',
#         'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#         'debug_toolbar.panels.templates.TemplatesPanel',
#         'debug_toolbar.panels.cache.CachePanel',
#         'debug_toolbar.panels.signals.SignalsPanel',
#         'debug_toolbar.panels.logging.LoggingPanel',
#         'debug_toolbar.panels.redirects.RedirectsPanel',
#     ]

ROOT_URLCONF = 'task_api.urls'

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

WSGI_APPLICATION = 'task_api.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
