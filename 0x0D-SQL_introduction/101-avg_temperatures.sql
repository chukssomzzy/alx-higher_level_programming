-- find the average temperature 

-- finds avg and sort
SELECT city, AVG(value) AS avg_temp FROM temperatures
  GROUP BY city 
  ORDER BY avg_temp DESC;
