file { 'holberton':
	path => '/tmp/holberton'
	source_permissions =>'0744'
	owner => 'www-data'
	group => 'www-data'
	contains => "I love Puppet"
}
