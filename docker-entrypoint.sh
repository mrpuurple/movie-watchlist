#!/bin/sh

exec gunicorn --bind 0.0.0.0:80 "movie_library:create_app()"