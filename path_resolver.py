import os.path
import settings


class PathResolver(object):
    def __init__(self):
        self._base_path = os.path.join(os.path.dirname(__file__), settings.BASE_PATH, settings.TEMPLATES_PATH)

    def resolve_template_path(self, provider, resource):
        """
        GIVEN user specifies a resource named RESOURCE
        AND the user specifies a provider named PROVIDER
        WHEN the user runs sthapathi
        THEN sthapathi finds the template to generate the code for the resource under
            .sthapathi/templates/PROVIDER/RESOURCE

        :param provider: The resource provider
        :param resource: The resource
        :return: The path to the template for the resource.
        """
        resolved_path = os.path.join(self._base_path, provider, resource) + os.path.extsep + settings.TEMPLATE_EXTENSION
        return resolved_path
