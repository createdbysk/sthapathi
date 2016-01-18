import importlib
from nose.tools import assert_equal
import tests.utilities


class TestAwsNetworkTransform(object):
    def __init__(self):
        self._aws_network_transform = None

    def setup(self):
        transform_module = tests.utilities.get_transform_module('aws', 'network')
        self._aws_network_transform = importlib.import_module(transform_module)

    def test_apply_transform_enable_dns_support_set_to_true(self):
        """
        GIVEN configuration parameters has enable_dns_support
        WHEN apply_transform runs on the configuration parameters
        THEN enable_dns_support is unchanged
        """
        # GIVEN
        configuration_parameters = {
            'cidr_block': '10.10.0.0/16',
            'enable_dns_support': True
        }
        expected_transformed_parameters = configuration_parameters

        # WHEN
        transformed_parameters = self._aws_network_transform.apply_transform(configuration_parameters)

        # THEN
        assert_equal(expected_transformed_parameters, transformed_parameters)

    def test_apply_transform_enable_dns_support_set_to_false(self):
        """
        GIVEN configuration parameters has enable_dns_support
        WHEN apply_transform runs on the configuration parameters
        THEN enable_dns_support is unchanged
        """
        # GIVEN
        configuration_parameters = {
            'cidr_block': '10.10.0.0/16',
            'enable_dns_support': False
        }
        expected_transformed_parameters = configuration_parameters

        # WHEN
        transformed_parameters = self._aws_network_transform.apply_transform(configuration_parameters)

        # THEN
        assert_equal(expected_transformed_parameters, transformed_parameters)

    def test_apply_transform_enable_dns_support_not_present(self):
        """
        GIVEN configuration parameters does not have enable_dns_support
        WHEN apply_transform runs on the configuration parameters
        THEN the result has enable_dns_support set to True
        """
        # GIVEN
        configuration_parameters = {
            'cidr_block': '10.10.0.0/16'
        }
        expected_transformed_parameters = {
            'cidr_block': '10.10.0.0/16',
            'enable_dns_support': True
        }

        # WHEN
        transformed_parameters = self._aws_network_transform.apply_transform(configuration_parameters)

        # THEN
        assert_equal(expected_transformed_parameters, transformed_parameters)
