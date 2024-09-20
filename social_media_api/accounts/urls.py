from django.urls import path
from rest_framework.authtoken import views as vs
from . import views

#app_name = "accounts"

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("api-token-auth/", vs.obtain_auth_token, name="api-token-auth"),
]
""" 
{
    "token": "b749ea2aef115e683b45f93dae52c71c35d074d4",
    "token_type": "Token"
} """