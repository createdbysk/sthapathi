import os
import tests.requirements


def __templates_base_path():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                        "..",
                                        tests.requirements.BASE_PATH,
                                        tests.requirements.TEMPLATES_PATH))
    return path


def get_template_path(provider, resource):
    """
    Get the path to the template given the provider and the resource
    :param provider: The provider
    :param resource: The resource
    :return: The path
    """
    template_filename = resource + os.path.extsep + tests.requirements.TEMPLATE_EXTENSION
    template_path = os.path.join(__templates_base_path(), provider, template_filename)
    return template_path
