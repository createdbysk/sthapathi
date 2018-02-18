import validator
from pykwalify.core import Core


class CatalogValidator(validator.Validator):
    def __init__(self):
        import os
        self.schema_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "schema/catalog_schema.yaml"))

    def validate(self, data):
        c = Core(source_data=data,
                 schema_files=[self.schema_path])
        c.validate(raise_exception=True)
