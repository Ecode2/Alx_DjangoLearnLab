from relationship_app.models import Author, Book, Library

# Query all books by a specific author
author = Author.objects.get(name="John Doe")
books_by_author = Book.objects.filter(author=author)

# List all books in a library
library = Library.objects.get(name="Main Library")
books_in_library = Book.objects.filter(library=library)

# Retrieve the librarian for a library
librarian = library.librarian

# Print the results
print("Books by author:")
for book in books_by_author:
    print(book.title)

print("\nBooks in library:")
for book in books_in_library:
    print(book.title)

print("\nLibrarian for library:", librarian)