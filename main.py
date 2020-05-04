"""
This program was created to run a reverse proxy.
"""

import sys
from http.server import HTTPServer
import yaml
from parsers import global_parser
from handlers import http_server

if len(sys.argv) != 2:
    print('Please, pass the configuration file of this server.')
    sys.exit(0)

YAML_FILE = sys.argv[1]

with open(YAML_FILE) as f:
    YAML_FILE = yaml.load(f, Loader=yaml.FullLoader)

for config_node in YAML_FILE:
    if config_node == "main":
        PORT = YAML_FILE[config_node]['port']
    global_parser.GlobalParser().parse(config_node, YAML_FILE[config_node])

hostname = YAML_FILE['main']['hostname']
port = YAML_FILE['main']['port']

client_address = (hostname, port)
reverse_proxy = http_server.ReverseProxy(YAML_FILE)

httpd = HTTPServer(client_address, reverse_proxy)

try:
    print('Serving in ', port)
    httpd.serve_forever()
except RuntimeError:
    httpd.shutdown()
