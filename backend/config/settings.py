from pathlib import Path
from django_settings_env import Env

# read .env for 12-factor settings
env = Env(readenv=True, parents=True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = BASE_DIR.parent
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG', type=bool, default=False)
ALLOWED_HOSTS = env('ALLOWED_HOSTS', type=list, default=['localhost'])

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'drf_generators',
    'drf_spectacular',

    'api.apps.ApiConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

CONTEXT_PROCESSORS = [
    "django.template.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
]

TEMPLATE_LOADERS = [
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.filesystem.Loader',
]
if DEBUG:
    CONTEXT_PROCESSORS.insert(0, "django.template.context_processors.debug")

if env('TEMPLATE_CACHE_ENABLED', type=bool, default=False):
    # wrap loaders in cache if enabled
    TEMPLATE_LOADERS = ('django.template.loaders.cached.Loader', TEMPLATE_LOADERS)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            PROJECT_DIR / "templates"
        ],
        "OPTIONS": {
            "context_processors": CONTEXT_PROCESSORS,
            "loaders": TEMPLATE_LOADERS,
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

DATABASES = { 'default': env.database_url() }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# DRF

REST_FRAMEWORK = {
    # use django model permissions for read/write
    # allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 25
}

SPECTACULAR_SETTINGS = {
    'TITLE': '.id Challenge API',
    'DESCRIPTION': 'Meet the challenge',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}

DOWNLOAD_PATH = BASE_DIR / 'downloads'
DOWNLOAD_URL = 'https://github.com/dotidconsulting/coding-challenge-location-decisions/blob/main/back-end/ABS_C16_T01_TS_SA_08062021164508583.xls?raw=true'
