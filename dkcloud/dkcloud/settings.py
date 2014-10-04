"""
Django settings for dkcloud project.
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Secrets file
from . import secrets

# Default Settings
from django.conf import global_settings

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = secrets.DEBUG

#TEMPLATE_DEBUG = True
TEMPLATE_DEBUG = secrets.TEMPLATE_DEBUG


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'treebeard',
    'treenav',
    'main',
    'contact',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dkcloud.urls'

WSGI_APPLICATION = 'dkcloud.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': secrets.DATABASE_NAME,
        'USER': secrets.DATABASE_USER,
        'PASSWORD': secrets.DATABASE_PASSWORD,
        'HOST': secrets.DATABASE_HOST,
        'PORT': secrets.DATABASE_PORT,
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/static/'

# Email Settings
EMAIL_USE_TLS = True
EMAIL_HOST_USER = secrets.MAIL_USER
EMAIL_HOST_PASSWORD = secrets.MAIL_PASSWORD

# Allowed Hosts
ALLOWED_HOSTS = ['.dk-cloud.net',
                 '.dk-cloud.net.', ]

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')] + secrets.ADDITIONAL_TEMPLATE_DIRS

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)

# Login Settings
LOGIN_REDIRECT_URL = '/'