#!/usr/bin/env bash

exec gunicorn -w 2 --threads 2 -b 0.0.0.0:80 "movie_library:create_app()"
