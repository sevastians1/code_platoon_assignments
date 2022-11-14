-- Schema
DROP TABLE IF EXISTS students;
CREATE TABLE customers (
    id                  serial PRIMARY KEY,
    first_name          varchar(50) NOT NULL,
    last_name           varchar(50) NOT NULL,
    birthdate           date NOT NULL,
    address_id          integer,
);

DROP TABLE IF EXISTS payment_details;
CREATE TABLE payment_details (
    id                  serieal PRIMARY KEY,
    street_address      varchar(100) NOT NULL,
    city                varchar(100) NOT NULL,
    state               varchar(50) NOT NULL,
    zipcode             integer NOT NULL,
    card_number         integer NOT NULL,
    card_expiration     varchar(20) NOT NULL,
    customer_id         integer REFERENCES customers,
)

DROP TABLE IF EXISTS addresses;
CREATE TABLE addresses (
    id                  serial PRIMARY KEY,
    street_address      varchar(100) NOT NULL,
    city                varchar(100) NOT NULL,
    state               varchar(50) NOT NULL,
    zipcode             integer NOT NULL,
    customer_id         integer REFERENCES customers,
);

DROP TABLE IF EXISTS categories;
CREATE TABLE categories (
    id                  serial PRIMARY KEY,
    name                varchar(100) NOT NULL,
)


DROP TABLE IF EXISTS products;
CREATE TABLE products (
    id                  serial PRIMARY KEY,
    name                varchar(100) NOT NULL,
    description         text,
    category_id         integer REFERENCES categories,
);

DROP TABLE IF EXISTS shopping_sessions;
CREATE TABLE shopping_sessions (
    id                  serial PRIMARY KEY,
    customer_id         integer REFERENCES customers,
    total               integer,
    order_placed        boolean,
);

DROP TABLE IF EXISTS carted_products;
CREATE TABLE carted_products (
    id                  serial PRIMARY KEY,
    quantity            integer,
    shopping_session_id integer REFERENCES shopping_sessions,
)

DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    id                  serial PRIMARY KEY,
    shopping_session_id integer REFERENCES shopping_sessions,
    payment_detail_id   integer REFERENCES payment_details,
)