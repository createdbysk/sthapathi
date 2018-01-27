import sys
import os

sys.path.append(os.path.abspath("../src"))

import sthapathi.configuration_reader
import sthapathi.terraform_plugin

reader = sthapathi.configuration_reader.ConfigurationReader(os.path.abspath("configuration"))
plugin = sthapathi.terraform_plugin.TerraformPlugin()

target_configuration = plugin.generate_target_configuration("aws",
                                                            catalog_path=os.path.abspath("catalog.yaml"),
                                                            configuration_reader=reader)

print(target_configuration)
