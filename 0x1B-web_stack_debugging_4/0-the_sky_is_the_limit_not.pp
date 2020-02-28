# Increase the requests' number to the server
exec { 'Increase_request's_number':
	command => '/bin/sed 'sed -i "s/15/20000/g" /etc/default/nginx | service nginx restart'
}
