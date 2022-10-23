from fastapi import FastAPI, HTTPException
from fastapi import Request, status, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from server_utils import *
import uvicorn
import requests
from data_base.db_maneger import db_manager

app = FastAPI()
app.mount("/client", StaticFiles(directory="client"), name="client")

# Routes

@app.get('/sanity')
def sanity():
    return "OK"

# @app.get('/')
# def root():
#     return FileResponse('./client/index.html')

# @app.get("/books")
# def get_players(word):
#     books = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={word}")
#     try:
#         return parse_data(books.json())

#     except GeneralUnicException:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Invalid word"
#         )

# @app.get("/books/")
# def get_book_by_parameter(parameter):
#     if parameter == "long":
#         book_name = db_manager.get_longest_book()
#         return book_name

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000,reload=True)

