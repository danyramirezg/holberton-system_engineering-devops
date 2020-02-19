# Correct error from .phpp to php
exec { 'fix error':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
}
exec { 'restart server':
  command => 'sudo service apache2 restart'
}
