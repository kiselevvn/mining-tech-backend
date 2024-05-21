"""Logging settings"""

from .paths import LOG_FILE

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "request": {
            "format": (
                "{levelname} {asctime} {status_code} {request} ",
                "{module} {process:d} {thread:d} {message}",
            ),
            "style": "{",
        },
    },
    "handlers": {
        "file-request": {
            "class": "logging.FileHandler",
            "filename": LOG_FILE,
            "formatter": "request",
        }
    },
    "loggers": {
        "django.request": {"handlers": ["file-request"], "propagate": True,}
    },
}

LOGGING = {
    "version": 1,
    "filters": {
        "require_debug_true": {"()": "django.utils.log.RequireDebugTrue",}
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
        }
    },
    "loggers": {
        "django.db.backends": {"level": "DEBUG", "handlers": ["console"],}
    },
}
