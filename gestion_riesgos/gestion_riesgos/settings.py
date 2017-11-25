"""
Django settings for gestion_riesgos project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+hh+-*p(=f^$1p9y9y78u&p16)qye2539fjs8vo&am!*!w7(wj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []#['52.90.156.149']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'general',
    'administracion',
    'procesos',
    'bootstrapform'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gestion_riesgos.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'general', 'templates'),
            os.path.join(BASE_DIR, 'procesos', 'Templates'),
            os.path.join(BASE_DIR, 'administracion', 'Templates'),
        ],
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

WSGI_APPLICATION = 'gestion_riesgos.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'Procesos3',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': 'DESKTOP-P4PU9JU',
    }
}

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'sql_server.pyodbc', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': 'Procesos2',                      # Or path to database file if using sqlite3.
#         'USER': 'bidss',                      # Not used with sqlite3.
#         'PASSWORD': 'admin123',                  # Not used with sqlite3.
#         'HOST': 'mssqlserver.canbbevbcgld.us-west-2.rds.amazonaws.com',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'TicketsBD.sqlite3'), #'/var/www/html/Tickets/TicketsBD.sqlite3',
#     }
# }



os.environ["ODBCSYSINI"] = "/etc"


# DATABASES = {
#     'default': {
#         'ENGINE': 'sql_server.pyodbc', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': 'Procesos2',                      # Or path to database file if using sqlite3.
#         'USER': 'bidss',                      # Not used with sqlite3.
#         'PASSWORD': 'admin123',                  # Not used with sqlite3.
#         'HOST': 'sqlserverdatasource',                      # Set to empty string for localhost. Not used with sqlite3.
#         'PORT': '1433',                      # Set to empty string for default. Not used with sqlite3.
#         'OPTIONS': {
#                 'host_is_server': False,
#                 'dsn': 'sqlserverdatasource',
#         },
#     }
# }
# DATABASE_NAME = 'Procesos2'
# DATABASE_HOST = 'sqlserverdatasource'
# DATABASE_PORT = '1433'
# DATABASE_USER = 'bidss'
# DATABASE_PASSWORD = 'admin123'
# DATABASE_OPTIONS = {
#         'host_is_server': False,
#         'dsn': 'sqlserverdatasource',
# }

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'sql_server.pyodbc', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': 'Procesos2',                      # Or path to database file if using sqlite3.
#         'USER': 'bidss',                      # Not used with sqlite3.
#         'PASSWORD': 'admin123',                  # Not used with sqlite3.
#         'HOST': 'mssqlserver.canbbevbcgld.us-west-2.rds.amazonaws.com',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Tegucigalpa'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/').replace('\\', '/')
#MEDIA_ROOT =  os.path.join(BASE_DIR, 'media/')


# MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media', 'upload')

# STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'static-only')

# STATICFILES_DIRS = (
#     os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'static'),
# )

# TEMPLATE_DIRS = (
#     os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'templates'),
# )

