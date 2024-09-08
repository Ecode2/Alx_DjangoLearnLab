from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
#from django_filters import rest_framework

from .serializers import BookSerializer
from .models import Book

# Create your views here.
class ListView(generics.ListAPIView):
    serializer_class=BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fileds = ["title", "publication_year", "author"]
    ordering_fileds = ["title", "publication_year"]
    
    def get_queryset(self):
        """ author = self.kwargs['author']
        return Book.objects.filter(author=author) """
        queryset = Book.objects.all()
        author = self.request.query_params.get('author')
        if author is not None:
            queryset = queryset.filter(author=author)
        return queryset
    
    #filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


class DetailView(generics.RetrieveAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CreateView(generics.CreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    #permission_classes = [IsAuthenticated]

class UpdateView(generics.UpdateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes = [IsAuthenticated]

class DeleteView(generics.DestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes = [IsAuthenticated]
