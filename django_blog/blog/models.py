from django.db import models
from django.contrib.auth.models import User #, AbstractUser

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', related_name='posts')

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name