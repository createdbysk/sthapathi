import mock
from nose.tools import assert_equal

import trace_logging
import transform_loader


class TestTransformLoader(object):
    def __init__(self):
        self._mock_path_resolver = None
        self._mock_trace = None
        self._mock_import_module = None
        self._transform_loader = None

    @mock.patch("transform_loader.importlib.import_module", autospec=True)
    @mock.patch("path_resolver.PathResolver", autospec=True)
    def setup(self, path_resolver_class, import_module):
        # Get access to the mock class instance
        self._mock_path_resolver = path_resolver_class.return_value
        # Mock the importlib.import_module() to verify the call to it.
        self._mock_import_module = import_module
        self._transform_loader = transform_loader.TransformLoader(self._mock_path_resolver, self._mock_import_module)
        # Mock the trace method. This does NOT work as a decorator.
        self._mock_trace = mock.patch.object(trace_logging.getLogger("transform_loader"), "trace").start()

    def teardown(self):
        self._transform_loader = None
        # Restore the original trace method.
        self._mock_trace.stop();

    def test_load_transform_given_transform_when_load_transform_then_return_transform(self):
        """
        GIVEN the name of the resource and the provider
        AND the resource has a transform
        WHEN sthapathi invokes the transform loader with the name of the resource
        THEN the template loader loads the transform corresponding to the resource.
        """
        # GIVEN
        provider = 'provider'
        resource = 'resource'
        transform_module = 'transforms.provider.resource'
        expected_transform = 'transform'
        self._mock_path_resolver.resolve_transform_path.return_value = transform_module
        self._mock_import_module.return_value = expected_transform

        # WHEN
        transform = self._transform_loader.load_transform(provider, resource)

        # THEN
        self._mock_path_resolver.resolve_transform_path.assert_called_once_with(provider, resource)
        self._mock_import_module.assert_called_once_with(transform_module)
        assert_equal(expected_transform, transform)
        self._mock_trace.assert_any_call("load_transform(%s, %s)", provider, resource)
        self._mock_trace.assert_any_call("load_transform(%s, %s) - import_module(%s)",
                                         provider, resource, transform_module)

    def test_load_transform_given_no_transform_when_load_transform_then_return_identity(self):
        """
        GIVEN the name of the resource and the provider
        AND the resource does not have a transform
        WHEN sthapathi invokes the transform loader with the name of the resource
        THEN the template loader returns the identity transform.
        """
        # GIVEN
        provider = 'provider'
        resource = 'resource'
        transform_module = 'transforms.provider.resource'
        value_to_transform = 'identity'
        self._mock_path_resolver.resolve_transform_path.return_value = transform_module
        self._mock_import_module.side_effect = ImportError()

        # WHEN
        transform = self._transform_loader.load_transform(provider, resource)

        # THEN
        # The returned transform is an identity transform.
        transformed_value = transform.apply_transform(value_to_transform)
        assert_equal(value_to_transform, transformed_value)
        self._mock_path_resolver.resolve_transform_path.assert_called_once_with(provider, resource)
        self._mock_import_module.assert_called_once_with(transform_module)
        self._mock_trace.assert_any_call("load_transform(%s, %s)", provider, resource)
        self._mock_trace.assert_any_call("load_transform(%s, %s) - import_module(%s)",
                                         provider, resource, transform_module)
