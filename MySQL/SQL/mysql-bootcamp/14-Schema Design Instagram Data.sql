-- USERS
CREATE DATABASE instagram_clone;

CREATE TABLE users(
	id INT AUTO_INCREMENT PRIMARY KEY,
	username VARCHAR(255) UNIQUE,
	created_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO users(username)
VALUES ('BlueTheCAT'),
	   ('CHarlieBrown'),
	   ('NZO');
	  
-- PHOTOS, should I add DELETE CASCADE
CREATE TABLE photos(
	id INT AUTO_INCREMENT PRIMARY KEY,
	image_url VARCHAR(255) NOT NULL,
	user_id INT NOT NULL,
	created_at TIMESTAMP DEFAULT NOW(),
	FOREIGN KEY(user_id) REFERENCES users(id)
);

INSERT INTO photos(image_url, user_id)
VALUES ('/qwerty', 1),
('/qwerty1', 2),
('/qwerty2', 2);


-- COMMENTS
CREATE TABLE comments(
	id INT AUTO_INCREMENT PRIMARY KEY,
	comment_text VARCHAR(255) NOT NULL,
	user_id INT NOT NULL,
	photo_id INT NOT NULL,
	created_at TIMESTAMP DEFAULT NOW(),
	FOREIGN KEY(user_id) REFERENCES users(id),
	FOREIGN KEY (photo_id) REFERENCES photos(id)
);

INSERT INTO comments(comment_text, user_id, photo_id)
VALUES('Meow', 1, 2), ('Amazing shot!', 3, 2), ('I heart this', 2, 1);


-- LIKES, no id because we don't need it. 
-- How do i ensure that there is 1 like per user? I would need a unique combination of the two foreign keys
-- Create a composite key to assign one value per combination/user.
CREATE TABLE likes(
	user_id INT NOT NULL,
	photo_id INT NOT NULL,
	created_at TIMESTAMP DEFAULT NOW(),
	FOREIGN KEY(user_id) REFERENCES users(id),
	FOREIGN KEY(photo_id) REFERENCES photos(id),
	PRIMARY KEY(user_id, photo_id)
);

INSERT INTO likes(user_id, photo_id)
VALUES(1, 1), (2, 1), (1, 2), (3,3); 

-- this will give a duplicate key error because user_id 1 already likes photo_id 1
INSERT INTO likes(user_id, photo_id)
VALUES(1,1);

-- FLLOWERS SCHEMA DESIGN
CREATE TABLE follows(
	follower_id INT NOT NULL,
	followee_id INT NOT NULL,
	created_at TIMESTAMP DEFAULT NOW(),
	FOREIGN KEY(follower_id) REFERENCES users(id),
	FOREIGN KEY(followee_id) REFERENCES users(id),
	PRIMARY KEY(follower_id, followee_id)
);

INSERT INTO follows(follower_id, followee_id)
VALUES(1,2), (1,3), (3,1), (2,3), (2,1);

INSERT INTO follows(follower_id, followee_id)
VALUES(2,1);

-- HASH TAGS: A few solutions
-- in my photos table I can include a tags column and separate them by '#'
	-- to add a new tag I can append the new tag at the end
	-- Searching may be slow since I will use LIKE 
	-- can't store additional info, like first person to use a hash tag
	-- will not be able to track trends
-- Solution 2:
	-- use two tables, the second table will have tag_name and photo_id.

CREATE TABLE tags(
	id INT AUTO_INCREMENT PRIMARY KEY,
	tag_name VARCHAR(255) UNIQUE,
	created_at TIMESTAMP
);

CREATE TABLE photo_tags(
	photo_id INT NOT NULL,
	tag_id INT NOT NULL,
	FOREIGN KEY(photo_id) REFERENCES photos(id),
	FOREIGN KEY(tag_id) REFERENCES tags(id),
	PRIMARY KEY(photo_id, tag_id)
);

INSERT INTO tags(tag_name)
VALUES('adorable'),('cute'),('sunrise');

INSERT INTO photo_tags(photo_id, tag_id)
VALUES(1,1),(1,2),(2,3),(3,2);

INSERT INTO photo_tags(photo_id, tag_id)
VALUES(1,1);

-- SELECT statments
SELECT * FROM comments;









