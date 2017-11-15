# -*-coding:utf-8-*-
# Author: alphadl
# read_mdb.py 2017/8/25 00:49
import pypyodbc

try:
    conn = pypyodbc.connect('Driver=MDBTools;DBQ=zhaiyao.mdb', unicode_results=False)
    # conn = pypyodbc.connect('Driver=MDBTools;DBQ=zhaiyao.mdb')

except pypyodbc.Error as ex:
    sqlstate = ex.args[1]
    print(sqlstate)

com = '"SELECT F_Abstract,F_EngAbstrict,qk_flh,qk_CN From lunwen WHERE F_Abstract IS NOT NULL AND F_EngAbstrict IS NOT NULL"'
cur = conn.cursor().execute('SELECT F_Abstract,F_EngAbstrict,qk_flh,qk_CN,f_clcnumber From lunwen')
# print cur[0].decode('utf-8')
# cur.execute(com)
#
count=0
real_count=0
for row in cur.fetchall():
    count+=1
        real_count+=1
        if len(row)!=5:
            print row
        # for col in row:
        #     print col,

        # print ''

print real_count,count
conn.close()
