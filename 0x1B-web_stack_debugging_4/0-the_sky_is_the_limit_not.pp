# Increase the requests' number to the server
exec { 'Increase_request's_number':
	command => 'sed -i \'s/15/2000/g\' /etc/default/nginx; service nginx restart',
	path => '/usr/bin'
}
