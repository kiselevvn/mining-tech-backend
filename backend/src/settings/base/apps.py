DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "corsheaders",
    "rest_framework",
    "django_filters",
    "djoser",
    "drf_yasg",
    "import_export",
    "puml_generator",
]

PROJECT_APPS = [
    "backend.apps.common",
    "backend.apps.users",
    "backend.apps.products",
    "backend.apps.orders",
]

DEVELOPER_APPS = [
    *DEFAULT_APPS,
    *PROJECT_APPS,
    "debug_toolbar",
]

PRODUCTION_APPS = [*DEFAULT_APPS, *PROJECT_APPS]
