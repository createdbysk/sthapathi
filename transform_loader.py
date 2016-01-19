import importlib
import trace_logging


class TransformLoader(object):
    def __init__(self, path_resolver):
        self._logger = trace_logging.getLogger(self.__module__)
        self._path_resolver = path_resolver

    def load_transform(self, provider, resource):
        transform_module = self._path_resolver.resolve_transform_path(provider, resource)
        transform = importlib.import_module(transform_module)
        return transform
