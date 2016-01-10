import pystache


class ConfigurationGenerator(object):
    """
    Provides the functionality to generate the provider specific configuration.
    """

    def __init__(self, template_loader, configuration_reader):
        self._template_loader = template_loader
        self._configuration_reader = configuration_reader

    def generate_configuration(self, provider, configuration_parameters):
        """
        Generate the provider specific configuration given the configuration_parameters
        :param provider: The provider
        :param configuration_parameters: The configuration_parameters
        :return: The generated configuration.
        """
        class Context(object):
            """
            Use this class to add name to the collection of template parameters.
            """
            def __init__(self, name, parameters):
                self._name = name
                self._parameters = parameters

            def name(self):
                """
                The name of the configuration from the configuration_parameters
                :return: configuration_name
                """
                return self._name

            def __getattr__(self, item):
                """
                All other context values other than the name are in the configuration_parameters.
                :param item: The key from the template
                :return: The value corresponding to the key
                """
                return self._parameters[item]

        configuration_name = self._configuration_reader.read_name(configuration_parameters)
        configuration_type = self._configuration_reader.read_type(configuration_parameters)
        parameters = self._configuration_reader.read_parameters(configuration_parameters)
        template = self._template_loader.load_template(provider, configuration_type)
        context = Context(configuration_name, parameters)
        generated_configuration = pystache.render(template, context)
        return generated_configuration
