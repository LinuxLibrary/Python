-- Create a table named Users with 2 columns "name" and "email" --
CREATE TABLE Users (
   name VARCHAR(128),
   email VARCHAR(128)
   );

-- Describe Users table --
PRAGMA table_info(Users);

-- Insert some values into that table --
INSERT INTO Users (name,email) VALUES ('Arjun','vmsnivas@gmail.com');
INSERT INTO Users (name,email) VALUES ('Mallik','mallikbheesetti@gmail.com');
INSERT INTO Users (name,email) VALUES ('Nivas','srinivas@gmail.com');

-- Delete a row --
DELETE FROM Users WHERE email='srinivas@gmail.com';
-- or else
DELETE FROM Users WHERE name='Nivas';

-- Update a row --
UPDATE Users SET name='ArjunShrinivas' WHERE email='vmsnivas@gmail.com';

-- Read or Retrieve a record --
SELECT * FROM Users WHERE email='vmsnivas@gmail.com';
SELECT * FROM Users WHERE email like '%@gmail.com';
