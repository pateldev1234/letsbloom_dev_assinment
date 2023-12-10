from setup import mysql_connector_cursor, mysql_connector

def get_all_books_details():
    sql_query = "SELECT * FROM books"
    mysql_connector_cursor.execute(sql_query) 
    books_list = mysql_connector_cursor.fetchall() 
    print(books_list)
    return books_list

def insert_books(book_details):
    try:
        sql_query = f"SELECT * FROM books WHERE id = {book_details['id']}"
        mysql_connector_cursor.execute(sql_query)
        book_list = mysql_connector_cursor.fetchall()
        if len(book_list) == 1:
            return False
        sql_query = f"INSERT INTO books(id, book_name, book_genere, number_of_pages,\
                edition_number, publication_year, publication_month) VALUES \
                ( {book_details['id']}, '{book_details['book_name']}', '{book_details['book_genere']}', \
                    {book_details['number_of_pages']}, {book_details['edition_number']},{book_details['publication_year']}, '{book_details['publication_month']}')"
        mysql_connector_cursor.execute(sql_query)
        mysql_connector.commit()
        return True
    except Exception as e:
        raise e

def update_book_details(book_id, updated_details):
    ## check if book with given book id exits or not ##
    try:
        sql_query = f"SELECT * FROM books WHERE id = {book_id}"
        mysql_connector_cursor.execute(sql_query)
        book_list = mysql_connector_cursor.fetchall()
        if len(book_list) == 0:
            return False
        ## book found perform update query ##
        where_clause = f" WHERE id = {book_id}"
        select_clause = "UPDATE books "
        update_clause_string = []
        for k in updated_details.keys():
            if updated_details[k] is not None:
                if type(updated_details[k]) == str:
                    update_clause_string.append(f"{k}='{updated_details[k]}'")
                else:
                    update_clause_string.append(f"{k}={updated_details[k]}")
        if len(update_clause_string) == 0:
            return False
        update_clase = ",".join(update_clause_string)
        update_clase = " SET " + update_clase
        sql_query = select_clause + update_clase + where_clause
        mysql_connector_cursor.execute(sql_query)
        mysql_connector.commit()
        return True
    except Exception as e:
        raise e