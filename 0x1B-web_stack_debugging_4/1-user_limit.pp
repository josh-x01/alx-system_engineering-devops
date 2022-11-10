# Fix open file limit

exec {'change-os-configuration-for-holberton-user':
  command  => 'sed -i s/holberton/foo/ /etc/security/limits.conf',
  provider => 'shell'
}
