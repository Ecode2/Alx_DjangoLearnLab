import json
from django.test import TestCase
from django.urls import include, path
from rest_framework.test import APIRequestFactory, APITestCase, URLPatternsTestCase
from rest_framework import status

from .serializers import AuthorSerializer
"from rest_framework import status"
from .models import Book,  Author

factory = APIRequestFactory()

author = Author.objects.get(name="Abubakar")

"""
self.client.login
request = factory.get("/api/books")
request = factory.post("/api/books/create", {"title": "Harry potter and the prisoner of azkaban",
                                             "publication_year": 2003, "author": author})

request= factory.get("/api/books?ordering=publication_year") """

class BookTests(APITestCase, URLPatternsTestCase):
    
    urlpatterns = [
        path('api/', include('api.urls')),
    ]

    """ def setUp(self):
        Book.objects.create(title="Harry potter and the prisoner of azkaban",
                            publication_year=2003,
                            author=author) """

    def test_book_detail(self):
        """ response=self.client.get("/api/books/2/")
        #?ordering=title
        print(response.data)
        self.assertEqual(response.data, {"title": "Harry potter and the goblet of fire",
                                        "publication_year": 2005,
                                        "author": author})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) """
        return status.HTTP_201_CREATED