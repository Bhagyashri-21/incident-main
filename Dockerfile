# Use official Python image
FROM python:3.11-bookworm

# Install Nginx
RUN apt-get update && apt-get install -y nginx

# Copy Nginx configuration
COPY ./nginx/nginx.conf /etc/nginx/sites-available/default

# Copy blog and portfolio static files
COPY ./blog /usr/share/nginx/html/blog
COPY ./incident-main/portfolio/resume.html /usr/share/nginx/html/portfolio/resume.html

# Copy the entrypoint script and make it executable
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Create working directory for the app
RUN mkdir -p /usr/app/myapp
WORKDIR /usr/app/myapp

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY ./incident-main/ .

# Expose port
EXPOSE 80

# Start the app and Nginx using the entrypoint
CMD ["/entrypoint.sh"]
