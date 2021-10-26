# Purpose
As Sparkify we want to analyze the data that we've been collecting on song and user activity on our new streraming app.</br>
- We want to understand what songs our users are listening to.

# Schema Design
## Fact Table
### 1. `songplays` records in log data associated with song plays i.e. records with page NextSong
#### columns: `songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent`

## Dimension Tables
### 2. `users` users in the app
#### columns: `user_id, first_name, last_name, gender, level`
### 3. `songs` - songs in music database
#### columns: `song_id, title, artist_id, year, duration`
### 4. `artists` artists in music database
#### columns: `artist_id, name, location, latitude, longitude### columns: `
### 5. `time` timestamps of records in songplays broken down into specific units
#### columns: `start_time, hour, day, week, month, year, weekday`

# ETL Pipeline
The ETL Pipeline does the following things:</br>
- First, processes the `song_data` from `data/song_data` by getting the 'song_id', 'title', 'artist_id', 'year', 'duration' columns and loading them to the **songs** table.
- Second, processes the `artist_data` from `data/song_data` by getting the 'artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude' columns and loading them to the **artists** table.
- Third, processes the `time_data` from `data/log_data` by parsing the timestamp (milliseconds) to datetime pandas object and load the 'start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday' columns into the **time** table.
- Fourth, processes the user_Data from `data/log_data` by getting the 'userId', 'firstName', 'lastName', 'gender', 'level' columns and loading them into the **users** table.
- Finally, loads the **songplays** table by joining **songs** and **artists** where the song (name and duration) and artist's name are the same in the **users** table. 

```sql
SELECT s.song_id, a.artist_id FROM songs s JOIN artists a ON s.song_id = a.artist_id WHERE s.title = %s AND a.name = %s AND s.duration = %s;
```

# Files

### `test.ipynb`
Displays the first few rows of each table to let you check your database. </br>
### `create_tables.py`
Drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.</br>
### `etl.ipynb`
Reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.</br>
### `etl.py`
Reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook.</br>
### `sql_queries.py`
Contains all your sql queries, and is imported into the last three files above.</br>

# Run
### Drops and creates tables in the DB
`python3 create_tables.py`

### Run the ETL script
`python3 etl.py`