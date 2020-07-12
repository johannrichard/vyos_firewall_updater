import argparse
import json
import socket

parser = argparse.ArgumentParser(description='Update firewall config')
parser.add_argument('--config', metavar='config_file', type=file, default="config.json",
                    help='path to the config file')

args = parser.parse_args()
config = json.load(args.config)
if len(config) == 0:
    print "No groups found in config"
    exit(-1)

for groupName in config:
    ip_addresses = []
    for host in config[groupName]:
        ip = socket.gethostbyname(host)
        if not ip_addresses.__contains__(ip):
            ip_addresses.append(ip)
    print ("Setting group %s to contain: " % groupName)
    for ip in ip_addresses:
        print(ip)

