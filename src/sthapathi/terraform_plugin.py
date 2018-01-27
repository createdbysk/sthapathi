import plugin


class TerraformPlugin(plugin.Plugin):
    class Error(plugin.Plugin.Error):
        def __init__(self, msg):
            super(TerraformPlugin.Error, self).__init__(msg)

    def __init__(self):
        """
        Constructor
        """
        super(TerraformPlugin, self).__init__()

    def generate_target_configuration(self, provider, **kwargs):
        """
        Generates the terraform configuration based on the sthapathi configuration.
        :param provider: The provider for which to generate the target configuration
        :param kwargs: Arguments expected to generate the target configuration.
        """
        if "catalog_path" not in kwargs:
            raise TerraformPlugin.Error("catalog_path is required")

        if "configuration_reader" not in kwargs:
            raise TerraformPlugin.Error("configuration_reader is required")

        parameter_groups = kwargs.get("parameter_groups", [
            {
                "default": {}
            }
        ])

        catalog = self.__load_catalog(kwargs["catalog_path"])

        if provider not in catalog:
            raise TerraformPlugin.Error("{provider} not found in catalog named {catalog_name}".format(
                provider=provider,
                catalog_name=catalog["name"]
            ))

        configuration_reader = kwargs["configuration_reader"]

        target_configuration = {
            "module": {}
        }

        for element in configuration_reader.read():
            self.__add(target_configuration, element, catalog["name"], catalog[provider], parameter_groups)

        return target_configuration

    @staticmethod
    def __load_catalog(catalog_path):
        import yaml
        with open(catalog_path, 'r') as stream:
            return yaml.load(stream)

    def __add(self, target_configuration, element, catalog_name, provider_specific_catalog, parameter_groups):

        element_type = element["type"]

        if element_type not in provider_specific_catalog:
            raise TerraformPlugin.Error("{element_type} not found in catalog named {catalog_name}".format(
                element_type=element_type,
                catalog_name=catalog_name
            ))

        module_configuration = {
            "source": provider_specific_catalog[element_type]
        }

        parameters = self.build_parameters(element["parameters"], parameter_groups)
        module_configuration.update(parameters)

        name = element["name"]
        target_configuration["module"].update({
            name: module_configuration
        })

