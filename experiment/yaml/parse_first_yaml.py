import yaml

with open("first.yaml", 'r') as stream:
    for doc in yaml.load_all(stream):
        print doc