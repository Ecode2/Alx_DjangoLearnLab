from django.shortcuts import render
from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test

def Admin(request):
    user UserProfile.objects.all()

# Create your views here.
def books(request):
    
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    all_books=Library.objects.all()
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

class LibraryBookListView(ListView):
    model = Book
    template_name = 'relationship_app/library_book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        library_id = self.kwargs['library_id']
        return Book.objects.filter(library_id=library_id)
    
class UserRegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/registration.html'
    success_url = '/'

class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'
    success_url = '/'

class UserLogoutView(LogoutView):
    next_page = '/'



@user_passes_test(lambda u: u.is_superuser)
def admin_view(request):
    # Code for admin view
    pass

@user_passes_test(lambda u: u.groups.filter(name='Librarians').exists())
def librarian_view(request):
    # Code for librarian view
    pass

@user_passes_test(lambda u: u.groups.filter(name='Members').exists())
def member_view(request):
    # Code for member view
    pass