import sys
import yaml

if len(sys.argv) is not 2:
    print('Please, pass the configuration file of this server.')
    sys.exit(0)

CONFIG_FILE=sys.argv[1]

with open(CONFIG_FILE) as f:

    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)