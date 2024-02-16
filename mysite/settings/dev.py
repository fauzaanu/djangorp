from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    "*",
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-22sgmf6qdtp+uq@e@cv(y7=5bne^7-8+fj4_u8yg2tl0ln!4fk"

CSRF_TRUSTED_ORIGINS = [
    "https://example.com"
]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database.sqlite3',
    }
}

# Cache settings
# https://docs.djangoproject.com/en/5.0/topics/cache/#setting-up-the-cache
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

# local.py - local development settings Without modifying the base.py file, you can create a local.py file in the
# same directory as settings.py and add the following code:
try:
    from .local import *
except ImportError:
    pass
