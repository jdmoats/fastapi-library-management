from sqlalchemy.orm import Session
from app.models.book import Book
from app.schemas.book import BookCreate

def get_book(db: Session, book_id: int):
  return db.query(Book).filter(Book.id == book_id).first()

def get_books(db: Session, skip: int = 0, limit: int = 100, author: str | None = None):
  query = db.query(Book)

  if author:
   query = query.filter(Book.author.ilike(f"%{author}%"))

  return query.order_by(Book.year).offset(skip).limit(limit).all()

def create_book(db: Session, book: BookCreate):
  db_book = Book(**book.model_dump())
  db.add(db_book)
  db.commit()
  db.refresh(db_book)
  return db_book