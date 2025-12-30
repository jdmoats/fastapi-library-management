from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import crud_book
from app.schemas import book
from app import crud, schemas
from app.api import deps

router = APIRouter()

@router.get("/{book_id}", response_model=book.Book)
def read_book(
  book_id: int,
  db: Session = Depends(deps.get_db)
):
  """Get a specific book by id"""
  book = crud_book.get_book(db, book_id=book_id)

  if book is None:
    raise HTTPException(status_code=404, detail="Book not found")
  
  return book

@router.post("/", response_model=book.Book, status_code=201)
def create_book(
  book_in: book.BookCreate,
  db: Session = Depends(deps.get_db)
):
  """Create a new book"""
  return crud_book.create_book(db=db, book=book_in)