# Correct error from .phpp to php
exec { 'Fix error':
  command  => 'sed -i \'s/.phpp/.php/\' /var/www/html/wp-settings.php && sudo service apache2 restart',
  provider => shell,
}
