
CREATE TABLE state
(
    user_id integer NOT NULL,
    task character varying(100) COLLATE pg_catalog."default",
    answer character varying(100) COLLATE pg_catalog."default",
    tries integer,
    CONSTRAINT state_pkey PRIMARY KEY (user_id)
)
