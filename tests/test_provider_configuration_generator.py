import mock
import provider_configuration_generator
from nose.tools import assert_equal


class TestProvideConfigurationGenerator(object):
    def __init__(self):
        self._provider_configuration_generator = None
        self._mock_template_loader = None
        self._mock_configuration_reader = None

    @mock.patch("configuration_reader.ConfigurationReader", autospec=True)
    @mock.patch("template_loader.TemplateLoader", autospec=True)
    def setup(self, template_loader_class, configuration_reader_class):
        self._mock_template_loader = template_loader_class.return_value
        self._mock_configuration_reader = configuration_reader_class.return_value
        self._provider_configuration_generator = \
            provider_configuration_generator.ProviderConfigurationGenerator(self._mock_template_loader,
                                                                            self._mock_configuration_reader)

    def test_generate_configuration(self):
        provider = 'PROVIDER'
        resource = 'RESOURCE'
        name = 'NAME'
        parameter = 'PARAMETER'
        value = 'VALUE'
        parameters = {parameter: value}
        configuration_parameters = [name, resource, parameters]
        self._mock_configuration_reader.read_type.return_value = resource
        self._mock_configuration_reader.read_name.return_value = name
        self._mock_configuration_reader.read_parameters.return_value = parameters
        template = '{{name}} {{%s}}' % (parameter,)
        self._mock_template_loader.load_template.return_value = template
        expected_configuration = '%s %s'%(name, value)
        generated_configuration = \
            self._provider_configuration_generator.generate_configuration(provider,
                                                                          configuration_parameters)
        self._mock_configuration_reader.read_name.assert_called_once_with(configuration_parameters)
        self._mock_configuration_reader.read_type.assert_called_once_with(configuration_parameters)
        self._mock_configuration_reader.read_parameters.assert_called_once_with(configuration_parameters)
        self._mock_template_loader.load_template.assert_called_once_with(provider, resource)
        assert_equal(expected_configuration, generated_configuration)
