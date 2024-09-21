from django.urls import path, include, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

from .views import (HomeView, PostList, SignupView, 
                    PostDetailView, ProfileView, 
                    CustomLogoutView, PostUpdateView,
                    PostCreateView, PostDeleteView,
                    CommentCreateView, CommentUpdateView,
                    CommentDeleteView)


app_name = "blog"

##/tags/<tag_name>/ and /search/.
##tags/<slug:tag_slug>/", "PostByTagListView.as_view()

urlpatterns = [
    path("login/", LoginView.as_view(template_name="blog/login.html", next_page=reverse_lazy('blog:home')), name="login"),
    path("logout/", CustomLogoutView.as_view(template_name="blog/logout.html", next_page=reverse_lazy('blog:home')), name="logout"), 
    path("register/", SignupView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("posts/", PostList.as_view(), name="posts"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post"),
    path("post/new/", PostCreateView.as_view(), name="create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="delete"),
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="new_comment"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="update_comment"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="delete_comment"),
    path("", HomeView.as_view(), name="home"),
]