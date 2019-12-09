# Create a manifest that kills a process named killmenow

exec {'Kills_process':
  path    => '/usr/bin',
  command => 'pkill -f killmenow',
}
