import mock
import path_resolver
import os
import tests.requirements
from nose.tools import assert_equal


class TestPathResolver(object):
    __BASE_DIR = "BASE_DIR"

    def __init__(self):
        self._path_resolver = None

    @mock.patch("path_resolver.os.path.dirname", autospec=True)
    def setup(self, dirname):
        dirname.return_value = TestPathResolver.__BASE_DIR
        self._path_resolver = path_resolver.PathResolver()

    def test_resolve_template_path(self):
        """
        GIVEN user specifies a resource named RESOURCE
        AND the user specifies a provider named PROVIDER
        WHEN the user runs sthapathi
        THEN sthapathi finds the template to generate the code for the resource under .sthapathi/templates/PROVIDER/RESOURCE
        """
        base_template_path = os.path.join(TestPathResolver.__BASE_DIR,
                                          tests.requirements.BASE_PATH,
                                          tests.requirements.TEMPLATES_PATH)
        provider = "PROVIDER"
        resource = "RESOURCE"
        extension = tests.requirements.TEMPLATE_EXTENSION
        expected_path = os.path.join(base_template_path, provider, resource) + os.path.extsep + extension
        resolved_path = self._path_resolver.resolve_template_path(provider, resource)
        assert_equal(expected_path, resolved_path)

    def test_resolve_transform_path(self):
        """
        GIVEN user specifies a resource named RESOURCE
        AND the user specifies a provider named PROVIDER
        AND RESOURCE has a transform associated with it
        WHEN the user runs sthapathi
        THEN sthapathi finds the apply_transform method in the module transforms.PROVIDER.RESOURCE
        """
        base_template_path = os.path.join(TestPathResolver.__BASE_DIR,
                                          tests.requirements.BASE_PATH,
                                          tests.requirements.TEMPLATES_PATH)
        transform_package = tests.requirements.TRANSFORMS_PATH
        provider = "PROVIDER"
        resource = "RESOURCE"
        expected_module = '%s.%s.%s' % (transform_package, provider, resource)
        resolved_module = self._path_resolver.resolve_transform_path(provider, resource)
        assert_equal(expected_module, resolved_module)
