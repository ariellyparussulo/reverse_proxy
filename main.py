import sys

print(sys.argv)

if len(sys.argv) is not 2:
    print('Please, pass the configuration file of this server.')
    sys.exit(0)

CONFIG_FILE=sys.argv[1]