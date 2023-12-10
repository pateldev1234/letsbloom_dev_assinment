CREATE DATABASE IF NOT EXISTS bloom_books;
USE bloom_books;

CREATE TABLE books(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    book_name VARCHAR(100) NOT NULL,
    book_genere VARCHAR(20) NOT NULL, 
    number_of_pages INT NOT NULL,
    edition_number INT NOT NULL,
    publication_year INT NOT NULL,
    publication_month VARCHAR(20) NOT NULL,
    created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_on TIMESTAMP DEFAULT  CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

INSERT INTO books(book_name, book_genere, number_of_pages, edition_number, publication_year, publication_month) VALUES ("BIG C++", "Programming", 121, 5, 2022, 4);