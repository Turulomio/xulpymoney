#!/usr/bin/python3
import sys
sys.path.append("/usr/lib/xulpymoney")
from libxulpymoney import *
from libsources import *

mem=MemProducts()
mem.init__script('Mercado Continuo Updater')

w=WorkerMercadoContinuo(mem)
w.run()

mem.disconnect(mem.con)