from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout

from .forms import PostForm, UserUpdateForm
from .models import Post, Comment

# Create your views here.
class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('blog:login')
    template_name = "blog/register.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form": self.form_class})

class CustomLogoutView(LogoutView):
    next_page=reverse_lazy("blog:home")

    def get(self, request: HttpRequest, *arg, **kwargs):
        logout(request)
        return redirect("blog:home")

class ProfileView(LoginRequiredMixin, UpdateView, DetailView):
    model= User
    form_class= UserUpdateForm
    template_name="blog/profile.html"
    success_url = reverse_lazy("blog:profile")

    "POST", "save()"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["form"]=self.get_form()
        return context
    
    def get_object(self):
        return self.request.user
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    

class HomeView(TemplateView):
    template_name = "blog/home.html"


class PostList(ListView):
    #model = Post
    context_object_name = 'posts'
    template_name='blog/posts.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(
                title__icontains=query,
                content__icontains=query,
                tags__name__icontains=query
            ).distinct()
        else:
            return Post.objects.none()

    """ def get_context_data(self, **kwargs):
            # Call the base implementation first to get a context
            context = super().get_context_data(**kwargs)
            # Add in a QuerySet of all the books
            context["book_list"] = Book.objects.all()
            return context """  

#@login_required

class PostCreateView(CreateView, LoginRequiredMixin):
    model=Post
    form_class=PostForm
    template_name="blog/create.html"
    login_url=reverse_lazy("blog:login")
    success_url=reverse_lazy("blog:posts")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
class PostDetailView(DetailView):
    model=Post
    context_object_name="post"
    template_name="blog/post.html"

class PostUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
        model = Post
        template_name = "blog/update.html"

class PostDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    template_name = "blog/delete.html"


class CommentCreateView(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    template_name = "blog/comment_create.html"

class CommentDetailView(DetailView,  LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    template_name = "blog/comment_detail.html"


class CommentUpdateView(UpdateView,  LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    template_name = "blog/comment_update.html"


class CommentDeleteView(DeleteView,  LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    template_name = "blog/comment_delete.html"
