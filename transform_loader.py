import importlib
import trace_logging


class TransformLoader(object):
    def __init__(self, path_resolver, import_module=importlib.import_module):
        self._logger = trace_logging.getLogger(self.__module__)
        self._path_resolver = path_resolver
        self._import_module = import_module

    def load_transform(self, provider, resource):
        """
        GIVEN user specifies a resource named RESOURCE
        AND the user specifies a provider named PROVIDER
        AND RESOURCE has a transform associated with it
        WHEN the user runs sthapathi
        THEN sthapathi finds the apply_transform method in the module transforms.PROVIDER.RESOURCE

        :param provider: The PROVIDER
        :param resource: The RESOURCE
        :return: The module at transforms.PROVIDER.RESOURCE
        """
        self._logger.trace("load_transform(%s, %s)", provider, resource)
        transform_module = self._path_resolver.resolve_transform_path(provider, resource)
        self._logger.trace("load_transform(%s, %s) - import_module(%s)", provider, resource, transform_module)
        transform = self._import_module(transform_module)
        return transform
