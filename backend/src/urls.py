from django.conf import settings
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    url(r"^auth/", include("djoser.urls")),
    url(r"^auth/", include("djoser.urls.jwt")),
    url(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    url(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    url(
        r"^redoc/$",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path("admin/", admin.site.urls),
    url(
        "api/v1/",
        include(
            [
                path(
                    "users/",
                    include("apps.users.api.urls"),
                ),
                path(
                    "products/",
                    include("apps.products.api.urls"),
                ),
                path(
                    "orders/",
                    include("apps.orders.api.urls"),
                ),
            ]
        ),
    ),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]

urlpatterns = i18n_patterns(
    *urlpatterns,
    prefix_default_language=False,
)


if settings.DEBUG:
    import debug_toolbar
    # pylint: disable=ungrouped-imports
    from django.conf.urls.static import static

    urlpatterns = (
        [
            path("__debug__/", include(debug_toolbar.urls)),
        ]
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        + urlpatterns
    )
