from django.urls import include, path

from .v1 import views

urlpatterns = [
    path("create/", views.UserCreateAPIView.as_view()),
    path("detail/", views.UserRetrieveUpdateAPIView.as_view()),
]
