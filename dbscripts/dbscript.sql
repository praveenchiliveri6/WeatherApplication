
CREATE SCHEMA IF NOT EXISTS info;

CREATE TABLE info.city
(
    id serial,
    city_name character varying COLLATE pg_catalog."default",
    CONSTRAINT city_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE info.city
    OWNER to postgres;