# Increase the requests' number to the server
exec { 'Increase_request__number':
    command => '/bin/sed -i "s/15/320000/g" /etc/default/nginx | service nginx restart'
}
