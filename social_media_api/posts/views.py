from django.shortcuts import render
from rest_framework import generics, permissions, pagination, response, status

from .models import Post, Comment
from accounts.permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer, PostSerializer

# Create your views here.
##viewsets.ModelViewSet
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
    permission_classes=[IsAuthorOrReadOnly]

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    ordering_fields = ['-created_at']
    pagination_class=pagination.PageNumberPagination

    def post(self, request, *args, **kwargs):
        post = Post.objects.get(pk=self.kwargs['post_pk'])
        author = request.user
        content = request.data['content']

        comment = Comment.objects.create(post=post, author=author, content=content)
        serializer = CommentSerializer(comment, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)              
        
    """ def perform_create(self, serializer):
        serializer.save(author=self.request.user) """
    
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes=[IsAuthorOrReadOnly]

class FeedView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class=pagination.PageNumberPagination

    def get_queryset(self):
        #Post.objects.filter(author__in=following_users).order_by", "following.all()", "permissions.IsAuthenticated
        return Post.objects.filter(author__followers__in=[self.request.user]).order_by('-created_at')
