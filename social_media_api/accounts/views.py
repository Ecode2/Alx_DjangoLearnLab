from django.shortcuts import render
from rest_framework import generics, permissions, response, status
from django.contrib.auth import login, authenticate, logout
from rest_framework.authtoken.models import Token


from .models import CustomUser
from .serializers import UserSerializer


# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    
    ##CustomUser.objects.create_user(username='admin', password='admin')
    ##get_user_model().objects.create_user

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
            token, created = Token.objects.create(user=user)
            return response.Response({"token": token.key, 
                                      "token_type": "Token"})
        else:
            return response.Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        
class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user