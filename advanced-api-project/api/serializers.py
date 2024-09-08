from datetime import datetime
from rest_framework import serializers
from .models import Book, Author

## serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    #author = serializers.ReadOnlyField(source="author.name")

    class Meta:
        model=Book
        #fields="__all__"
        fields=["title", "publication_year", "author"]

    def validate(self, data:Book):
        if data.publication_year > datetime.now().year():
            raise serializers.ValidationError("Year can not exceed current year")
        return data


## Serializer for the Author model that includes a refrence to the book serializer
class AuthorSerializer(serializers.ModelSerializer):
    books= BookSerializer(many=True, read_only=True)
    
    class Meta:
        model=Author
        fields=["name", "books"]