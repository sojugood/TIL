CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL
);

PRAGMA table_info('users');

CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(50) NOT NULL,
  content VARCHAR(100) NOT NULL,
  userId INTEGER NOT NULL,
  FOREIGN KEY (userId)
    REFERENCES users(id)
);

PRAGMA table_info('articles');

INSERT INTO
  users(name)
VALUES
  ('하석주'),
  ('송윤미'),
  ('유하선');

SELECT * FROM users;

INSERT INTO
  articles(title, content, userId)
VALUES
  ('제목1', '내용1', 1),
  ('제목2', '내용2', 2),
  ('제목3', '내용3', 1),
  ('제목4', '내용4', 4),
  ('제목5', '내용5', 1);

SELECT * FROM articles;

-- join
SELECT * FROM articles
INNER JOIN users
  ON users.id = articles.userId;

SELECT articles.title, users.name
  FROM articles
INNER JOIN users
  ON users.id = articles.userId
-- WHERE users.id = 1;
-- WHERE users.name = '하석주';
WHERE userId = 1;

SELECT articles.title, users.name
  FROM users
INNER JOIN articles
  ON users.id = articles.userId
-- WHERE users.id = 1;
WHERE users.name = '하석주';

SELECT * FROM articles
LEFT JOIN users
  ON users.id = articles.userId;

SELECT * FROM articles
RIGHT JOIN users
  ON users.id = articles.userId
WHERE articles.title IS NULL;

SELECT * FROM users
LEFT JOIN articles
  ON users.id = articles.userId
WHERE userId IS NULL;
