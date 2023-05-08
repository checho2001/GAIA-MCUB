from pathlib import Path
import os
import django


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-z^%r=a+r%r)c)xx9-$l6t3+f8ht@78#ywsu7a1pwivgdh*f@4g"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "52.4.94.183", "127.0.0.1"]
# Application definition
AUTH_USER_MODEL = "users.User"
CAPTCHA_IMAGE_SIZE = (200, 50)
CAPTCHA_FONT_SIZE = 50

INSTALLED_APPS = [
    "users",
    "captcha",
    #'qr_code',
    "GAIA_UEB",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

ROOT_URLCONF = "GAIA_UEB.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
AUTH_USER_MODEL = "users.User"


STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": "usuarios",
        "ENFORCE_SCHEMA": False,
        "CLIENT": {
            "host": "mongodb+srv://saortizc:lina040220@cluster0.x58wvtr.mongodb.net/?retryWrites=true&w=majority"
        },
    }
}
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""
WSGI_APPLICATION = "GAIA_UEB.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "es-es"

TIME_ZONE = "America/Bogota"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


# Default primarsy key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
MEDIA_URL = "/media/"

# MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'media')
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "soportemcub@gmail.com"
EMAIL_HOST_PASSWORD = "SupportMCUB1234"
DEFAULT_FROM_EMAIL = "soportemcub@gmail.com"
