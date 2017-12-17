import configuration_reader
import provider_configuration_generator
import yaml_configuration_loader

reader = configuration_reader.ConfigurationReader()
generator = provider_configuration_generator.ProviderConfigurationGenerator(reader)

with open("network.yaml", 'r') as stream:
    for configuration in yaml_configuration_loader.load_configuration(stream):
        generated_configuration = generator.generate_configuration("aws", configuration)
        print generated_configuration
