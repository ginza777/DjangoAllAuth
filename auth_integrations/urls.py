from django.urls import path
from . import views
urlpatterns = [
    path("GoogleLogin", views.GoogleLogin.as_view(), name="GoogleLogin"),
    path("AppleLogin", views.AppleLogin.as_view(), name="AppleLogin"),
]
