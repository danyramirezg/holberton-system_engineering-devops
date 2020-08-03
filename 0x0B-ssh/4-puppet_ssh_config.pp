# Using Puppet to make changes to the configuration file.
# The SSH client configuration must be configured to use the private key ~/.ssh/holberton
# The SSH client configuration must be configured to refuse to authenticate using a password

file_line { 'use the private key':
  ensure => 'present',
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'refuse the authentication':
  ensure => 'present',
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no'
}
