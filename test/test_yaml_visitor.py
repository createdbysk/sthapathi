import pytest
import sthapathi.yaml_visitor


class TestYamlVisitor(object):
    @pytest.fixture
    def yaml_visitor(self):
        return sthapathi.yaml_visitor.YamlVisitor()

    def test_visit_mapping(self, yaml_visitor):
        # Given
        element = None

        # Then
        with pytest.raises(NotImplementedError):
            # When
            yaml_visitor.visit_mapping(element)

    def test_visit_sequence(self, yaml_visitor):
        # Given
        element = None

        # Then
        with pytest.raises(NotImplementedError):
            # When
            yaml_visitor.visit_sequence(element)
