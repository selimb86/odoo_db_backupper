#!/usr/bin/python3

import sys
import odoorpc

hostname = sys.argv[1]
port = sys.argv[2] 
master_pwd = sys.argv[3]
dbname = sys.argv[4]
filename = sys.argv[5]

odoo = odoorpc.ODOO(hostname, port=port)

dump = odoo.db.dump(master_pwd, dbname)

with open('./tmp/' + filename, 'wb') as dump_zip:
    dump_zip.write(dump.read())
