from ecomprj.settings.components.base import (
    INSTALLED_APPS,
    MIDDLEWARE,
    DEBUG,
    MEDIA_ROOT,
)
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from django.http import HttpRequest


# Installed apps for development only:

INSTALLED_APPS += ("debug_toolbar",)


EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = f"{MEDIA_ROOT}/email_out"
# TODO: Django debug toolbar:
# https://django-debug-toolbar.readthedocs.io

MIDDLEWARE += (
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # https://github.com/bradmontgomery/django-querycount
    # Prints how many queries were executed, useful for the APIs.
    # "querycount.middleware.QueryCountMiddleware",
)


def _custom_show_toolbar(request: "HttpRequest") -> bool:
    """Only show the debug toolbar to users with the superuser flag."""
    return DEBUG and request.user.is_superuser


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": "ecomprj.settings.environments.dev._custom_show_toolbar",
}
