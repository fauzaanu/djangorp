from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    "https://example.com/",
    "*",
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

CSRF_TRUSTED_ORIGINS = [
    "https://example.com/",
]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ["PGDATABASE"],
        'USER': os.environ["PGUSER"],
        'PASSWORD': os.environ["PGPASSWORD"],
        'HOST': os.environ["PGHOST"],
        'PORT': os.environ["PGPORT"],
    }
}

# Cache settings
# https://docs.djangoproject.com/en/5.0/topics/cache/#setting-up-the-cache
# These are the default values for Railway's Redis cache
# REDIS_PRIVATE_URL=redis://default:${{REDIS_PASSWORD}}@${{RAILWAY_PRIVATE_DOMAIN}}:6379
# REDIS_URL=redis://default:${{REDIS_PASSWORD}}@${{RAILWAY_TCP_PROXY_DOMAIN}}:${{RAILWAY_TCP_PROXY_PORT}}

REDIS_URL = os.environ["REDIS_PRIVATE_URL"]
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": [
            REDIS_URL,  # primary
            # "redis://127.0.0.1:6378",  # read-replica 1
            # "redis://127.0.0.1:6377",  # read-replica 2
        ],
    }
}

# huey - as it is more lightweight than celery
# To create huey tasks just create a tasks.py file in the app same as celery
# common decorators are @huey.task() and @huey.periodic_task(crontab(minute=0, hour=0))
from huey import RedisHuey
from redis import ConnectionPool

pool = ConnectionPool()
HUEY = RedisHuey(SITE_NAME, connection_pool=pool.from_url(REDIS_URL))
