import sys
import yaml

global configFile

if len(sys.argv) is not 2:
    print('Please, pass the configuration file of this server.')
    sys.exit(0)

CONFIG_FILE_PATH = sys.argv[1]

with open(CONFIG_FILE_PATH) as f:
    configFile = yaml.load(f, Loader=yaml.FullLoader)

print("data %s" % configFile)

