from faker import Faker
from app.db.session import SessionLocal
from app.models.book import Book
import random

# Initialize Faker
fake = Faker()

def seed_books():
    db = SessionLocal()
    
    print("Generating 1,000 books...")
    
    # 1. Create a list of objects in memory (fast)
    books_to_create = []
    for _ in range(1000):
        new_book = Book(
            title=fake.catch_phrase(),     # Random catchy title
            author=fake.name(),            # Random name
            year=random.randint(1900, 2024) # Random year
        )
        books_to_create.append(new_book)
    
    # 2. Add all objects to the session
    db.add_all(books_to_create)
    
    # 3. Commit only ONE time (super fast)
    db.commit()
    
    print("Success! Added 1,000 books to the database.")
    db.close()

if __name__ == "__main__":
    seed_books()