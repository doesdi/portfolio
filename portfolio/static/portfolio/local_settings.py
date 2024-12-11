import os
from django.template.defaultfilters import join
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-wfzugaxk#hxy#7is9c+)r=1gfoe80i5o$bs=hk+75l_fb$=g&y"

DEBUG = True

ALLOWED_HOSTS = ['localhost',  'wpad.beeline', 'wpad']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'django'),
        'USER': os.getenv('POSTGRES_USER', 'husokka'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'Hbcrfec2017!'),
        'HOST': os.getenv('DATABASE_HOST', 'db'),  # имя сервиса из docker-compose.yml
        'PORT': os.getenv('DATABASE_PORT', '5432'),
    }
}

STATIC_URL = '/static/'
STATIC_DIR = join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

