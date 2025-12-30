from typing import Generator
from app.db.session import SessionLocal

# This function creates a session, yields it to the route, 
# and then ensures it is closed after the request finishes.
def get_db() -> Generator:
  db = SessionLocal()

  try:
    yield db
  finally:
    db.close()