"""
This program was created to run a reverse proxy.
"""

import sys
import yaml
from parsers import global_parser

if len(sys.argv) != 2:
    print('Please, pass the configuration file of this server.')
    sys.exit(0)

YAML_FILE = sys.argv[1]

with open(YAML_FILE) as f:
    YAML_FILE = yaml.load(f, Loader=yaml.FullLoader)

for config_node in YAML_FILE:
    global_parser.GlobalParser().parse(config_node, YAML_FILE[config_node])
