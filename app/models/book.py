from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.session import Base
from app.models.user import user_books

class Book(Base):
  __tablename__ = "books"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, index=True)
  author = Column(String)
  year = Column(Integer)
  users = relationship("User", secondary=user_books, back_populates="books")