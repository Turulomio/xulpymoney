#!/usr/bin/python3
import sys
sys.path.append("/usr/lib/xulpymoney")
from libxulpymoney import *
from libsources import *

mem=MemProducts()
mem.init__script('Yahoo Intraday Updater')

cur=mem.con.cursor()
cur.execute("select count(*) from products where active=true and priority[1]=1")
num=cur.fetchone()[0]
print ("Products",  num)
step=150
for i in range (0, int(num/step)+1):
    w=WorkerYahoo(mem, "select * from products where active=true and priority[1]=1 order by ticker limit {} offset {};".format(step, step*i))
    w.run()
cur.close()
mem.disconnect(mem.con)
