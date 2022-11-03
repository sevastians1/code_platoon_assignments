
-- USERS
INSERT INTO users (first_name, last_name) VALUES ('John', 'Doe');
INSERT INTO users (first_name, last_name) VALUES ('Jake', 'Doe2');
INSERT INTO users (first_name, last_name) VALUES ('John3', 'Doe3');
INSERT INTO users (first_name, last_name) VALUES ('John4', 'Doe4');



-- ADDRESSES
INSERT INTO addresses (street, city, state, zip_code, country) VALUES ('6232 Guiseppe Courts', 'Jamartown', 'Maryland', '49028', 'US');
INSERT INTO addresses (street, city, state, zip_code, country) VALUES ('704 Cecil Mountain', 'West Jon', 'South Dakota', '91578', 'US');
INSERT INTO addresses (street, city, state, zip_code, country) VALUES ('41613 Huel Ranch', 'Loycefort', 'Florida', '12109', 'US');
INSERT INTO addresses (street, city, state, zip_code, country) VALUES ('1397 Braden Shoals', 'New Karine', 'New York', '03913', 'US');


-- RESTAURANTS
INSERT INTO restaurants (name, address_id) VALUES ('Burger King', 2);
INSERT INTO restaurants (name, address_id) VALUES ('Chinese Restaraunt', 3);


-- MENU ITEMS
INSERT INTO menu_items (name, price, restaurant_id) VALUES ('CS 101', 4, 1);
INSERT INTO menu_items (name, price, restaurant_id) VALUES ('HIST 107', 8, 2);
INSERT INTO menu_items (name, price, restaurant_id) VALUES ('SPAN 210', 5, 2);
INSERT INTO menu_items (name, price, restaurant_id) VALUES ('PHYS 218', 4, 1);
INSERT INTO menu_items (name, price, restaurant_id) VALUES ('ART 118', 2, 2);




