"""
Django settings for ecomprj project.

"""

from typing import Tuple

from django.utils.translation import gettext_lazy as _

from ecomprj.settings.components import BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

SECRET_KEY = (
    "django-insecure-$p2q^f)6ac80#@6=xcjr6ke&(v@iie6k)vg32exs!l(%!d4x1("
)

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "0.0.0.0", "[::1]"]

# Application definition:

INSTALLED_APPS: Tuple[str, ...] = (
    # Admin Panels
    "jazzmin",

    # Standard App
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Custom Apps
    "core",
    "userauths"
)

MIDDLEWARE: Tuple[str, ...] = (
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

ROOT_URLCONF = "ecomprj.urls"


TEMPLATES = [
    {
        "APP_DIRS": True,
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            # Contains plain text templates, like `robots.txt`:
            BASE_DIR.joinpath("templates"),
        ],
        "OPTIONS": {
            "context_processors": [
                # Default template context processors:
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
        },
    }
]


WSGI_APPLICATION = "ecomprj.wsgi.application"
ASGI_APPLICATION = "ecomprj.asgi.application"


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

# LANGUAGE_CODE = "ru-ru"
LANGUAGE_CODE = "en-us"

USE_I18N = True

LANGUAGES = (
    ("en", _("English")),
    ("ru", _("Russian")),
)

LOCALE_PATHS = ("locale/",)

USE_TZ = True
TIME_ZONE = "UTC"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR.joinpath("staticfiles")

STATICFILES_DIRS = [BASE_DIR.joinpath("static")]

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR.joinpath("media")


# Templates
# https://docs.djangoproject.com/en/4.2/ref/templates/api


# Django authentication system
# https://docs.djangoproject.com/en/4.2/topics/auth/

# AUTHENTICATION_BACKENDS = (
#     "axes.backends.AxesBackend",
#     "django.contrib.auth.backends.ModelBackend",
# )

# PASSWORD_HASHERS = [
#     "django.contrib.auth.hashers.Argon2PasswordHasher",
#     "django.contrib.auth.hashers.PBKDF2PasswordHasher",
#     "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
#     "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
# ]


# Security
# https://docs.djangoproject.com/en/4.2/topics/security/

SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

# X_FRAME_OPTIONS = "DENY"

# # https://github.com/DmytroLitvinov/django-http-referrer-policy
# # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy
# REFERRER_POLICY = "same-origin"

# # https://github.com/adamchainz/django-permissions-policy#setting
# PERMISSIONS_POLICY: Dict[str, Union[str, List[str]]] = {}  # noqa: WPS234


# Timeouts
# https://docs.djangoproject.com/en/4.2/ref/settings/#std:setting-EMAIL_TIMEOUT

# EMAIL_TIMEOUT = 5


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"


JAZZMIN_SETTINGS = {
    "site_header": "Training Shop",
    "site_brand": "You order, we deliver",
    "site_logo": "assets/imgs/theme/logo.svg",
    "copyright": "training-shop.com",
}
