from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
  email: EmailStr

# Properties to receive via API on creation
class UserCreate(UserBase):
  password: str

#Properties to return via API response
class User(UserBase):
  id: int

  class Config:
    from_attributes = True