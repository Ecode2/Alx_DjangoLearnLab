from django.shortcuts import render
from rest_framework import generics, permissions, pagination, response, status

from notifications.models import Notification
from .models import Post, Comment, Like
from accounts.permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer, PostSerializer, LikeSerializer

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
    permission_classes=[permissions.IsAuthenticated, IsAuthorOrReadOnly]

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    ordering_fields = ['-created_at']
    pagination_class=pagination.PageNumberPagination

    def get_queryset(self):
        pk=self.kwargs['post_pk']
        return Comment.objects.filter(post_id=pk)
    

    def post(self, request, *args, **kwargs):

        post = generics.get_object_or_404(Post, pk=self.kwargs['post_pk'])
        author = request.user
        content = request.data['content']

        comment = Comment.objects.create(post=post, author=author, content=content)
        serializer = CommentSerializer(comment, data=request.data)

        notification = Notification.objects.create(recipient=post.author, actor=author, verb=f"{author.username} commented on your post")
        notification.save()

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)              
        
    """ def perform_create(self, serializer):
        serializer.save(author=self.request.user) """
    
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes=[permissions.IsAuthenticated, IsAuthorOrReadOnly]

class FeedView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class=pagination.PageNumberPagination

    def get_queryset(self):
        #Post.objects.filter(author__in=following_users).order_by", "following.all()", "permissions.IsAuthenticated
        return Post.objects.filter(author__followers__in=[self.request.user]).order_by('-created_at')
    
class LikeView(generics.ListCreateAPIView):
    serializer_class = LikeSerializer
    pagination_class=pagination.PageNumberPagination

    def get_queryset(self):
        return Like.objects.filter(post_id=self.kwargs['pk'])

    def post(self, request, *args, **kwargs):
        pk=self.kwargs['pk']
        post = generics.get_object_or_404(Post, pk=pk)
        user = request.user

        like = Like.objects.get_or_create(post=post, user=user)
        serializer = LikeSerializer(like, data=request.data)

        if serializer.is_valid():
            serializer.save()

            notification = Notification.objects.create(recipient=post.author, actor=user, verb=f"{user.username} liked your post")
            notification.save()

            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
class UnLikeView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def delete(self, request, *args, **kwargs):
        
        pk=self.kwargs['pk']
        post = generics.get_object_or_404(Post, pk=pk)
        user = request.user

        try:
            like = Like.objects.get(post=post, user=user)
            #like = Like.objects.delete(post=post, user=user)
            if like:
                like.delete()
                return response.Response({"status": True, "msg": "Post Unliked"}, status=status.HTTP_200_OK)
        except Exception as e:
            return response.Response({"status": False, "msg": "Post not found"}, status=status.HTTP_400_BAD_REQUEST) 