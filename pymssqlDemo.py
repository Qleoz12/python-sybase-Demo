import pymssql

print(pymssql)

server="172.16.123.68"
database="asiqpre"
port="2890"
user="llsanchez"
password="muv5M+rQ2pDYr&*+"

conn =pymssql.connect(server=server+":"+port,user=user,password=password,database=database, conn_properties='')
print(conn)
cursor = conn.cursor()
cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
row = cursor.fetchone()
while row:
    print("ID=%d, Name=%s" % (row[0], row[1]))
    row = cursor.fetchone()
conn.close()