#!/bin/bash

# Function for logging messages
log_message() {
    echo "$(date +'%Y-%m-%d %H:%M:%S') - $1"
}

# Attempt database migration with retry
while true; do
    log_message "Attempting database migration..."
    flask db upgrade
    if [[ "$?" == "0" ]]; then
        log_message "Database migration successful."
        break
    fi
    log_message "Upgrade command failed, retrying in 5 seconds..."
    sleep 5
done

# Start the Flask application
log_message "Starting Flask application..."
exec gunicorn -w 4 --bind 0.0.0.0:5000 microblog:app
