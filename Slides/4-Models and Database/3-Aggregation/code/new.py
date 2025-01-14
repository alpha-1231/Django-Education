# https://pypi.org/project/Faker/
# -------------------------------------------------------------
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'example.settings')
django.setup()
# -------------------------------------------------------------



from faker import Faker
import random
# print("INSTALLED_APPS:", django.conf.settings.INSTALLED_APPS)
from app.models import *

fake = Faker()
def create_dummy_data(num_records):
    """
    Creates dummy data for the given models: Author, Publisher, Book, Store.
    """
    authors = []
    publishers = []
    books = []
    stores = []

    # Create Authors
    for _ in range(num_records):
        author = Author(
            name=fake.name(),
            age=random.randint(25, 70)
        )
        authors.append(author)

    Author.objects.bulk_create(authors)  # Bulk create authors to avoid multiple save calls

    # Create Publishers
    for _ in range(num_records):
        publisher = Publisher(
            name=fake.company()
        )
        publishers.append(publisher)

    Publisher.objects.bulk_create(publishers)  # Bulk create publishers

    # Create Books
    for _ in range(num_records):
        book = Book(
            name=fake.sentence(nb_words=6)[:-1],  # Remove the period at the end
            pages=random.randint(100, 500),
            price=round(random.uniform(10.0, 50.0), 2),
            rating=round(random.uniform(3.0, 5.0), 1),
            publisher=random.choice(publishers),
            pubdate=fake.date_between(start_date='-10y', end_date='today')
        )
        books.append(book)

    Book.objects.bulk_create(books)  # Bulk create books

    # Assign authors to books (ManyToMany field)
    for book in books:
        book.authors.set(random.sample(authors, random.randint(1, 3)))  # Assign 1-3 random authors

    # Create Stores
    for _ in range(num_records):
        store = Store(
            name=fake.company()
        )
        stores.append(store)

    Store.objects.bulk_create(stores)  # Bulk create stores

    # Assign books to stores (ManyToMany field)
    for store in stores:
        store.books.set(random.sample(books, random.randint(1, 5)))  # Assign 1-5 random books

    return authors, publishers, books, stores

# Generate 50 dummy records
authors, publishers, books, stores = create_dummy_data(50)