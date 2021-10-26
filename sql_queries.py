# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE
songplays (songplay_id  INTEGER, start_time BIGINT, user_id INTEGER, level VARCHAR(15), song_id VARCHAR(50), artist_id VARCHAR(50), session_id INTEGER, location VARCHAR(150), user_agent VARCHAR(150));
""")

user_table_create = ("""
CREATE TABLE
users (user_id INTEGER, first_name VARCHAR(150), last_name VARCHAR(150), gender VARCHAR(1), level VARCHAR(15));
""")

song_table_create = ("""
CREATE TABLE
songs (song_id VARCHAR(50), title VARCHAR(150), artist_id VARCHAR(50), year INTEGER, duration DECIMAL);
""")

artist_table_create = ("""
CREATE TABLE
artists (artist_id VARCHAR(50), name VARCHAR(150), location VARCHAR(150), latitude TEXT, longitude TEXT);
""")

time_table_create = ("""
CREATE TABLE
time (start_time TIMESTAMP(3), hour INTEGER, day INTEGER, week INTEGER, month INTEGER, year INTEGER, weekday INTEGER);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s);
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s);
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s);
""")


time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s);
""")

# FIND SONGS

song_select = ("""
SELECT s.song_id, a.artist_id FROM songs s JOIN artists a ON s.song_id = a.artist_id WHERE s.title = %s AND a.name = %s AND s.duration = %s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]