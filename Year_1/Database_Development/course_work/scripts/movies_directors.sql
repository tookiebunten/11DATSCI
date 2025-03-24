CREATE TABLE movies_directors (
    id integer PRIMARY KEY,
    movie integer NOT NULL,
    director integer NOT NULL,
    FOREIGN KEY (movie) REFERENCES movies(id),
    FOREIGN KEY (director) REFERENCES directors(id)
);