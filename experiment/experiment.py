import sys
import os
import yaml
import json

sys.path.append(os.path.abspath("../src"))

import sthapathi.configuration_reader
import sthapathi.terraform_plugin
import sthapathi.parameter_group_reader

reader = sthapathi.configuration_reader.ConfigurationReader(os.path.abspath("configuration"))
plugin = sthapathi.terraform_plugin.TerraformPlugin()

additional_parameter_group = {
    "additional": {
        "variables": [
            "additional"
        ]
    }
}

parameter_groups = sthapathi.parameter_group_reader.read(os.path.abspath("parameter_groups"))
parameter_groups.update(additional_parameter_group)

target_configuration = plugin.generate_target_configuration("aws",
                                                            "sthapathi-component",
                                                            catalog_path=os.path.abspath("catalog.yaml"),
                                                            parameter_groups=parameter_groups,
                                                            configuration_reader=reader)


print(json.dumps(target_configuration, indent=4))
