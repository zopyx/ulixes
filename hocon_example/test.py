# https://github.com/chimpler/pyhocon

from pyhocon import ConfigFactory

conf = ConfigFactory.parse_file('test.conf')
host = conf.get_string('databases.mysql.host')
same_host = conf.get('databases.mysql.host')
same_host = conf['databases.mysql.host']
same_host = conf['databases']['mysql.host']
print(conf['databases.mysql.port'])
print(conf['databases']['mysql']['username'])
print(conf.get_config('databases')['mysql.password'])
print(conf.get('databases.mysql.password', 'default_password'))
