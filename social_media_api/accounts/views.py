from django.shortcuts import render, get_object_or_404
from rest_framework import generics, permissions, response, status
from django.contrib.auth import login, authenticate, logout
from rest_framework.authtoken.models import Token

from .permissions import IsAuthorOrReadOnly
from .models import CustomUser
from .serializers import UserProfileSerializer, UserSerializer, FollowSerializer

#permissions.IsAuthenticated", "return Response

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, username=username, email=email, password=password)
        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return response.Response({"token": token.key, 
                                      "token_type": "Token"})
        else:
            return response.Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        
class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user
    
class FollowUserView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def update(self, request, *args, **kwargs):
        user_to_follow = get_object_or_404(CustomUser, id=self.kwargs['user_id'])
        request.user.followers.add(user_to_follow)

        return response.Response({"message":"User followed successfully"}, 
                                 status=status.HTTP_200_OK)

class UnFollowUserView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def update(self, request, *args, **kwargs):
        user_to_unfollow = get_object_or_404(CustomUser, id=self.kwargs['user_id'])
        request.user.followers.remove(user_to_unfollow)
        
        return response.Response({"message":"User unfollowed successfully"}, 
                                 status=status.HTTP_200_OK)
