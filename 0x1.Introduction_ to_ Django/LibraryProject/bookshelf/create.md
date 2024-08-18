from bookshelf.models import Book
books = Book.objects.all()

Book.objects.create(title="1984",
     author="George Orwell",
     publication_year=1949)

new_book.save()
