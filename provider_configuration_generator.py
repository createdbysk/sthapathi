import pystache


class ProviderConfigurationGenerator(object):
    """
    Provides the functionality to generate the provider specific configuration.
    """

    def __init__(self, template_loader, transform_loader, configuration_reader):
        """
        Stores the components necessary to generate the configuration.

        :param template_loader: The component that loads the template.
        :param transform_loader: The component that loads the configuration transform.
        :param configuration_reader: The component that reads the parts of the configuration.
        :return:
        """
        self._template_loader = template_loader
        self._transform_loader = transform_loader
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
                parameters = configuration_reader.read_parameters(configuration_parameters)
                self._parameters = transform.apply_transform(parameters)

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
                return self._parameters.get(item)

        configuration_type = self._configuration_reader.read_type(configuration_parameters)
        template = self._template_loader.load_template(provider, configuration_type)
        transform = self._transform_loader.load_transform(provider, configuration_type)
        context = Context(self._configuration_reader)
        generated_configuration = pystache.render(template, context)
        return generated_configuration
