from django.test import TestCase
from rest_framework.test import APIRequestFactory, APITestCase

factory = APIRequestFactory()
request = factory.get("/api/books")
request = factory.post("/api/books/create", {"title": "Harry potter and the chamber of secret",
                                             "publication_year": 2001, "author": 1}, format="json")