# -*- coding: UTF-8 -*-
from mod_python import util
from core import *
from xul import *

def index(req):
    form=util.FieldStorage(req)    

    con=Conection()
    cd=ConectionDirect()


    if form.has_key('year') and form.has_key('month'):
       year=int(form['year'])
       month=int(form['month'])
    else:
       year=datetime.date.today().year
       month=datetime.date.today().month
    
    req.content_type="application/vnd.mozilla.xul+xml"
    req.write(xulheaderwindowmenu("Xulpymoney > Informes > Conceptos > Estudio mensual"))
    arrG=[]
    arrI=[]

    req.write('<vbox align="center">\n')
    req.write('    <label id="titulo"  value="Estudio mensual por conceptos" />\n')
    req.write('</vbox>\n')
    req.write('<vbox flex="1" >\n')

    sql="select concepto, sum (importe) as suma from opercuentastarjetas, conceptos where conceptos.id_conceptos=opercuentastarjetas.id_conceptos and date_part('year',fecha) = "+str(year)+" and date_part('month',fecha)="+str(month)+" and opercuentastarjetas.id_tiposoperaciones=1 group by conceptos.concepto order by suma"
    curs=cd.con.Execute(sql); 

    while not curs.EOF:
        row = curs.GetRowAssoc(0)   
        arrG.append((utf82xul(row['concepto']), float(round(row['suma'], 2))))
        curs.MoveNext()     
    curs.Close()
    
    sql="select concepto, sum (importe) as suma from opercuentastarjetas, conceptos where conceptos.id_conceptos=opercuentastarjetas.id_conceptos and date_part('year',fecha) ="+str(year)+" and date_part('month',fecha)="+str(month)+" and opercuentastarjetas.id_tiposoperaciones=2 group by conceptos.concepto order by suma desc"
    
    curs=cd.con.Execute(sql);
    
    while not curs.EOF:
        row = curs.GetRowAssoc(0)
        arrI.append((utf82xul(row['concepto']), float(round(row['suma'], 2))))
        curs.MoveNext()
    curs.Close()
    
    
    gastos=Total().grafico_concepto_mensual("gg",arrG)
    ingresos=Total().grafico_concepto_mensual("gi",arrI)
    con.close()

    req.write('        <tabbox orient="vertical" flex="1"  style="overflow: auto;">\n')
    req.write('            <tabs>\n')
    req.write('                <tab label="Gastos" />\n')
    req.write('                <tab label="Ingresos" />\n')
    req.write('            </tabs>\n')
    req.write('            <tabpanels flex="1">\n')
    req.write('                <vbox  style="overflow: auto;">\n')
    req.write(gastos)
    req.write('                </vbox>\n')
    req.write('                <vbox  style="overflow: auto;">\n')
    req.write(ingresos)
    req.write('                </vbox>\n')
    req.write('            </tabpanels>\n')
    req.write('         </tabbox>\n')

    req.write('</vbox>\n')
    req.write('</window>\n')
