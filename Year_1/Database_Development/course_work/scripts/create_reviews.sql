CREATE TABLE reviews (
    id integer PRIMARY KEY,
    movie integer NOT NULL,
    reviewer text NOT NULL,
    FOREIGN KEY (movie) REFERENCES movies(id)
);