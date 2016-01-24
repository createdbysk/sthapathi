import mock
import provider_configuration_generator
from nose.tools import assert_equal


class TestProvideConfigurationGenerator(object):
    def __init__(self):
        self._provider_configuration_generator = None
        self._mock_template_loader = None
        self._mock_transform_loader = None
        self._mock_configuration_reader = None

    # These annotations will populate the parameters in the reverse order of occurrence of the annotations.
    @mock.patch("configuration_reader.ConfigurationReader", autospec=True)
    @mock.patch("transform_loader.TransformLoader", autospec=True)
    @mock.patch("template_loader.TemplateLoader", autospec=True)
    def setup(self, template_loader_class, transform_loader_class, configuration_reader_class):
        self._mock_template_loader = template_loader_class.return_value
        self._mock_transform_loader = transform_loader_class.return_value
        self._mock_configuration_reader = configuration_reader_class.return_value
        self._provider_configuration_generator = \
            provider_configuration_generator.ProviderConfigurationGenerator(self._mock_template_loader,
                                                                            self._mock_transform_loader,
                                                                            self._mock_configuration_reader)

    def test_generate_configuration(self):
        provider = 'PROVIDER'
        resource = 'RESOURCE'
        name = 'NAME'
        parameter = 'PARAMETER'
        value = 'VALUE'
        optional_parameter = "OPTIONAL_PARAMETER"
        optional_value = "OPTIONAL_VALUE"
        parameters = {parameter: value}
        transformed_parameters = {parameter: value, optional_parameter: optional_value}
        configuration_parameters = [name, resource, parameters]
        self._mock_configuration_reader.read_type.return_value = resource
        self._mock_configuration_reader.read_name.return_value = name
        self._mock_configuration_reader.read_parameters.return_value = parameters
        template = '{{name}} {{%s}} {{#%s}}%s{{/%s}}' % (parameter, optional_parameter, optional_value,
                                                         optional_parameter)
        self._mock_template_loader.load_template.return_value = template

        # Mock the transform module
        class ModuleStub(object):
            @staticmethod
            def apply_transform(_):
                pass

        module_stub = ModuleStub()
        with mock.patch.object(module_stub, 'apply_transform', autospec=True) as mock_transform:
            self._mock_transform_loader.load_transform.return_value = module_stub
            mock_transform.return_value = transformed_parameters
            expected_configuration = '%s %s %s' % (name, value, optional_value)
            generated_configuration = \
                self._provider_configuration_generator.generate_configuration(provider,
                                                                              configuration_parameters)
            self._mock_configuration_reader.read_name.assert_called_once_with(configuration_parameters)
            self._mock_configuration_reader.read_type.assert_called_once_with(configuration_parameters)
            self._mock_configuration_reader.read_parameters.assert_called_once_with(configuration_parameters)
            mock_transform.assert_called_once_with(parameters)
            self._mock_template_loader.load_template.assert_called_once_with(provider, resource)
            self._mock_transform_loader.load_transform.assert_called_once_with(provider, resource)
            assert_equal(expected_configuration, generated_configuration)
