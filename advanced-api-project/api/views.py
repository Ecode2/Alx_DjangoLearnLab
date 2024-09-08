from django.shortcuts import render
from rest_framework import generics, permissions

from .serializers import BookSerializer
from .models import Book

# Create your views here.
class ListView(generics.ListAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DetailView(generics.RetrieveAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CreateView(generics.CreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class UpdateView(generics.UpdateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class DeleteView(generics.DestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes = [permissions.IsAuthenticated]