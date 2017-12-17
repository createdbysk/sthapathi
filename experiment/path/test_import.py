import sys
import os

current_dir = os.path.dirname(__file__)
root_dir = os.path.abspath(os.path.dirname(os.path.dirname(current_dir)))
modules_dir = os.path.join(root_dir, "transforms")

sys.path.append(modules_dir)

import aws.network

apply_transform = aws.network.apply_transform

