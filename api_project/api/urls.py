from django.urls import path, include
from .views import BookList, BookViewSet, ObtainTokenView

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r"book", BookViewSet, basename="book")

urlpatterns = [
    path("list/", BookList.as_view()),
    path("", include(router.urls)),
    path("token/", ObtainTokenView.as_view())
]