import pystache
from nose.tools import assert_equal
import tests.utilities


class TestAwsNetworkTemplate(object):
    def __init__(self):
        self._template = None
        self._expected_name = None
        self._expected_cidr_block = None

    def setup(self):
        template_path = tests.utilities.get_template_path('aws', 'network')
        with open(template_path, 'r') as stream:
            self._template = stream.read()

    def test_required_parameters(self):
        expected_rendered = u"""{
    "resource": {
        "aws_vpc": {
            "network": {
                "cidr_block": "10.10.0.0/16"
            }
        }
    }
}
"""
        rendered = pystache.render(self._template, {'name': 'network', 'cidr_block': '10.10.0.0/16'})
        assert_equal(expected_rendered, rendered)

