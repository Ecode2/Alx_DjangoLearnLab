from django.urls import path, include

from .views import ListView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path("/books/", ListView.as_view()),
    path("/books/delete/<int:pk>/", DeleteView.as_view()),
    path("/books/create/<int:pk>/", CreateView.as_view()),
    path("/books/<int:pk>/", DetailView.as_view()),
    path("/books/update/<int:pk>/", UpdateView.as_view()),
]