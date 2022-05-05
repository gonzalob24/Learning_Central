-- CHALLENGES
-- ask question: What am I trying to figure out

-- WHo are the top five oldest users
SELECT * FROM users u
ORDER BY created_at 
LIMIT 5;


-- What day of the week do most users register on?
SELECT DAYNAME(created_at) AS 'day', COUNT(*) AS total FROM users u
GROUP BY DAYNAME(created_at)
ORDER BY total DESC;

-- We want to target our inactive users with an email compaign. Find the users who have never posted a photo.
SELECT * FROM users u 
LEFT JOIN photos p ON p.user_id = u.id
WHERE p.user_id IS NULL;

-- We're running a new contest to see who can get the most likes on a single photo
SELECT u.username, p.id, p.image_url, COUNT(*) AS total_likes FROM photos p 
JOIN likes l ON l.photo_id = p.id
JOIN users u ON u.id = p.user_id
GROUP BY p.id
ORDER BY total_likes DESC
LIMIT 1;

-- Our investors want to know how many times does the averga user post
-- using subqueries
SELECT (SELECT COUNT(*) FROM photos p) /
(SELECT COUNT(*) FROM users u) AS avg;

-- A brand wants to know hwich hashtags to use in a post, What are the tio 5 most commony used hashtags?
SELECT * FROM photo_tags pt;

SELECT t.tag_name, COUNT(*) AS total FROM photo_tags pt
JOIN tags t ON t.id = pt.tag_id
GROUP BY t.tag_name
ORDER BY total DESC
LIMIT 5;

-- we have a small problem with bots o out site. Find users who have liked every single photo on the site.
-- I can't do a where because WHERE goes before the GROUP BY
SELECT * FROM photos p;

SELECT u.username, COUNT(*) AS user_likes FROM likes l
JOIN users u ON u.id = l.user_id
GROUP BY l.user_id
HAVING user_likes = 257;

-- this one is dynamic using a subquery
SELECT u.username, COUNT(*) AS total FROM users u 
JOIN likes l ON u.id = l.user_id 
GROUP BY l.user_id
HAVING total = (SELECT COUNT(*) FROM photos);







