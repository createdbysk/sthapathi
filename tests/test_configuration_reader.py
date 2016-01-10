import configuration_reader
from nose.tools import assert_equal


class TestConfigurationReader(object):
    def __init__(self):
        self._configuration_reader = None

    def setup(self):
        self._configuration_reader = configuration_reader.ConfigurationReader()

    def test_configuration_reader(self):
        expected_resource = 'RESOURCE'
        expected_name = 'NAME'
        expected_parameters = {'parameter': 'value'}
        configuration_parameters = [expected_name, expected_resource, expected_parameters]
        resource = self._configuration_reader.read_type(configuration_parameters)
        name = self._configuration_reader.read_name(configuration_parameters)
        parameters = self._configuration_reader.read_parameters(configuration_parameters)
        assert_equal(expected_resource, resource)
        assert_equal(expected_name, name)
        assert_equal(expected_parameters, parameters)
