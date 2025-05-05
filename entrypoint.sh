#!/bin/bash

# Start Gunicorn
echo "Starting Gunicorn..."
gunicorn --workers 3 --bind 0.0.0.0:8000 incident_reporting_system.wsgi:application &

# Start Nginx
echo "Starting Nginx..."
nginx -g 'daemon off;'
