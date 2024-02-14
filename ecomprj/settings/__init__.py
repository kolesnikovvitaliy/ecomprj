from split_settings.tools import optional, include
from os import environ

_ENV = environ.get('DJANGO_ENV') or "dev"

_base_settings = (
    "components/base.py",
    # "components/logging.py",
    "components/caches.py",
    "components/database.py",
    # Select the right env:
    "environments/{0}.py".format(_ENV),
    # Optionally override some settings:
    optional("environments/local.py"),
)
# Include settings:
include(*_base_settings)
