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

    def generate_target_configuration(self, provider, component, **kwargs):
        """
        Generates the terraform configuration based on the sthapathi configuration.
        :param component: The component this configuration belongs to.
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

        target_configuration = {}
        self.__add_provider_and_backend(target_configuration, provider, component)

        modules = {}
        variables = {}
        current_active_parameter_group = "default"

        for element in configuration_reader.read():
            self.__parse_element(catalog, element, parameter_groups, provider, modules, variables,
                                 current_active_parameter_group)

        for parameter_group_name, parameter_group in parameter_groups.iteritems():
            self.__parse_variables(parameter_group["variables"], variables)

        target_configuration.update({
            "module": modules,
            "variable": variables
        })

        return target_configuration

    def __parse_variables(self, local_variables, variables):
        for parameter in local_variables:
            value = {}
            if type(parameter) is dict:
                variable_name = parameter.keys()[0]
                if "type" in parameter[variable_name]:
                    value["type"] = parameter[variable_name]["type"]
            else:
                variable_name = parameter
            variables.update({variable_name: value})

    def __parse_element(self, catalog, element, parameter_groups, provider, modules, variables,
                        active_parameter_group):
        import json
        if "group" in element:
            self.__create_group_configuration(element, catalog, parameter_groups, provider, modules, variables,
                                              active_parameter_group)
        elif "module" in element:
            module_configuration = self.__create_module_configuration(element, catalog["name"], catalog[provider],
                                                                      parameter_groups, active_parameter_group)
            modules.update(module_configuration)
        elif "variables" in element:
            self.__parse_variables(element["variables"], variables)
        else:
            raise TerraformPlugin.Error("Unknown element {element}".format(
                element=json.dumps(element)
            ))

    @staticmethod
    def __load_catalog(catalog_path):
        import yaml
        with open(catalog_path, 'r') as stream:
            return yaml.load(stream)

    @staticmethod
    def __add_provider_and_backend(target_configuration, provider, component):
        terraform = {
            "terraform": {
                "required_version": ">= 0.10, < 0.12",
                "backend": {
                    "s3": {
                        "key": "dpk/dpk-{component}/{component}.tfstate".format(component=component),
                        "encrypt": 1
                    }
                }
            }
        }

        provider = {
            "provider": {
                provider: {
                    "profile": "${var.env}",
                    "region": "${var.region}"
                }
            }
        }

        target_configuration.update(terraform)
        target_configuration.update(provider)

    def __create_module_configuration(self, element, catalog_name, provider_specific_catalog, parameter_groups,
                                      active_parameter_group):
        element_type = element["module"]

        if element_type not in provider_specific_catalog:
            raise TerraformPlugin.Error("{element_type} not found in catalog named {catalog_name}".format(
                element_type=element_type,
                catalog_name=catalog_name
            ))

        module_configuration = {
            "source": provider_specific_catalog[element_type]
        }

        parameters = self.build_parameters(element["parameters"], parameter_groups, active_parameter_group)
        module_configuration.update(parameters)

        name = element["name"]

        return {
            name: module_configuration
        }

    def __create_group_configuration(self, element, catalog, parameter_groups, provider, modules, variables,
                                     active_parameter_group):
        group = element["group"]

        group_parameter_group = group.get("parameter_group_name", active_parameter_group)
        elements = group.get("elements", [])

        for element in elements:
            self.__parse_element(catalog, element, parameter_groups, provider, modules, variables,
                                 group_parameter_group)


