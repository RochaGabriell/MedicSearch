import dj_database_url
from .settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*pl4xa)00@s-cj7pgu+ym_f7+mjp6h5-jlics0itvaik+97^mk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['web-production-e30d7.up.railway.app']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASE_URL = 'postgresql://postgres:bJWH2HKQpNkvvk13OpWl@containers-us-west-188.railway.app:6758/railway'

DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),
}
