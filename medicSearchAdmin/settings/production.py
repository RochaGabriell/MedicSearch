from .settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*pl4xa)00@s-cj7pgu+ym_f7+mjp6h5-jlics0itvaik+97^mk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}