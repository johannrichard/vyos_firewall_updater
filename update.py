#!/usr/bin/python

import argparse
import json
import socket

parser = argparse.ArgumentParser(description='Update firewall config')
parser.add_argument('--config', metavar='config_file', type=file, default="update_config.json",
                    help='path to the config file')

args = parser.parse_args()
config = json.load(args.config)
if len(config) == 0:
    exit(-1)

for groupName in config:
    print "set firewall group address-group %s" % groupName
    print "delete firewall group address-group %s address" % groupName
    ip_addresses = []
    for host in config[groupName]:
        try:
            ip = socket.gethostbyname(host)
            if not ip_addresses.__contains__(ip):
                ip_addresses.append(ip)
        except:
            pass
    for ip in ip_addresses:
        print "set firewall group address-group %s address '%s'" %(groupName, ip)
    print "commit"

