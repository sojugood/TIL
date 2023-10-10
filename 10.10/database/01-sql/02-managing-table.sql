CREATE TABLE examples (
  ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
  LastName VARCHAR(50) NOT NULL,
  FirstName VARCHAR(50) NOT NULL
);

PRAGMA table_info('examples');
-- cid : 컬럼 아이디

ALTER TABLE
  examples
ADD COLUMN
  Country VARCHAR(50) NOT NULL DEFAULT 1;

ALTER TABLE
  examples
ADD COLUMN
  Age INTEGER NOT NULL DEFAULT 1;

ALTER TABLE
  examples
ADD COLUMN
  Adderss VARCHAR(100) NOT NULL DEFAULT 1;

ALTER TABLE
  examples
RENAME COLUMN
  Adderss
TO
  PostCode;

ALTER TABLE
  examples
DROP COLUMN
  PostCode;

SELECT sqlite_version();

