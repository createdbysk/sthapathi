class YamlVisitor(object):
    """Base class for yaml visitors"""
    def visit_mapping(self, element):
        """Override in derived class to visit a yaml mapping (object, dictionary)"""
        raise NotImplementedError("YamlVisitor.visit_mapping is not implemented in {}.".format(type(self).__name__))
