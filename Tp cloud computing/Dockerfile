# Use the official PHP Apache image as base
FROM php:7.4-apache

# Install MySQL client library
RUN docker-php-ext-install mysqli && docker-php-ext-enable mysqli

# Copy PHP files into Apache document root
COPY src/ /var/www/html/

# Change the ownership of the web directory to the Apache user
RUN chown -R www-data:www-data /var/www/html/

# Set environment variables for MySQL connection
ENV MYSQL_HOST=mysql
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=password
ENV MYSQL_DATABASE=my_database

# Configure Apache
RUN a2enmod rewrite

# Expose port 80
EXPOSE 80
