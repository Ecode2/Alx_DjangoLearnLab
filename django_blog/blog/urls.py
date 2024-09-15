from django.urls import path, include, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

from .views import (HomeView, PostList, SignupView, 
                    PostDetailView, ProfileView, 
                    CustomLogoutView, PostUpdateView,
                    PostCreateView, PostDeleteView)


app_name = "blog"

urlpatterns = [
    path("login/", LoginView.as_view(template_name="blog/login.html", next_page=reverse_lazy('blog:home')), name="login"),
    path("logout/", CustomLogoutView.as_view(template_name="blog/logout.html", next_page=reverse_lazy('blog:home')), name="logout"), 
    path("register/", SignupView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("posts/", PostList.as_view(), name="posts"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post"),
    path("posts/new/", PostCreateView.as_view(), name="create"),
    path("posts/<int:pk>/update/", PostUpdateView.as_view(), name="update"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="delete"),
    path("", HomeView.as_view(), name="home"),
]