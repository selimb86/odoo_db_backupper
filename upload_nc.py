#!/usr/bin/python3

import os, sys, configparser, itertools
import owncloud

config = configparser.ConfigParser()
with open('backup.conf') as fp:
  config.read_file(itertools.chain(['[global]'], fp), source='backup.conf')

filename = sys.argv[1]

hostname = config['global']['NC_HOSTNAME'].replace("\"","").replace("'","")
username = config['global']['NC_USER'].replace("\"","").replace("'","")
password = config['global']['NC_PWD'].replace("\"","").replace("'","")
path = config['global']['NC_PATH'].replace("\"","").replace("'","")

oc = owncloud.Client(hostname)
oc.login(username, password)
oc.put_file_contents(path + filename, open('./tmp/' + filename, 'rb'))
