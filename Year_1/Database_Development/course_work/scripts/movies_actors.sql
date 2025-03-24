CREATE TABLE movies_actors (
    id integer PRIMARY KEY,
    movie_id integer NOT NULL,
    actor_id integer NOT NULL,
    FOREIGN KEY (movie_id) REFERENCES movies(id),
    FOREIGN KEY (actor_id) REFERENCES actors(id)
);