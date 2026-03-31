#!/bin/bash
# Start the cron service
service cron start

# Start Apache in the foreground
exec apache2-foreground


chown -R www-data:www-data /var/www/html/config.php /var/www/moodledata
chown www-data:www-data /var/www/html/config.php
chmod 644 /var/www/html/config.php