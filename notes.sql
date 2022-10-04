-- Four basic queries: SELECT, DELETE, INSERT, UPDATE

-- INSERT
-- INSERT INTO table_name (column_name, column_name ) VALUES (column_val, column_val), (column_val, column_val);

INSERT INTO users (name, email) VALUES ("Spencer", "spencer@email.com"), ("Joe", "joe@email.com");

-- INSERT WITH A ONE TO ONE oR ONE TO MANY:

INSERT INTO posts (content, user_id) VALUES ("This is the first post for this site!", 1);

-- we need to supply the fk, fk must match with an entry in the related table

INSERT INTO pizzas (size, crust) VALUES ( 10, "deep");
INSERT INTO toppings (vegetarian, name) VALUES (1,"olives");

-- Many to many, must supply both fks

INSERT INTO pizzas_have_toppings (topping_id, pizza_id) VALUES (1,1);

-- SELECT data retrieval (READ)
-- SELECT what_to_grab FROM where_we_want_to_grab_it_from WHERE condition;

SELECT * FROM users WHERE name = "Spencer";

SELECT name AS fake_name FROM users ORDER BY created_at ASC;

-- UPDATE
-- UPDATE table_name SET column_name = val, column_name = val WHERE condition;
SELECT * FROM users;
UPDATE users SET name = "Reset" WHERE id = 3;

-- DELETE
-- DELETE FROM table WHERE condition;

DELETE FROM users WHERE id = 3;









