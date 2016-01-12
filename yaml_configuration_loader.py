import yaml


def load_configuration(stream):
    """
    GIVEN a yaml file that is formatted as shown below to configure a network
    WHEN sthapathi loads the yaml file
    THEN sthapathi loads it in the representation ["name", "network", {"cidr_block": "<cidr_block>"}]

    yaml format for network:
    name:
    - network
    - cidr_block:<cidr_block>

    :param stream: The stream that contains the contents of the yaml configuration.
    :return: yields the contents.
    """
    for document in yaml.load_all(stream):
        # document is expected in the form
        # {
        #   name1: {
        #       type1,
        #       {... parameters1 ...}
        #   },
        #   name2: {
        #       type2,
        #       {... parameters2 ...}
        #   },
        #   ...
        # }
        for name, [configuration_type, parameters] in document.iteritems():
            configuration = [name, configuration_type, parameters]
            yield configuration
