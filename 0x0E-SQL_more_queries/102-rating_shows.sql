-- script that list all shows without the genre Comedy in the databases
-- hbtn_0d_tvshows.
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating -- Query to join tables
FROM tv_shows
JOIN tv_show_ratings
     ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_shows.title
ORDER BY rating DESC;
