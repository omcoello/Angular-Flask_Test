# Angular-Flask_Test

The code runs with two active servers, Flask and Angular.
Two endpoints are used. One to obtain the user account data and another to generate this data and save it in the database.

Additionally, after successfully running the docker container, it will be necessary to run the contents of insert_data.sql in the docker image after logging into the database with "mysql -u root -p" with the password "root". This is the only step that is not automated.
