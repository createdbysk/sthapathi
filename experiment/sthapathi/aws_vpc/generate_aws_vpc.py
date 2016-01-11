import yaml
import configuration_reader
import provider_configuration_generator
import template_loader
import path_resolver

resolver = path_resolver.PathResolver()
loader = template_loader.TemplateLoader(resolver)
reader = configuration_reader.ConfigurationReader()
generator = provider_configuration_generator.ProviderConfigurationGenerator(loader, reader)

with open("network.yaml", 'r') as stream:
    configuration = yaml.load(stream)
    for name, params in configuration.iteritems():
        parameters = [name]
        parameters.extend(params)
        generated_configuration = generator.generate_configuration("aws", parameters)
        print generated_configuration
