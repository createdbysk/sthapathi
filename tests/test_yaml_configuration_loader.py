import mock
import yaml_configuration_loader
from nose.tools import assert_equal


@mock.patch("yaml.load_all", autospec=True)
def test_load_configuration(mock_yaml_load_all):
    """
    GIVEN a yaml file that is formatted as shown below to configure a network
    WHEN sthapathi loads the yaml file
    THEN sthapathi loads it in the representation ["name", "network", {"cidr_block": "<cidr_block>"}]

    yaml format for network:
    name:
    - network
    - cidr_block:<cidr_block>
    """
    stream = mock.Mock()
    mock_yaml_load_all.return_value = [{"name": ["resource", {"parameter": "value"}]}]
    expected_configuration = [["name", "resource", {"parameter": "value"}]]
    loaded_configuration = [configuration for configuration in yaml_configuration_loader.load_configuration(stream)]
    mock_yaml_load_all.assert_called_once_with(stream)
    assert_equal(expected_configuration, loaded_configuration)
