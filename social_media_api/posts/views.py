from django.shortcuts import render
from rest_framework import generics, permissions, pagination

from .models import Post, Comment
from .serializers import CommentSerializer, PostSerializer

# Create your views here.
class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_fields = {"title": ['icontains', 'iexact'], 
                        "content": ['icontains', 'iexact'], 
                        'author__username':['icontains', 'iexact'], 
                        "created_at":['iexact', 'gte', 'lte']}
    search_fields = ['title', 'content', 'author__username']
    ordering_fields = ['title', 'created_at']
    ordering = ['title']
    pagination_class=pagination.PageNumberPagination


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
