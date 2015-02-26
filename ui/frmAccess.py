from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Ui_frmAccess import *

class frmAccess(QDialog, Ui_frmAccess):
    def __init__(self, mem, parent = None, name = None, modal = False):
        QDialog.__init__(self,  parent)
        self.mem=mem
        self.setModal(True)
        self.setupUi(self)
        self.parent=parent
        self.mem.languages.qcombobox(self.cmbLanguages,self.mem.languages.find(self.mem.config.get_value("settings", "language")))

        icon = QtGui.QIcon()
        pix=QtGui.QPixmap(":xulpymoney/coins.png")
        icon.addPixmap(pix, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)        
        self.setWindowTitle(self.tr("Xulpymoney - Access"))
        self.txtDB.setText(self.mem.config.get_value("frmAccess", "db" ))
        self.txtPort.setText(self.mem.config.get_value("frmAccess", "port" ))
        self.txtUser.setText(self.mem.config.get_value("frmAccess", "user" ))
        self.txtServer.setText(self.mem.config.get_value("frmAccess", "server" ))

    @pyqtSlot(str)      
    def on_cmbLanguages_currentIndexChanged(self, stri):
        self.mem.languages.cambiar(self.cmbLanguages.itemData(self.cmbLanguages.currentIndex()))
        self.retranslateUi(self)

    def make_connection(self):
        """Función que realiza la conexión devolviendo true o false con el éxito"""
        try:
            self.mem.config.set_value("frmAccess", "db", self.txtDB.text() )
            self.mem.config.set_value("frmAccess", "port",  self.txtPort.text())
            self.mem.config.set_value("frmAccess", "user" ,  self.txtUser.text())
            self.mem.config.set_value("frmAccess", "server", self.txtServer.text())   
            self.mem.config.set_value("settings", "language", self.cmbLanguages.itemData(self.cmbLanguages.currentIndex()))
            self.mem.config.save()      
            self.mem.password=self.txtPass.text()
            self.mem.con=self.mem.connect_from_config()                       
            return True
        except:
            print ("Error in function make_connection",  self.mem.con)
            return False
    
    @QtCore.pyqtSlot() 
    def on_cmdYN_accepted(self):
        if self.make_connection()==False:
            self.reject()
            return
        self.accept()

    @QtCore.pyqtSlot() 
    def on_cmdYN_rejected(self):
        self.reject()

