import sys
import os

sys.path.append(os.path.abspath("../src"))

import sthapathi.configuration_reader

for element in sthapathi.configuration_reader.read_configuration(os.path.abspath(os.path.dirname(__file__))):
    print(element)
