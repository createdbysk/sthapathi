import pytest
import sthapathi.catalog_yaml_visitor

class TestCatalogYamlVisitor(object):
    @pytest.fixture
    def catalog_yaml_visitor(self):
        self.__catalog = {}
        return sthapathi.catalog_yaml_visitor.CatalogYamlVisitor(self.__catalog)

    def test_visit_mapping_empty_catalog_raises_exception(self, catalog_yaml_visitor):
        # Given
        element = {}

        # Then
        with pytest.raises(sthapathi.catalog_yaml_visitor.CatalogYamlVisitorError):
            # When
            catalog_yaml_visitor.visit_mapping(element)

    def test_visit_mapping_given_providers_then_store_providers_in_catalog(self, catalog_yaml_visitor):
        # Given
        element = {
            "providers": {
                "test_module": {
                    "source": "./modules/test_module"
                }
            }
        }

        # When
        catalog_yaml_visitor.visit_mapping(element)

        # Then
        assert self.__catalog == element
