"""Development settings"""

from src.settings.base import DEVELOPER_APPS, DEVELOPER_MIDDLEWARE, env


from .common import DEFAULT_DB_CONNECTION

INTERNAL_IPS = [
    "127.0.0.1",
]
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [*DEVELOPER_APPS]

MIDDLEWARE = [*DEVELOPER_MIDDLEWARE]


DATABASES = {
    "default": env.db(DEFAULT_DB_CONNECTION),
}
