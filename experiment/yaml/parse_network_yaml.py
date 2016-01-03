import yaml

with open("network.yaml", 'r') as stream:
    for doc in yaml.load_all(stream):
        print doc