-- join with multiple tables

-- join 
SELECT tv_genres.name FROM tv_shows INNER JOIN (tv_genres,tv_show_genres)
  ON (tv_genres.id = tv_show_genres.genre_id AND tv_shows.id = tv_show_genres.show_id)
  WHERE tv_shows.title = 'Dexter'
  ORDER BY tv_genres.name ASC;
