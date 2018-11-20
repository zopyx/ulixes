import pprint

class Config:

    def __init__(self):
        self.xxxx = 'hello'
        self.b = 12
        self.a = 42
        self.foo = 'bar'

    def as_ordered_dict(self):
        # dicts maintain insertion order in Python 3.6+
        return dict(sorted(self.__dict__.items()))

c = Config()
pprint.pprint(c.as_ordered_dict())
for k, v in c.as_ordered_dict().items():
    print(k, '=', v)
