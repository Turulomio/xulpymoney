# -*- coding: UTF-8 -*-
from mod_python import util
import time
from core import *
from xul import *

def index(req):
    #Consultas BD
    con=Conection()
    hoy=datetime.date.today()
    checked=""
    id_inversiones=0
    if form.has_key('id_inversiones'):
        id_inversiones=form['id_inversiones']
    
    cmbcuentas=Cuenta().cmb('id_cuentas','select * from cuentas where cu_activa=true order by cuenta',  0,  False)
    con.close()
    
    req.content_type="application/vnd.mozilla.xul+xml"
    req.write(xulheaderwindowmenu("Xulpymoney > Tarjeta > Nueva"))


    req.write('<script>\n')
    req.write('<![CDATA[\n')
         
    req.write('function tarjeta_insert(){\n')
    req.write('    var xmlHttp;\n')
    req.write('    xmlHttp=new XMLHttpRequest();\n')
    req.write('    xmlHttp.onreadystatechange=function(){\n')
    req.write('        if(xmlHttp.readyState==4){\n')
    req.write('            var ale=xmlHttp.responseText;\n')
    req.write('            location="tarjeta_listado.py";\n')
    req.write('        }\n')
    req.write('    }\n')
    req.write('    var id_cuentas = document.getElementById("id_cuentas").value;\n')
    req.write('    var tarjeta = document.getElementById("tarjeta").value;\n')
    req.write('    var numero = document.getElementById("numero").value;\n')
    req.write('    var pago_diferido = document.getElementById("pago_diferido").checked;\n')
    req.write('    var saldomaximo = document.getElementById("saldomaximo").value;\n')
    req.write('    var url="ajax/tarjeta_insertar.py?id_cuentas="+id_cuentas+"&tarjeta="+tarjeta+"&numero="+numero+"&pago_diferido="+pago_diferido+"&saldomaximo="+saldomaximo \n')
    req.write('    xmlHttp.open("GET",url,true);\n')
    req.write('    xmlHttp.send(null);\n')
    req.write('}\n')

    req.write(']]>\n')
    req.write('</script>\n')

    req.write('<vbox flex="1">\n')
    req.write('    <label id="titulo" flex="0" value="Nueva tarjeta" />\n')
    req.write('    <label value="" />\n')
    req.write('    <hbox flex="1">\n')
    req.write('    <grid align="center">\n')
    req.write('        <rows>\n')
    req.write('        <row><label value="Cuenta asociada"/><hbox>'+cmbcuentas+'</hbox></row>\n')
    req.write('        <row><label value="Nombre de la tarjeta"/><hbox><textbox id="tarjeta" value="Nueva tarjeta"/></hbox></row>\n')
    req.write('        <row><label value="Número de la tarjeta" /><hbox><textbox id="numero" value="XXXXXXXXXXXXXXXXXXX"/></hbox></row>        \n')
    req.write('        <row><label value="Pago diferido" /><hbox><checkbox id="pago_diferido" /></hbox></row>\n')
    req.write('        <row><label value="Saldo máximo" /><hbox><textbox id="saldomaximo" value="0"/></hbox></row>\n')
    req.write('        <row><label value="" /><hbox><button id="cmd" label="Aceptar" onclick="tarjeta_insert();"/></hbox></row>\n')
    req.write('        </rows>\n')
    req.write('    </grid>\n')
    req.write('    </hbox>\n')
    req.write('</vbox>\n')
    req.write('</window>\n')
    
