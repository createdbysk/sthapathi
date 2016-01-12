import configuration_reader
import provider_configuration_generator
import template_loader
import path_resolver
import yaml_configuration_loader

resolver = path_resolver.PathResolver()
loader = template_loader.TemplateLoader(resolver)
reader = configuration_reader.ConfigurationReader()
generator = provider_configuration_generator.ProviderConfigurationGenerator(loader, reader)

with open("network.yaml", 'r') as stream:
    for configuration in yaml_configuration_loader.load_configuration(stream):
        generated_configuration = generator.generate_configuration("aws", configuration)
        print generated_configuration
