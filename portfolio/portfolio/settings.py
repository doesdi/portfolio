import os
from django.template.defaultfilters import join
from pathlib import Path
import environ




BASE_DIR = Path(__file__).resolve().parent.parent


env = environ.Env()
environ.Env.read_env(env_file=os.path.join(BASE_DIR, '.env'))


SECRET_KEY = env("SECRET_KEY")


DEBUG = env("DEBUG")

ALLOWED_HOSTS = ['127.0.0.1','localhost',  'wpad.beeline', 'wpad']




INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'captcha',
    'main.apps.MainConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

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

WSGI_APPLICATION = 'portfolio.wsgi.application'


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


LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



STATIC_URL = '/static/'
STATIC_DIR = join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR, STATIC_URL)



MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

INTERNAL_IPS = [
    '127.0.0.1',
]



CACHES = {
         'default': {
             'BACKEND': 'django_redis.cache.RedisCache',
             'LOCATION': 'redis://redis:6379/1',
             'OPTIONS': {
                 'CLIENT_CLASS': 'django_redis.client.DefaultClient',
             }
         }
     }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': env("DB_HOST"),
        'PORT': env("DB_PORT"),
    }
}




