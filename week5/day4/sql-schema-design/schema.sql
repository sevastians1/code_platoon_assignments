

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id          serial PRIMARY KEY,
    first_name  varchar(255) NOT NULL,
    last_name   varchar(255) NOT NULL
);

DROP TABLE IF EXISTS addresses;
CREATE TABLE addresses (
    id          serial PRIMARY KEY,
    street      varchar(255) NOT NULL,
    street2     varchar(255),
    city        varchar(255) NOT NULL,
    state       varchar(255) NOT NULL,
    zip_code    integer,
    country     varchar(255) NOT NULL 
);

DROP TABLE IF EXISTS restaurants;
CREATE TABLE restaurants (
    id               serial PRIMARY KEY,
    name             varchar(255) NOT NULL,
    address_id       integer REFERENCES addresses (id)
);

DROP TABLE IF EXISTS menu_items;
CREATE TABLE menu_items (
    id               serial PRIMARY KEY,
    name             varchar(255) NOT NULL,
    price            float NOT NULL,
    restaurant_id    integer REFERENCES restaurants (id)
);

DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    id                  serial PRIMARY KEY,
    user_id             integer REFERENCES users (id),
    address_id          integer REFERENCES addresses (id)
);

DROP TABLE IF EXISTS order_menu_items;
CREATE TABLE order_menu_items (
    id               serial PRIMARY KEY,
    order_id         integer REFERENCES orders (id),
    menu_item_id          integer REFERENCES menu_items (id)
);


