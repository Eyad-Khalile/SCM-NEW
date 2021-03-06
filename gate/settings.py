"""
Django settings for gate project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

print('here is base_dir',BASE_DIR)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yucmz538)r(j89-97e-*^19n!kql%wrd!7nuw@*dpe7y0*qw+f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'widget_tweaks',
    'crispy_forms',
    'six',
    'django_admin_listfilter_dropdown',
    'rangefilter',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gate.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'gate.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


DATABASES = {
     'default': {
         'ENGINE': 'sql_server.pyodbc',
         'NAME': 'kh-test3',
         'USER': 'khalil',
         'PASSWORD': '5617944kK',
         'HOST': 'kh-ttest3.database.windows.net',
         'PORT': '1433 ',
         'OPTIONS': {
             'driver': 'ODBC Driver 17 for SQL Server',
             'MARS_Connection': 'True',
         }
     }
 }

# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ar'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

LANGUAGES = [
    ('ar', 'عربي'),
    ('en', 'English'),
]


###################registrion account###############
LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
###################################################

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


# STATIC_ROOT = (os.path.join(BASE_DIR, 'static'))
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/')
]
#directoy for data map
DATA_URL = '/data/'
Data_ROOT = (os.path.join(BASE_DIR, 'data'))
print('here is ',Data_ROOT)

MEDIA_ROOT = (os.path.join(BASE_DIR, 'media'))
MEDIA_URL = '/media/'


# ======== Email
# DEFAULT_FROM_EMAIL = ''
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'khalile.eyad@gmail.com'
EMAIL_HOST_PASSWORD = 'Eyad1979@'


# YAHOO 
# EMAIL_HOST = 'smtp.mail.yahoo.fr'
# EMAIL_PORT = 25
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'eyad.basha79@yahoo.com'

# DEFAULT_FROM_EMAIL = 'email@yahoo.com'
# DEFAULT_TO_EMAIL = 'email@yahoo.com'


# Celery settings
# //Specify which broker you will use, we are using django's broker for development
# BROKER_URL = 'django://'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'
# CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
# djcelery.setup_loader()









