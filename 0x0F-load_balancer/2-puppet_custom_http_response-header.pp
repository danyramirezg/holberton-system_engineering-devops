#!/usr/bin/env bash
# Add a custom HTTP header with Puppet

package { 'nginx':
    ensure => installed,
}

service { 'nginx':
    ensure => 'running',
    require => Package['nginx'],
    enable => true,
}

file { '/var/www/html/index.html':
    require => Package['nginx'],
    content => 'Holberton School',
}

file_line { 'custom HTTP header':
    ensure => 'present',
    path => '/etc/nginx/sites-available/default',
    line => 'add_header X-Served-By "$HOSTNAME";',
    after => 'listen 80 default_server;',
 }

file_line { 'Redirection':
    ensure => 'present';
    path => '/etc/nginx/sites-available/default',
    after => 'server_name _;',
    line => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=FGdXnX25z6Q permanent;',
}
