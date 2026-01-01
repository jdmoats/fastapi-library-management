from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

#Association table with books
user_books = Table(
  "user_books",
  Base.metadata,
  Column("user_id", ForeignKey("users.id"), primary_key=True),
  Column("book_id", ForeignKey("books.id"), primary_key=True)
)

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  email = Column(String, index=True)
  password = Column(String, unique=True, index=True)
  books = relationship("Book", secondary=user_books, back_populates="users")