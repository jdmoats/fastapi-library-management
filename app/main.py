import uvicorn
from fastapi import FastAPI
from app.api.v1.api import api_router

app = FastAPI(title="Library Management API")

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def get_index():
  return {"message": "Welcome to the Library Management API"}

@app.get("/about")
def get_about():
  return {"message": "This is the about endpoint"}

if __name__ == "__main__":
  uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)