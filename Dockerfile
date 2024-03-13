FROM python:slim

# Install required dependencies
RUN apt-get update && apt-get install -y default-libmysqlclient-dev && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt to the container
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install gunicorn
RUN pip install gunicorn

# Copy the application code to the container
COPY app app
COPY migrations migrations
COPY microblog.py config.py boot.sh ./

# Make boot.sh executable
RUN chmod +x boot.sh

# Set the Flask app environment variable
ENV FLASK_APP microblog.py

# Expose port 5000
EXPOSE 5000

# Set the entry point
ENTRYPOINT ["./boot.sh"]
