#!/usr/bin/python3

import os, sys, configparser, itertools
import boto3

config = configparser.ConfigParser()
with open('backup.conf') as fp:
  config.read_file(itertools.chain(['[global]'], fp), source='backup.conf')

filename = sys.argv[1]

bucket = config['global']['S3_BUCKET'].replace("\"","").replace("'","")
path = config['global']['S3_PATH'].replace("\"","").replace("'","") + '/' + filename

s3 = boto3.resource('s3')
s3.Object(bucket, path).put(Body=open('./tmp/' + filename, 'rb'))
