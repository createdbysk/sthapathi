import pytest
import pykwalify.errors


class TestCatalogValidator(object):
    @pytest.fixture
    def catalog_validator(self):
        import sthapathi.catalog_validator
        return sthapathi.catalog_validator.CatalogValidator()

    def test_validate_empty_catalog_then_raise_exception(self, catalog_validator):
        # Given
        element = {}

        # Then
        with pytest.raises(pykwalify.errors.SchemaError):
            # When
            catalog_validator.validate(element)

    def test_validate_given_empty_providers_then_raise_exception(self, catalog_validator):
        # Given
        element = {
            "providers": {}
        }

        # Then
        with pytest.raises(pykwalify.errors.SchemaError):
            # When
            catalog_validator.validate(element)

    def test_validate_given_providers_is_not_mapping_then_raise_exception(self, catalog_validator):
        # Given
        element = {
            "providers": []
        }

        # Then
        with pytest.raises(pykwalify.errors.SchemaError):
            # When
            catalog_validator.validate(element)

    def test_validate_given_provider_is_not_mapping_then_raise_exception(self, catalog_validator):
        # Given
        element = {
            "providers": {
                "provider": "invalid"
            }
        }

        # Then
        with pytest.raises(pykwalify.errors.SchemaError):
            # When
            catalog_validator.validate(element)

    def test_validate_given_element_does_not_have_source_then_raise_exception(self, catalog_validator):
        # Given
        element = {
            "providers": {
                "provider": {
                    "element": {}
                }
            }
        }

        # Then
        with pytest.raises(pykwalify.errors.SchemaError):
            # When
            catalog_validator.validate(element)

    def test_validate_given_argument_group_is_not_a_sequence_then_raise_exception(self, catalog_validator):
        # Given
        element = {
            "providers": {
                "provider": {
                    "element": {
                        "source": "./module/element",
                        "argument_groups": "not_a_sequence"
                    }
                }
            }
        }

        # Then
        with pytest.raises(pykwalify.errors.SchemaError):
            # When
            catalog_validator.validate(element)

    def test_validate_given_argumens_is_not_a_sequence_then_raise_exception(self, catalog_validator):
        # Given
        element = {
            "providers": {
                "provider": {
                    "element": {
                        "source": "./module/element",
                        "arguments": "not_a_sequence"
                    }
                }
            }
        }

        # Then
        with pytest.raises(pykwalify.errors.SchemaError):
            # When
            catalog_validator.validate(element)

