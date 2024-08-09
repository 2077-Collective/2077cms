from .settings import *

DEBUG = True

ALLOWED_HOSTS = ['74.119.195.253', 'cms.2077.xyz']

CSRF_TRUSTED_ORIGINS = ["https://" + host for host in ALLOWED_HOSTS]

CORS_ALLOWED_ORIGINS = [
    "https://cms.2077.xyz",
]

# REDISCLOUD_URL = config("REDISCLOUD_URL")

STATIC_URL = 'staticfiles/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASS'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}

CSP_DEFAULT_SRC = ("self",)

CSP_STYLE_SRC = ("self",)

CSP_SCRIPT_SRC = ("self",)

CSP_IMG_SRC = ("self",)

CSP_FONT_SRC = ("self",)

CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 31536000

SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_HSTS_PRELOAD = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True
