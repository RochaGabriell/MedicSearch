from .settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l4gh65*3k1e-_8@eew!&ni5bp_by1og&ge6b$i8ze#(-+%%x@$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}