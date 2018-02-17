from yaml_visitor import YamlVisitor

class CatalogYamlVisitorError(Exception):
    def __init__(self, msg):
        super(CatalogYamlVisitorError, self).__init__(msg)


class CatalogYamlVisitor(YamlVisitor):
    __PROVIDERS = "providers"

    """Implements a YamlVisitor to visit a catalog.yaml file"""
    def __init__(self, catalog):
        self.__catalog = catalog

    def visit_mapping(self, element):
        if CatalogYamlVisitor.__PROVIDERS in element:
            self.__catalog[CatalogYamlVisitor.__PROVIDERS] = element[CatalogYamlVisitor.__PROVIDERS]
        else:
            raise CatalogYamlVisitorError("No known keys in {} in catalog".format(element))

    def visit_sequence(self, element):
        pass
