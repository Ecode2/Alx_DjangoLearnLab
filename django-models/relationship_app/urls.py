from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import list_books

urlpatterns = [
    path('function-based-view/', views.book_list, name='function_based_view'),
    path('library-list/', views.LibraryBookListView.as_view(), name='class_based_view'),
    path('library/', views.LibraryDetailView.as_view(), name='class_based_view'),
    path('new-user/', views.UserRegistrationView.as_view(), name='class_based_view'),
    # Add the following URL patterns for authentication views
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),
    path('admin/', views.AdminView.as_view(), name='admin'),
    path('librarian/', views.LibrarianView.as_view(), name='librarian'),
    path('member/', views.MemberView.as_view(), name='member'),
    "add_book/", "edit_book/", "delete_book"
]


""" path('register/', SignUpView.as_view(), name='register'), """
"views.register", "LogoutView.as_view(template_name="