-- LEFT OUTER JOIN 

-- lists all shows and all genres linked to that show, from the database 

SELECT tv_shows.title, tv_genres.name FROM tv_shows LEFT OUTER JOIN (tv_show_genres, tv_genres)
  ON (tv_shows.id = tv_show_genres.show_id AND tv_genres.id = tv_show_genres.genre_id)
  ORDER BY tv_shows.title, tv_genres.name ASC;
