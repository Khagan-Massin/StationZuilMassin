CREATE TABLE station_service (
     station_city VARCHAR (50) PRIMARY KEY NOT NULL,
     country VARCHAR (2) NOT NULL,
     ov_bike BOOLEAN NOT NULL,
     elevator BOOLEAN NOT NULL,
     toilet BOOLEAN NOT NULL,
     park_and_ride BOOLEAN NOT NULL
);

CREATE TABLE moderator(
    mod_id serial PRIMARY KEY,
    mod_naam varchar(255),
    mod_email varchar(255),
    keuring_datumtijd varchar(255),
    bericht varchar(255)

);

CREATE TABLE opmerkingen(
    naam VARCHAR(255) NOT NULL,
    station VARCHAR(255) NOT NULL,
    bericht VARCHAR(255) NOT NULL,
    goedgekeurd boolean NOT NULL,
    id serial PRIMARY KEY,
    datetime VARCHAR(255),
    mod_id integer,
    FOREIGN KEY (mod_id)
	REFERENCES moderator(mod_id),
	FOREIGN KEY (station)
	REFERENCES station_service(station_city)   
);

INSERT INTO station_service (
    station_city, country, ov_bike, elevator, toilet, park_and_ride)
VALUES
    ('Arnhem', 'NL', true, false, true, false),
    ('Almere', 'NL', false, true, false, true),
    ('Amersfoort', 'NL', true, false, true, false),
    ('Almelo', 'NL', false, true, false, true),
    ('Alkmaar', 'NL', true, false, true, false),
    ('Apeldoorn', 'NL', false, true, false, true),
    ('Assen', 'NL', true, false, true, false),
    ('Amsterdam', 'NL', false, true, false, true),
    ('Boxtel', 'NL', true, false, true, false),
    ('Breda', 'NL', false, true, false, true),
    ('Dordrecht', 'NL', true, false, true, false),
    ('Delft', 'NL', false, true, false, true),
    ('Deventer', 'NL', true, false, true, false),
    ('Enschede', 'NL', false, true, false, true),
    ('Gouda', 'NL', true, false, true, false),
    ('Groningen', 'NL', false, true, false, true),
    ('Den Haag', 'NL', true, false, true, false),
    ('Hengelo', 'NL', false, true, false, true),
    ('Haarlem', 'NL', true, false, true, false),
    ('Helmond', 'NL', false, true, false, true),
    ('Hoorn', 'NL', true, false, true, false),
    ('Heerlen', 'NL', false, true, false, true),
    ('Den Bosch', 'NL', true, false, true, false),
    ('Hilversum', 'NL', false, true, false, true),
    ('Leiden', 'NL', true, false, true, false),
    ('Lelystad', 'NL', false, true, false, true),
    ('Leeuwarden', 'NL', true, false, true, false),
    ('Maastricht', 'NL', false, true, false, true),
    ('Nijmegen', 'NL', true, false, true, false),
    ('Oss', 'NL', false, true, false, true),
    ('Roermond', 'NL', true, false, true, false),
    ('Roosendaal', 'NL', false, true, false, true),
    ('Sittard', 'NL', true, false, true, false),
    ('Tilburg', 'NL', false, true, false, true),
    ('Utrecht', 'NL', true, false, true, false),
    ('Venlo', 'NL', false, true, false, true),
    ('Vlissingen', 'NL', true, false, true, false),
    ('Zaandam', 'NL', false, true, false, true),
    ('Zwolle', 'NL', true, false, true, false),
    ('Zutphen', 'NL', false, true, false, true);