CREATE TABLE payments (
    id INTEGER,
    type VARCHAR(255),
    date DATE,
    PRIMARY KEY(id),
    FOREIGN KEY(id) REFERENCES tickets(id)
);

CREATE TABLE seances (
    id SERIAL,
    name VARCHAR(255),
    cinema_name VARCHAR(255),
    PRIMARY KEY(id)
);
INSERT INTO seances (name, cinema_name) VALUES
('Kevin sam w domu 12:00', 'Kino Tralal'),
('Rambo 15:00', 'Kino Praga'),
('Django 16:30', 'Kino Praga'),
('Kill Bill 23:00', 'Kino Tralal');


CREATE TABLE tickets (
    id SERIAL,
    quantity INTEGER,
    price DECIMAL(5,2),
    seance_id INTEGER,
    PRIMARY KEY(id),
    FOREIGN KEY(seance_id) REFERENCES seances(id)
);


CREATE TABLE cinemas (
    id SERIAL,
    name VARCHAR(255),
    address VARCHAR(255),
    capacity INTEGER,
    PRIMARY KEY(id)
);

INSERT INTO cinemas VALUES (DEFAULT, 'Wolność', 'Krakowskie Przedmieście 12/3', 300);
INSERT INTO cinemas VALUES (DEFAULT, 'Arkadia', 'Inflacka 12', 100);
INSERT INTO cinemas VALUES (DEFAULT, 'Blue City', 'Al. Jerozolimskie 1', 500);
INSERT INTO cinemas VALUES (DEFAULT, 'Cinema Galaxy', 'Jowiszowa 1', 300);

CREATE TABLE movies (
    id SERIAL,
    name VARCHAR(255),
    description VARCHAR(255),
    rating NUMERIC(5,2),
    PRIMARY KEY(id)
);
INSERT INTO movies VALUES (DEFAULT, 'K-Pax', 'o kosmitach', 9.8);
INSERT INTO movies VALUES (DEFAULT, 'Fight Club', 'o biciu sie i schizofreni', 9.9);
INSERT INTO movies VALUES (DEFAULT, 'Benjamin Button', 'znowu brad pitt', 9.2);
INSERT INTO movies VALUES (DEFAULT, 'Incepcja', 'nie ogarniecie tego!', 8.7);

CREATE TABLE seances (
  id SERIAL,
  cinema_id INTEGER NOT NULL,
  movie_id INTEGER NOT NULL,
  PRIMARY KEY(id),
  FOREIGN KEY(cinema_id) REFERENCES cinemas(id),
  FOREIGN KEY(movie_id) REFERENCES movies(id),
  UNIQUE (cinema_id, movie_id)
);

""" KOMENTARZ: końcowy UNIQUE (cinema_id, movie_id) jest po to, aby niemożliwe było dodanie drugi
raz obiektu o tych samych wartościach w kolumnach cinema_id i movie_id.
Zwykle pisaliśmy UNIQUE po typie pola, jednak można również dopisywać go na końcu, podobnie jak primary key.
W nawiasie możemy przekazać więcej niż jedną kolumnę, wtedy każda z nich z osobna nie będzie unikalna, ale obie
naraz już tak. To znaczy, że będą mogły istnieć seanse o tej samej wartości pól cinema_id, oraz będą mogły istnieć
seanse o tej samej wartości pól movie_id, natomiast nigdy nie wystąpi sytuacja, że dwa seanse mają te same wartości
w obu polach.
"""