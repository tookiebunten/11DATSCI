CREATE TABLE movies (
    id integer PRIMARY KEY,
    cinema_id integer NOT NULL,
    title text NOT NULL,
    FOREIGN KEY (cinema_id) REFERENCES cinemas(id)  
);