#!/usr/bin/env bash

# Start the main web server (gunicorn) on the host and port Render provides
gunicorn blog_project.wsgi:application --bind 0.0.0.0:$PORT &

# Start the chat server (daphne) on a different port in the foreground
daphne -b 0.0.0.0 -p 10001 blog_project.asgi:application
