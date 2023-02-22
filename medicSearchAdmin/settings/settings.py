"""
Django settings for medicSearchAdmin project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!k7pqk6vz(mvyjuxhlv&7v#ys(e6@gf*b7np0^y&sfy%855-i!'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = []

CSRF_TRUSTED_ORIGINS = ['https://medicsearch.up.railway.app']

# Application definition

INSTALLED_APPS = [
    'admin_menu',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'medicSearch.apps.MedicsearchConfig',
    'social_django'
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

ROOT_URLCONF = 'medicSearchAdmin.urls'

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

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'medicSearchAdmin.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_URL = '/login' # Define a rota padrão de login do sistema.
LOGIN_REDIRECT_URL = '/' # Define para onde seremos redirecionados caso o login ocorra com sucesso.
LOGOUT_URL = '/logout' # Define a rota padrão de logout do sistema.
LOGOUT_REDIRECT_URL = '/login' # Define para onde seremos redirecionados caso o logout ocorra com sucesso.


# Django Admin Menu Theme
ADMIN_LOGO = 'img/logo.png'

ADMIN_STYLE = {
    'background': 'black',
    'primary-color': '#164B36',
    'primary-text': '#d6d5d2',
    'secondary-color': '#092117',
    'secondary-text': 'white',
    'tertiary-color': '#51B48E',
    'tertiary-text': 'black',
    'breadcrumb-color': '#092117',
    'breadcrumb-text': '#e0e0e0',
    'focus-color': '#eaeaea',
    'focus-text': '#666',
    'primary-button': '#26904A',
    'primary-button-text':' white',
    'secondary-button': '#999',
    'secondary-button-text': 'white',
    'link-color': '#e0e0e0',
    'link-color-hover': 'lighten($link-color, 20%)',
    'logo-width': 'auto',
    'logo-height': '35px'
}

MENU_WEIGHT = {
    'Auth': 100
}


AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

SOCIAL_AUTH_FACEBOOK_KEY = '549379146987638' # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'a5f2d15d1c420c4532e65cb372da8411' # App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_link'] # Lista de permissões para acessar as propriedades de dados que nosso aplicativo requer.
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email, picture.type(large), link'
} # Possui uma chave fields em que o valor é uma lista de atributos que devem ser retornados pelo Facebook quando o usuário tiver efetuado login com êxito. Os valores dependem de SOCIAL_AUTH_FACEBOOK_SCOPE.
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [
    ('name', 'name'),
    ('email', 'email'),
    ('picture', 'picture'),
    ('link', 'profile_url'),
] # Especificar os dados adicionais que solicitamos ao banco de dados. Esses dados ficarão 'extra data' do painel 'user social auths'. 
# Pra usar qualquer atributo que está no campo extra fields em nosso template html podemos fazê-lo chamando {{ass.extra_data.nome_do_campo}}. Ex: {{ass.extra_data.picture.data.url}}.


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '45626635179-f7m389civ0qduht30npc3d1kvek281aj.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'