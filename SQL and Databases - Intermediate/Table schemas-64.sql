## 2. Adding columns ##

ALTER TABLE facts
ADD leader text;

## 6. Creating a table with relations ##

CREATE TABLE factbook.states(
   id integer PRIMARY KEY,
   name text,
   country integer,
   area integer,
   FOREIGN KEY(id) REFERENCES facts(id)
);

## 7. Querying across foreign keys ##

SELECT * from landmarks
INNER JOIN facts
ON landmarks.country == facts.id;

## 8. Types of joins ##

SELECT * from landmarks
LEFT JOIN facts
ON landmarks.country == facts.id;