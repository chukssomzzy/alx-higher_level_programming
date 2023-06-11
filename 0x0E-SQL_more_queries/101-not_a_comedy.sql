-- Left join 

-- query with left join and , 

SELECT DISTINCT tv_shows.title FROM tv_shows LEFT OUTER JOIN (tv_genres, tv_show_genres)
  ON (tv_shows.id = tv_show_genres.show_id AND tv_genres.id = tv_show_genres.genre_id)
  WHERE tv_genres.name <> 'Comedy' OR tv_genres.id IS NULL
  ORDER BY tv_shows.title ASC;
