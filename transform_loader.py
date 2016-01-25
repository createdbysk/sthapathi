import importlib

import exceptions

import trace_logging


class TransformLoader(object):
    class IdentityTransform(object):
        """
        Return this class as the identity transform when a resource does not have an associated transform.
        """
        @staticmethod
        def apply_transform(value):
            """
            Identity, which just returns the original value.
            :param value: The value, which this function will return unmodified
            :return: The value.
            """
            return value

    def __init__(self, path_resolver, import_module=importlib.import_module):
        self._logger = trace_logging.getLogger(self.__module__)
        self._path_resolver = path_resolver
        self._import_module = import_module
        self._identity_transform = TransformLoader.IdentityTransform

    def load_transform(self, provider, resource):
        """
        GIVEN user specifies a resource named RESOURCE
        AND the user specifies a provider named PROVIDER
        AND RESOURCE has a transform associated with it
        WHEN the user runs sthapathi
        THEN sthapathi finds the apply_transform method in the module transforms.PROVIDER.RESOURCE

        GIVEN the name of the resource and the provider
        AND the resource does not have a transform
        WHEN sthapathi invokes the transform loader with the name of the resource
        THEN the template loader returns the identity transform.

        :param provider: The PROVIDER
        :param resource: The RESOURCE
        :return: The module at transforms.PROVIDER.RESOURCE if it exists, identity transform otherwise.
        """
        self._logger.trace("load_transform(%s, %s)", provider, resource)
        transform_module = self._path_resolver.resolve_transform_path(provider, resource)
        self._logger.trace("load_transform(%s, %s) - import_module(%s)", provider, resource, transform_module)
        try:
            transform = self._import_module(transform_module)
        except ImportError:
            return self._identity_transform
        return transform
