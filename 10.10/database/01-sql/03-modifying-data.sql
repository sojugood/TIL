CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  content VARCHAR(200) NOT NULL,
  createdAt DATE NOT NULL
);

PRAGMA table_info('articles');

INSERT INTO
  articles (title, content, createdAt)
VALUES
  ('title1', 'content1', '2000-01-01'),
  ('title2', 'content2', '2010-01-01'),
  ('title3', 'content3', '2020-01-01');

INSERT INTO
  articles (title, content, createdAt)
VALUES
  ('title4', 'content4', DATE());

UPDATE
  articles
SET
  title = 'update Title'
WHERE
  id = 1;

UPDATE
  articles
SET
  title = 'update Title',
  content = 'update Content'
WHERE
  id = 2;

SELECT
  *
FROM
  articles
ORDER BY
  id DESC;

DELETE FROM
  albums
WHERE
  AlbumId = 5;

SELECT
  *
FROM
  albums;

DELETE FROM
  articles
WHERE
  id IN (SELECT id FROM articles ORDER BY createdAt LIMIT 2);

SELECT id FROM articles ORDER BY createdAt LIMIT 2;