import pytest


class TestValidator(object):
    @pytest.fixture
    def validator(self):
        import sthapathi.validator
        return sthapathi.validator.Validator()

    def test_validate(self, validator):
        # Given
        data = None

        # Then
        with pytest.raises(NotImplementedError):
            # When
            validator.validate(data)
