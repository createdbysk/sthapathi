import path_resolver
import os
from nose.tools import assert_equal

class TestPathResolver(object):
    def __init__(self):
        self._path_resolver = None

    def setup(self):
        self._path_resolver = path_resolver.PathResolver()

    def test_resolve_path(self):
        """
        GIVEN user specifies a resource named RESOURCE
        AND the user specifies a provider named PROVIDER
        WHEN the user runs sthapathi
        THEN sthapathi finds the template to generate the code for the resource under .sthapathi/templates/PROVIDER/RESOURCE
        """
        base_template_path = os.path.join(".sthapathi", "templates")
        provider = "PROVIDER"
        resource = "RESOURCE"
        expected_path = os.path.join(base_template_path, provider, resource)
        resolved_path = self._path_resolver.resolve_template_path(provider, resource)
        assert_equal(expected_path, resolved_path)
