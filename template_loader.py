import trace_logging


class TemplateLoader(object):
    def __init__(self, path_resolver_class):
        self._logger = trace_logging.getLogger(self.__module__)
        self._path_resolver = path_resolver_class()

    def load_template(self, _provider, _resource):
        self._logger.trace("load_template(%s, %s)", _provider, _resource)
        template_path = self._path_resolver.resolve_path(_provider, _resource)
        self._logger.trace("load_template(%s, %s) - read template from %s", _provider, _resource, template_path)
        with open(template_path, 'r') as stream:
            template = stream.read()
        return template
