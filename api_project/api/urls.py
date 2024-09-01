from django.urls import path, include
from .views import BookList, BookViewSet

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r"book", BookViewSet, basename="book")

urlpatterns = [
    path("list/", BookList.as_view()),
    path("", include(router.urls))
]