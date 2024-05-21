from django.urls import include, path

from .v1 import views

urlpatterns = [
    path("product/", views.ProductListAPIView.as_view(), name="product"),
    path("product-reference/", views.ProductReferenceListAPIView.as_view(), name="product-reference"),
]
