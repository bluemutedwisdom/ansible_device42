#!/usr/bin/env python

import argparse
import sys
from lib import *

try:
    import json
except ImportError:
    import simplejson as json

class Inventory(object):

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action='store_true')
        self.args = parser.parse_args()

        # Called with `--list`.
        if self.args.list:
            self.inventory = self.inventory()
        # Called with `--host [hostname]`.
        # If no groups or vars are present, return an empty inventory.
        else:
            self.inventory = self.empty_inventory()

        print json.dumps(self.inventory)

    def inventory(self):
        conf = get_conf()
        ansible = Ansible(conf)
        groups = ansible.get_grouping(Device42(conf).doql())
        groups['_meta'] = {'hostvars': {}}
        return groups

    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}

Inventory()
