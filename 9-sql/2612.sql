SELECT m.id,m.name
FROM movies AS m
INNER JOIN genres AS g ON m.id_genres=g.id
WHERE g.description='Action'
AND m.id IN(
    SELECT DISTINCT ma.id_movies
    FROM movies_actors AS ma
    INNER JOIN actors AS a ON a.id=ma.id_actors
    WHERE a.name='Marcelo Silva' OR a.name='Miguel Silva'
);
