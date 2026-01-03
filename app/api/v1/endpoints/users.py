from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import crud_user
from app.schemas import user
from app.api import deps

router = APIRouter()

@router.get("/{user_email}", response_model=user.User)
def get_user(
  user_email: str,
  db: Session = Depends(deps.get_db)
):
  user = crud_user.get_user_by_email(db, email=user_email)

  if user is None:
    raise HTTPException(status_code=404, detail="No user with that email address exists.")
  
  return user

@router.post("/", response_model=user.User, status_code=201)
def create_user(
  user_in: user.UserCreate,
  db: Session = Depends(deps.get_db)
):
  user = crud_user.get_user_by_email(db, email=user_in.email)

  if user:
    raise HTTPException(
      status_code=400,
      detail="The user with this email already exists."
    )

  return crud_user.create_user(db=db, user=user_in)