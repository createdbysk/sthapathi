import mock
import template_loader
import trace_logging
from nose.tools import *


class TestTemplateLoader(object):
    def __init__(self):
        self._expected_template = """resource "example" "name" {
    property1 = "value1"
    property2 = "value2"
}"""
        self._resource = "RESOURCE"
        self._provider = "PROVIDER"
        self._template_path = "path/to/template"
        self._template_loader = None
        self._mock_logging = None
        self._mock_trace = None

    @mock.patch("path_resolver.PathResolver")
    def setup(self, path_resolver_class):
        # Get access to the mock class instance
        path_resolver = path_resolver_class.return_value
        # Set the return value from the PathResolver.resolve_path method.
        path_resolver.resolve_path.return_value = self._template_path
        self._template_loader = template_loader.TemplateLoader(path_resolver_class)
        # Mock the trace method. This does NOT work as a decorator.
        self._mock_trace = mock.patch.object(trace_logging.getLogger("template_loader"), "trace").start()

    def teardown(self):
        self._template_loader = None
        # Restore the original trace method.
        self._mock_trace.stop();

    def test_load_template(self):
        """
        GIVEN the name of the resource and the provider
        WHEN sthapathi invokes the template loader with the name of the resource
        AND the resource is valid
        THEN the template loader loads the template corresponding to the resource.
        :param mock_logging: Mock instance of the logging module.
        """
        # Documentation for mock_open - https://docs.python.org/dev/library/unittest.mock.html#mock-open
        # Mock the open in the template_loader module.
        # mock_open creates the mock for open.
        # The read_data value is returned on the call to the read() on the stream returned by open().
        mock_open = mock.mock_open(read_data=self._expected_template)
        # This patch call patches the open in the template_loader module with the mock open.
        with mock.patch("template_loader.open", mock_open):
            template = self._template_loader.load_template(self._provider, self._resource)
            mock_open.assert_called_once_with(self._template_path, 'r')
            assert_equal(self._expected_template, template)
            self._mock_trace.assert_any_call("load_template(%s, %s)", self._provider, self._resource)
            self._mock_trace.assert_any_call("load_template(%s, %s) - read template from %s",
                                                       self._provider, self._resource, self._template_path)
