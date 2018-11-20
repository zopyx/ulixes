import toml
import pprint

toml_string = """
# This is a TOML document.

title = "TOML Example"

[owner]
name = "Tom Preston-Werner"
dob = 1979-05-27T07:32:00-08:00 # First class dates

[database]
server = "192.168.1.1"
ports = [ 8001, 8001, 8002 ]
connection_max = 5000
enabled = true

[servers]

  # Indentation (tabs and/or spaces) is allowed but not required
  [servers.alpha]
  ip = "10.0.0.1"
  dc = "eqdc10"

  [servers.beta]
  ip = "10.0.0.2"
  dc = "eqdc10"

[clients]
data = [ ["gamma", "delta"], [1, 2] ]

# Line breaks are OK when inside arrays
hosts = [
  "alpha",
  "omega"
]
"""

class BaseConfig(dict):

    _defaults = {}

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

    def get_by_key(self, key):
        try:
            return self._get_by_key(key)
        except KeyError:
            if key in self._defaults:
                return self._defaults[key]
        raise KeyError('Unknown key: "{0}"'.format(key))


    def _get_by_key(self, key):
        current = self
        for name in key.split('.'):
            current = current[name]
        return current


class MyConfig(BaseConfig):

    _defaults = {
        'foo.bar': 42
    }


result = toml.loads(toml_string, _dict=MyConfig)

print(result.__class__)
pprint.pprint(result)
print(result['servers']['alpha']['ip'])
print(result.get_by_key('servers.alpha.ip'))
print(result.get_by_key('clients.data'))
print(result.get_by_key('foo.bar'))

import pdb; pdb.set_trace()

