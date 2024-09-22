from django.urls import path
from rest_framework.authtoken import views as vs
from . import views

#app_name = "accounts"

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("api-token-auth/", vs.obtain_auth_token, name="api-token-auth"),
    path("follow/<int:user_id>/", views.FollowUserView.as_view(), name="follow_user"),
    path("unfollow/<int:user_id>/", views.FollowUserView.as_view(), name="follow_user"),
]