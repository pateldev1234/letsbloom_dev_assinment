from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    id:                 int
    book_name:          str
    book_genere:        str
    number_of_pages:    int
    edition_number:     int
    publication_year:   int
    publication_month:  str


class BookEditModel(BaseModel):
    id:                 Optional[int]
    book_name:          Optional[str]
    book_genere:        Optional[str]
    number_of_pages:    Optional[int]
    edition_number:     Optional[int]
    publication_year:   Optional[int]
    publication_month:  Optional[str]


