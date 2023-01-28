from .settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7uf^xnbqu9v!nyb5-f!-huy@dv5zw&%a+8052v1t+%-+qp#eem'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}