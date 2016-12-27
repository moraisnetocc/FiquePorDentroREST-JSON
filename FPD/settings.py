import os

import re

from dj_database_url import config as db_config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Start of ".env" reader
# https://gist.github.com/bennylope/2999704
try:
    with open(os.path.join(BASE_DIR, '.env')) as f:  # pragma: no cover
        content = f.read()
except IOError:
    content = ''

for line in content.splitlines():  # pragma: no cover
    m1 = re.match(r'\A(?P<key>[A-Za-z_0-9]+)=(?P<value>.*)\Z',
                  re.sub(r"( +)?#(.+)?", "", line))  # Allow comments on the ".env" file
    if m1:
        os.environ.setdefault(**m1.groupdict())
# End of ".env" reader

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%iazc^-xqx_h39aeaww14^y38xbaw_=fnoezep0@h@5w4yotyl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.getenv('DEBUG', '0')))

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'rest_framework',
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

ROOT_URLCONF = 'FPD.urls'

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

WSGI_APPLICATION = 'FPD.wsgi.application'

DATABASES = {
    'default': db_config()
}

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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
