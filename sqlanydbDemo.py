# ***************************************************************************
# Copyright (c) 2016 SAP SE or an SAP affiliate company. All rights reserved.
# ***************************************************************************
#######################################################################
# This sample code is provided AS IS, without warranty or liability
# of any kind.
# 
# You may use, reproduce, modify and distribute this sample code
# without limitation, on the condition that you retain the foregoing
# copyright notice and disclaimer as to the original code.
# 
#######################################################################
# 
# This sample program contains a hard-coded userid and password
# to connect to the demo database. This is done to simplify the
# sample program. The use of hard-coded passwords is strongly
# discouraged in production code.  A best practice for production
# code would be to prompt the user for the userid and password.
#
#######################################################################

import sqlanydb
import os

os.environ['SQLANY_API_DLL'] = 'C:\Program Files\SQL Anywhere 16\Bin64\dbcapi.dll'

server=""
database=""
port=""
user=""
password=""

#con = sqlanydb.connect(userid='dba', password='sql', dbn='iqdemo', dbf='iqdemo.db')
con=sqlanydb.connect(userid=user, pwd=password, servername='asiqpre1', host=server + ':' + port, dbn=database)
cur = con.cursor()
cur.execute('select top 10 *  from dba.cs_embargos_sp')
#assert cur.fetchone()[0] > 0
row= cur.fetchone()
while row:
    print( (row[0], row[1]))
    row = cur.fetchone()
con.close()
print('sqlanydb successfully installed.')


