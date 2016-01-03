import yaml


def parse_yaml(filename):
    """
    Parse the given yaml file and print the parsed output.
    :param filename: The name of the file whose contents to parse.
    :return: None
    """
    with open(filename, 'r') as stream:
        for doc in yaml.load_all(stream):
            print doc