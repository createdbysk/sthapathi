import os
import tests.requirements


def get_template_path(provider, resource):
    """
    Get the path to the template given the provider and the resource
    :param provider: The provider
    :param resource: The resource
    :return: The path
    """
    templates_base_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                       "..",
                                                       tests.requirements.BASE_PATH,
                                                       tests.requirements.TEMPLATES_PATH))
    template_filename = resource + os.path.extsep + tests.requirements.TEMPLATE_EXTENSION
    template_path = os.path.join(templates_base_path, provider, template_filename)
    return template_path


def get_transform_module(provider, resource):
    """
    Get the module that implements the transform for a resource given the provider and the resource.
    :param provider: The provider
    :param resource: The resource
    :return: The name of the module that implements the resource.
    """

    module_name = "%s.%s.%s"%(tests.requirements.TRANSFORMS_PATH, provider, resource)
    return module_name
