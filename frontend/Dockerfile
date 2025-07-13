# Use nginx to serve static files
FROM nginx:alpine

# Remove default nginx static files
RUN rm -rf /usr/share/nginx/html/*

# Copy your frontend files to nginx html directory
COPY . /usr/share/nginx/html

# Expose port 80
EXPOSE 80
