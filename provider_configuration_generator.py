import sys
import os

current_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(current_dir, '.sthapathi'))


class ProviderConfigurationGenerator(object):
    """
    Provides the functionality to generate the provider specific configuration.
    """

    def __init__(self, configuration_reader):
        """
        Stores the components necessary to generate the configuration.

        :param configuration_reader: The component that reads the parts of the configuration.
        :return:
        """
        self.__configuration_reader = configuration_reader

    def generate_configuration(self, provider, configuration_parameters):
        """
        Generate the provider specific configuration given the configuration_parameters
        :param provider: The provider
        :param configuration_parameters: The configuration_parameters
        :return: The generated configuration.
        """

        configuration_type = self.__configuration_reader.read_type(configuration_parameters)
        name = self.__configuration_reader.read_name(configuration_parameters)
        parameters = self.__configuration_reader.read_parameters(configuration_parameters)

        import importlib
        module_name = "sthapathi-{provider}-{type}".format(provider=provider, type=configuration_type)
        generator = importlib.import_module(module_name)
        return generator.generator.generate(name, parameters, module_name)
