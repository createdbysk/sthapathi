from yaml_visitor import YamlVisitor


class CatalogYamlVisitorError(Exception):
    def __init__(self, msg):
        super(CatalogYamlVisitorError, self).__init__(msg)


class CatalogYamlVisitor(YamlVisitor):
    __PROVIDERS = "providers"
    __SOURCE = "source"
    __ARGUMENTS_KEY = "arguments"
    __ARGUMENT_GROUPS_KEY = "argument_groups"

    """Implements a YamlVisitor to visit a catalog.yaml file"""

    def __init__(self, catalog):
        self.__catalog = catalog

    def visit_mapping(self, element):
        argument_groups = element.get(CatalogYamlVisitor.__ARGUMENT_GROUPS_KEY, {})
        self.__validate_argument_groups(argument_groups)
        self.__catalog[CatalogYamlVisitor.__ARGUMENT_GROUPS_KEY] = argument_groups

        if CatalogYamlVisitor.__PROVIDERS in element:
            providers = element[CatalogYamlVisitor.__PROVIDERS]
            self.__validate_providers(providers, argument_groups)
            self.__catalog[CatalogYamlVisitor.__PROVIDERS] = providers
        else:
            raise CatalogYamlVisitorError("No known keys in {} in catalog".format(element))

    @staticmethod
    def __validate_argument_groups(argument_groups):
        if type(argument_groups) is not dict:
            raise CatalogYamlVisitorError("argument group in catalog must be a mapping. Found {}".format(
                argument_groups))


    @staticmethod
    def __validate_providers(providers, argument_groups):
        if type(providers) is not dict:
            raise CatalogYamlVisitorError("providers in catalog must be a mapping. Found {}".format(providers))

        if len(providers.keys()) == 0:
            raise CatalogYamlVisitorError("Expected at least one provider under providers in catalog. Found none.")

        for provider_name, provider in providers.iteritems():
            if type(provider) is not dict:
                raise CatalogYamlVisitorError("Expected at least one provider under providers in catalog. Found none.")

            for element_name, element in provider.iteritems():
                if CatalogYamlVisitor.__SOURCE not in element:
                    raise CatalogYamlVisitorError("Did not find key named {} for element named {} "
                                                  "in provider named {} in the catalog.".format(
                        CatalogYamlVisitor.__SOURCE, element_name, provider_name))


                if CatalogYamlVisitor.__ARGUMENTS_KEY in element:
                    arguments_or_group_name = element[CatalogYamlVisitor.__ARGUMENTS_KEY]
                    if type(arguments_or_group_name) is str and arguments_or_group_name not in argument_groups:
                        raise CatalogYamlVisitorError("Did not find argument group named {} in element named {} "
                                                      "in provider named {} in the catalog.".format(
                            arguments_or_group_name, element_name, provider_name))
