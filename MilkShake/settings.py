#!/usr/bin/python
# -*- coding: utf-8 -*-

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from django.utils.translation import gettext_lazy


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+eq@9^2&z%-e%t6vowlj@rhx#x7mg%$46w$k1km=l1@qfq_gk@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Url de login de l'application
LOGIN_URL = "/login"


# Application definition

INSTALLED_APPS = (
    # Framework Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd Party Apps
    'compressor',

    # Application
    'MilkShake',
    'Core',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
)

ROOT_URLCONF = 'MilkShake.urls'

WSGI_APPLICATION = 'MilkShake.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# <Configuration de la langue>

# Activation de la traduction
USE_I18N = True

# Activation de la locale
USE_L10N = True

# Langue de l'application
LANGUAGE_CODE = 'en-GB'

# Timezone de l'application
TIME_ZONE = 'Europe/Paris'

# Langues disponibles pour l'application
LANGUAGES = (
    ('en', gettext_lazy('English')),
    ('fr', gettext_lazy('French')),
    ('pt', gettext_lazy('Portuguese')),
)

# Dossiers des traductions
LOCALE_PATH = (
    os.path.join(BASE_DIR, "Core/locale"),
    os.path.join(BASE_DIR, "MilkShake/locale"),
)

# ///////////////////////////////////////////


# <Configuration des fichiers statiques>

# Url des fichiers statiques
STATIC_URL = '/static/'

# Répertoires des fichiers statiques
# @see https://redbooth.com/a/#!/projects/1184903/notes/1127038
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "MilkShake/static"),
    os.path.join(BASE_DIR, "Core/static"),
    STATIC_URL,
)

STATICFILES_FINDERS = (
    'compressor.finders.CompressorFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# ///////////////////////////////////////////


# <Configuration de Compress>

# Activation de Compress
COMPRESS_ENABLED = True

# Dossier  où seront stockés les fichiers compressés
COMPRESS_ROOT = os.path.join(BASE_DIR, "MilkShake/static")
# Pré-compilateurs

COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)
# ///////////////////////////////////////////