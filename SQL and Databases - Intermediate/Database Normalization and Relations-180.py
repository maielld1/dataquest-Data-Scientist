## 4. Querying a normalized database ##

portman_movies = list(conn.execute("SELECT ceremonies.year, nominations.movie FROM nominations INNER JOIN ceremonies ON nominations.ceremony_id == ceremonies.id WHERE nominations.nominee == 'Natalie Portman';"))

print(portman_movies)

## 6. Join table ##

five_join_table = list(conn.execute("select * from movies_actors limit 5"))
five_actors = list(conn.execute("select * from actors limit 5"))
five_movies = list(conn.execute("select * from movies limit 5"))

## 7. Querying a many-to-many relation ##

query = 'select actors.actor, movies.movie from movies inner join movies_actors on movies.id == movies_actors.movie_id inner join actors on movies_actors.actor_id == actors.id where movies.movie == "The King\'s Speech"'
kings_actors = conn.execute(query).fetchall()
print(kings_actors)
conn.close()


## 8. Practice: querying a many-to-many relation ##

query = 'select movies.movie, actors.actor from actors inner join movies_actors on actors.id == movies_actors.actor_id inner join movies on movies_actors.movie_id == movies.id where actors.actor == "Natalie Portman"'
portman_joins = conn.execute(query).fetchall()
print(portman_joins)
conn.close()