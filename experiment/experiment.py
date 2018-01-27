import sys
import os
import yaml

sys.path.append(os.path.abspath("../src"))

import sthapathi.configuration_reader
import sthapathi.terraform_plugin

reader = sthapathi.configuration_reader.ConfigurationReader(os.path.abspath("configuration"))
plugin = sthapathi.terraform_plugin.TerraformPlugin()

with open("default_parameter_group.yaml", "r") as stream:
    default_parameter_group = yaml.load(stream)

component_parameter_group = {
    "component": {
        "component": "network"
    }
}
component_parameter_group.update(default_parameter_group)

target_configuration = plugin.generate_target_configuration("aws",
                                                            catalog_path=os.path.abspath("catalog.yaml"),
                                                            parameter_groups=component_parameter_group,
                                                            configuration_reader=reader)

print(target_configuration)
