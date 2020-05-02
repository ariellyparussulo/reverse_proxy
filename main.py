"""
This program was created to run a reverse proxy.
"""

import sys
import yaml
import socket
import sys
from parsers import global_parser

if len(sys.argv) != 2:
    print('Please, pass the configuration file of this server.')
    sys.exit(0)

YAML_FILE = sys.argv[1]
HOST = ''
PORT = None

with open(YAML_FILE) as f:
    YAML_FILE = yaml.load(f, Loader=yaml.FullLoader)

for config_node in YAML_FILE:
    if config_node == "main":
        PORT = YAML_FILE[config_node]['port']
    global_parser.GlobalParser().parse(config_node, YAML_FILE[config_node])

server_address = (HOST, PORT)
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skt.bind(server_address)
skt.listen()
while True:
    conn, addr = skt.accept()
    print ('Client connected: ' + addr[0])

skt.close()