import sys
import os
import yaml
import json

sys.path.append(os.path.abspath("../src"))

import sthapathi.configuration_reader
import sthapathi.terraform_plugin

reader = sthapathi.configuration_reader.ConfigurationReader(os.path.abspath("configuration"))
plugin = sthapathi.terraform_plugin.TerraformPlugin()

with open("default_parameter_group.yaml", "r") as stream:
    default_parameter_group = yaml.load(stream)

additional_parameter_group = {
    "additional": {
        "variables": [
            "additional"
        ]
    }
}
additional_parameter_group.update(default_parameter_group)

with open("lambda_parameter_group.yaml", "r") as stream:
    lambda_parameter_group = yaml.load(stream)

additional_parameter_group.update(lambda_parameter_group)


target_configuration = plugin.generate_target_configuration("aws",
                                                            "sthapathi-component",
                                                            catalog_path=os.path.abspath("catalog.yaml"),
                                                            parameter_groups=additional_parameter_group,
                                                            configuration_reader=reader)


print(json.dumps(target_configuration, indent=4))
