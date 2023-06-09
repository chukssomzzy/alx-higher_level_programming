-- select cities of california in asc 

-- SELECT Query 
SELECT id, name FROM cities WHERE state_id = (
  SELECT id FROM states WHERE name = 'california'
  LIMIT 1)
  ORDER BY id ASC;
