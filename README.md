# Techstack used 
i have used fastapi, a framework in python programming lanuage for creating API.
For databsae i have used mysql. Here is details for setup and run my application.

# Sample database creation
There is a sql file named databse_init.sql import that in your mysql server using commaind
```sh
mysql -u root -p < database_init.sql
```
# MYSQL server configuration
Add mysql server details in config.py, for example
```python
DB_HOST = "localhost"
DB_USERNAME = "root"
DB_PASSWORD = "Patel@123"
DB_DATABASE_NAME = "bloom_books"
```
# Install required dependencies 
Install required dependices
```sh
pip install -r requirements.txt
```

# Documentation
Here is required documentation for each api.
## GET : /api/books
It is a simple get requirest do not take any input as argument. 
### Response
    ```json
    
    {
        "data": [
            [
                1,
                "BIG C++",
                "Programming",
                121,
                5,
                2022,
                "January",
                "2023-12-10T14:33:42",
                "2023-12-10T14:33:42"
            ],
            [
                11,
                "check",
                "programming",
                121,
                1,
                23,
                "January",
                "2023-12-10T14:40:17",
                "2023-12-10T14:40:17"
            ]
        ],
        "message": "Successfull",
        "status_code": 200
    }

    ```

## POST : /api/books
Api used for adding book deatils on server.
In request body it takes details for book.
### Request
```json
{
    "id": 11,
    "book_name": "check",
    "book_genere": "programming",
    "number_of_pages": 121,
    "edition_number": 1,
    "publication_year": 23,
    "publication_month": "January"
}
```

### Reponse
```json
{
    "data": [],
    "message": "Successfull",
    "status_code": 200
}
```

### PUT  : /api/books/{id}
Used for updating the targetd book_id.

### Request 
Here put the details you want to update with regard to targeted book.
```json
{
    "book_name": "python",
    "book_genere": "programming",
    "number_of_pages": 121,
    "edition_number": 1,
    "publication_year": 23,
    "publication_month": "January"
}
```

### Response
```json
{
    "data": [],
    "message": "Successfull",
    "status_code": 200
}
```