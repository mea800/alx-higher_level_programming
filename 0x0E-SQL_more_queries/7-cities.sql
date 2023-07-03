-- script that create a database hbtn_0d_usa & the table cities
-- (in the database hbtn_0d_usa) on your MySQL server.
-- cities description:___
--      id INT unique, auto generated, can’t be null & is a primary key.
--      state_id INT, can’t be null and must be a FOREIGN KEY that
--      reference to id of the states table.
--      name VARCHAR(256) can’t be null.
-- If the database hbtn_0d_usa already exist, your script should not fail.
-- If the table cities already exist, your script should not fail.
-- CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
