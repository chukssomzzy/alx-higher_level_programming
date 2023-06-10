-- LIst by genre 

-- Join 
SELECT tv_shows.title FROM tv_shows INNER JOIN (tv_show_genres, tv_genres)
  ON (tv_genres.id = tv_show_genres.genre_id AND tv_shows.id = tv_show_genres.show_id)
  WHERE tv_genres.name = 'Comedy'
  ORDER BY tv_shows.title ASC;
