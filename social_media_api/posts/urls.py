from django.urls import path, re_path
from . import views

#app_name = 'posts'

urlpatterns = [
    path("posts/", views.PostListCreateView.as_view(), name="post-list-create"),
    path("posts/feed/", views.FeedView.as_view(), name="feed"),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:post_pk>/comments/", views.CommentListCreateView.as_view(), name="comment-list-create"),
    path("posts/<int:post_pk>/comments/<int:pk>/", views.CommentDetailView.as_view(), name="comment-detail"),
    path("posts/<int:pk>/like/", views.LikeView.as_view(), name="like_post"),
    path("posts/<int:pk>/unlike/", views.UnLikeView.as_view(), name="unlike_post"),
]