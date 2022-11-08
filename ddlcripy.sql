CREATE TABLE moderator(
    mod_id serial PRIMARY KEY,
    mod_naam varchar(255),
    mod_email varchar(255),
    keuring_datumtijd varchar(255),
    bericht varchar(255)

);

alter table opmerkingen
add constraint fk_mod_id
FOREIGN key (mod_ID) REFERENCES moderator(mod_ID);
