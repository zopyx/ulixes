import yaml
import pprint


with open('test.yaml') as fp:
    result = yaml.load(fp)

pprint.pprint(result)
