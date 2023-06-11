-- not in my genres 

-- Joins 
SELECT DISTINCT tv_genres.name FROM tv_genres INNER JOIN (tv_shows, tv_show_genres)
  ON (tv_shows.id = tv_show_genres.show_id AND tv_genres.id = tv_show_genres.genre_id)
  WHERE tv_genres.name NOT IN (
    SELECT tv_genres.name FROM tv_genres INNER JOIN (tv_shows, tv_show_genres)
      ON (tv_shows.id = tv_show_genres.show_id AND tv_genres.id = tv_show_genres.genre_id)
      WHERE tv_shows.title = 'Dexter'
  )
  ORDER BY tv_genres.name ASC;
