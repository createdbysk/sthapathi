import pytest
import sthapathi.catalog_yaml_visitor

@pytest.mark.skip(reason="Temporary to allow development of yaml_validator. Some code here will migrate to the test"
                         "for that mechanism.")
class TestCatalogYamlVisitor(object):
    @pytest.fixture
    def catalog_yaml_visitor(self):
        self.__catalog = {}
        return sthapathi.catalog_yaml_visitor.CatalogYamlVisitor(self.__catalog)

    def test_visit_mapping_empty_catalog_then_raise_exception(self, catalog_yaml_visitor):
        # Given
        element = {}

        # Then
        with pytest.raises(sthapathi.catalog_yaml_visitor.CatalogYamlVisitorError):
            # When
            catalog_yaml_visitor.visit_mapping(element)

    def test_visit_mapping_given_empty_providers_then_raise_exception(self, catalog_yaml_visitor):
        # Given
        element = {
            "providers": {}
        }

        # Then
        with pytest.raises(sthapathi.catalog_yaml_visitor.CatalogYamlVisitorError):
            # When
            catalog_yaml_visitor.visit_mapping(element)

    def test_visit_mapping_given_providers_is_not_mapping_then_raise_exception(self, catalog_yaml_visitor):
        # Given
        element = {
            "providers": []
        }

        # Then
        with pytest.raises(sthapathi.catalog_yaml_visitor.CatalogYamlVisitorError):
            # When
            catalog_yaml_visitor.visit_mapping(element)

    def test_visit_mapping_given_provider_is_not_mapping_then_raise_exception(self, catalog_yaml_visitor):
        # Given
        element = {
            "providers": {
                "provider": []
            }
        }

        # Then
        with pytest.raises(sthapathi.catalog_yaml_visitor.CatalogYamlVisitorError):
            # When
            catalog_yaml_visitor.visit_mapping(element)

    def test_visit_mapping_given_element_does_not_have_source_then_raise_exception(self, catalog_yaml_visitor):
        # Given
        element = {
            "providers": {
                "provider": {
                    "element": {}
                }
            }
        }

        # Then
        with pytest.raises(sthapathi.catalog_yaml_visitor.CatalogYamlVisitorError):
            # When
            catalog_yaml_visitor.visit_mapping(element)

    def test_visit_mapping_given_argument_group_is_not_a_sequence_then_raise_exception(self, catalog_yaml_visitor):
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
        with pytest.raises(sthapathi.catalog_yaml_visitor.CatalogYamlVisitorError):
            # When
            catalog_yaml_visitor.visit_mapping(element)

    def test_visit_mapping_given_arguments_is_not_a_sequence_then_raise_exception(self, catalog_yaml_visitor):
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
        with pytest.raises(sthapathi.catalog_yaml_visitor.CatalogYamlVisitorError):
            # When
            catalog_yaml_visitor.visit_mapping(element)

    def test_visit_mapping_given_element_has_unknown_argument_group_then_raise_exception(self, catalog_yaml_visitor):
        # Given
        element = {
            "providers": {
                "provider": {
                    "element": {
                        "source": "./module/element",
                        "argument_groups": ["Unknown"]
                    }
                }
            }
        }

        # Then
        with pytest.raises(sthapathi.catalog_yaml_visitor.CatalogYamlVisitorError):
            # When
            catalog_yaml_visitor.visit_mapping(element)

    def test_visit_mapping_given_argument_groups_is_not_a_mapping_then_raise_exception(self, catalog_yaml_visitor):
        # Given
        element = {
            "providers": {
                "provider": {
                    "element": {
                        "source": "./module/element"
                    }
                }
            },
            "argument_groups": []
        }

        # Then
        with pytest.raises(sthapathi.catalog_yaml_visitor.CatalogYamlVisitorError):
            # When
            catalog_yaml_visitor.visit_mapping(element)


    def test_visit_mapping_given_a_argument_group_is_neither_sequence_nor_mapping_then_raise_exception(self, catalog_yaml_visitor):
        # Given
        element = {
            "providers": {
                "provider": {
                    "element": {
                        "source": "./module/element"
                    }
                }
            },
            "argument_groups": {
                "argument_group": "Invalid"
            }
        }

        # Then
        with pytest.raises(sthapathi.catalog_yaml_visitor.CatalogYamlVisitorError):
            # When
            catalog_yaml_visitor.visit_mapping(element)

    def test_visit_mapping_given_a_argument_group_mapping_has_no_arguments_key_then_raise_exception(self, catalog_yaml_visitor):
        # Given
        element = {
            "providers": {
                "provider": {
                    "element": {
                        "source": "./module/element"
                    }
                }
            },
            "argument_groups": {
                "argument_group": {
                }
            }
        }

        # Then
        with pytest.raises(sthapathi.catalog_yaml_visitor.CatalogYamlVisitorError):
            # When
            catalog_yaml_visitor.visit_mapping(element)

    def test_visit_mapping_given_a_argument_group_mapping_has_unknown_key_then_raise_exception(self, catalog_yaml_visitor):
        # Given
        element = {
            "providers": {
                "provider": {
                    "element": {
                        "source": "./module/element"
                    }
                }
            },
            "argument_groups": {
                "argument_group": {
                    "unknown_key": {}
                }
            }
        }

        # Then
        with pytest.raises(sthapathi.catalog_yaml_visitor.CatalogYamlVisitorError):
            # When
            catalog_yaml_visitor.visit_mapping(element)

    def test_visit_mapping_given_a_argument_group_arguments_is_not_a_sequence_then_raise_exception(self, catalog_yaml_visitor):
        # Given
        element = {
            "providers": {
                "provider": {
                    "element": {
                        "source": "./module/element"
                    }
                }
            },
            "argument_groups": {
                "argument_group": {
                    "arguments": {}
                }
            }
        }

        # Then
        with pytest.raises(sthapathi.catalog_yaml_visitor.CatalogYamlVisitorError):
            # When
            catalog_yaml_visitor.visit_mapping(element)

    def test_visit_mapping_given_a_argument_group_inherits_is_not_a_sequence_then_raise_exception(self, catalog_yaml_visitor):
        # Given
        element = {
            "providers": {
                "provider": {
                    "element": {
                        "source": "./module/element"
                    }
                }
            },
            "argument_groups": {
                "argument_group": {
                    "arguments": [],
                    "inherits": {}
                }
            }
        }

        # Then
        with pytest.raises(sthapathi.catalog_yaml_visitor.CatalogYamlVisitorError):
            # When
            catalog_yaml_visitor.visit_mapping(element)

    def test_visit_mapping_given_valid_providers_then_store_providers_in_catalog(self, catalog_yaml_visitor):
        # Given
        # NOTE: This element matches the example in the README.md
        element = {
            "providers": {
                "provider_name": {
                    "element_one": {
                        "source": "./modules/element_one",
                        "argument_groups": [
                            "argument_group_name1",
                            "argument_group_name2"
                        ],
                        "arguments": [
                            "argument_name11",
                            "argument_name12"
                        ]
                    },
                    "element_two": {
                        "source": "git::ssh://git.url/path/to/module/in/git",
                        "arguments": [
                            "argument_name21",
                            "argument_name22",
                            "argument_name23"
                        ]
                    }
                }
            },
            "argument_groups": {
                "argument_group_name1": {
                    "arguments": [
                        "argument_name31",
                        "argument_name32"
                    ],
                    "inherits": [
                        "argument_group_name3"
                    ]
                },
                "argument_group_name2": [
                    "argument_name41",
                    "argument_name42",
                    "argument_name43"
                ],
                "argument_group_name3": [
                    "argument_name51"
                ]
            }
        }
        expected_element = element

        # When
        catalog_yaml_visitor.visit_mapping(element)

        # Then
        assert self.__catalog == expected_element

    def test_visit_mapping_given_no_argument_groups_then_store_empty_argument_groups_in_catalog(self, catalog_yaml_visitor):
        # Given
        element = {
            "providers": {
                "aws": {
                    "element": {
                        "source": "./modules/test_module"
                    }
                }
            }
        }
        expected_element = {
            "providers": {
                "aws": {
                    "element": {
                        "source": "./modules/test_module"
                    }
                }
            },
            "argument_groups": {}
        }

        # When
        catalog_yaml_visitor.visit_mapping(element)

        # Then
        assert self.__catalog == expected_element

