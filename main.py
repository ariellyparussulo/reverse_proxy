import sys
import yaml
from parsers import globalParser

global configFile

if len(sys.argv) is not 2:
    print('Please, pass the configuration file of this server.')
    sys.exit(0)

configFile = sys.argv[1]

with open(configFile) as f:
    configFile = yaml.load(f, Loader=yaml.FullLoader)

for configNode in configFile:
    globalParser.GlobalParser().parse(configNode, configFile[configNode])
    print(configFile[configNode])

