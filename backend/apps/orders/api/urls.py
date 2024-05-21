from django.urls import include, path

from .v1 import views

urlpatterns = [
    path("list/", views.OrderListAPIView.as_view(), name="order-list"),
    path("create/", views.OrderCreateAPIView.as_view(), name="order-create"),

]
