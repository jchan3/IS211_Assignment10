"""Docstring for Joe Chan: music.sql"""

CREATE TABLE artist (id INTEGER PRIMARY KEY ASC,
                     first_name TEXT,
                     last_name TEXT);
CREATE TABLE album (id INTEGER PRIMARY KEY ASC,
                    artist_id INTEGER,
                    album_name TEXT);
CREATE TABLE song (id INTEGER PRIMARY KEY ASC,
                   album_id INTEGER,
                   song_name TEXT,
                   track_number INTEGER,
                   song_length INTEGER);
