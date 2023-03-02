import dj_database_url
from .settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*pl4xa)00@s-cj7pgu+ym_f7+mjp6h5-jlics0itvaik+97^mk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['medicsearch.up.railway.app']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASE_URL = 'postgresql://postgres:GMBHXHlPYp5bZUyH8sO7@containers-us-west-22.railway.app:5994/railway'

DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),
}