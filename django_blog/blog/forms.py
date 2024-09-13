from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]