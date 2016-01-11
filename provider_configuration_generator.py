import pystache


class ProviderConfigurationGenerator(object):
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
            def __init__(self, configuration_reader):
                # configuration_parameters, which is the parameter passed to the enclosing function
                # is available in this scope.
                self._name = configuration_reader.read_name(configuration_parameters)
                self._parameters = configuration_reader.read_parameters(configuration_parameters)

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

        configuration_type = self._configuration_reader.read_type(configuration_parameters)
        template = self._template_loader.load_template(provider, configuration_type)
        context = Context(self._configuration_reader)
        generated_configuration = pystache.render(template, context)
        return generated_configuration
