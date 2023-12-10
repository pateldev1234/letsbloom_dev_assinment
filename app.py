from fastapi import FastAPI
from models.model import Book, BookEditModel
from services.services import get_all_books_details, update_book_details, insert_books

app = FastAPI()

@app.get('/api/books')
def get_all_books():
    book_details = get_all_books_details()
    res = {
        'data': book_details,
        'message': "Successfull",
        'status_code': 200
    }
    return res

@app.post('/api/books')
def add_book(book_details : Book):
    try: 
        book_details = book_details.dict()
        res = insert_books(book_details)
        if not res:
            return {
            'data': [],
            'message': "Books with same ID alredy exists",
            'status_code': 200
        }
        return {
            'data': [],
            'message': "Successfull",
            'status_code': 200
        }
    except Exception as e:
        return {
            'data': [e],
            'message': "Error",
            'status_code': 400
        }

@app.put('/api/books/{id}')
def update_book(id : int,  item: BookEditModel):
    try:
        item = item.dict()
        res = update_book_details(id, item)
        if not res: 
            return {
                'data': [],
                'message': "Book Id not found",
                'status_code': 400
            }
        return {
            'data': [],
            'message': "Successfull",
            'status_code': 200
        }
    except Exception as e:
        return {
            'data': [e],
            'message': "Error",
            'status_code': 400
        }