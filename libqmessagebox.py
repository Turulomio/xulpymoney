from libxulpymoney import tr

from PyQt5.QtWidgets import *

def qmessagebox_xulpymoney_update_and_superuser():
    m=QMessageBox()
    m.setIcon(QMessageBox.Information)
    m.setText(tr("Xulpymoney needs to be updated. Please login with a superuser role."))
    m.exec_()   
    
def qmessagebox_connexion_error(database, server):
    m=QMessageBox()
    m.setIcon(QMessageBox.Information)
    m.setText(tr("Error conecting to {} database in {} server").format(database, server))
    m.exec_()   
            
def qmessagebox_connexion_not_superuser():
    m=QMessageBox()
    m.setIcon(QMessageBox.Information)
    m.setText(tr("The role of the user is not an administrator"))
    m.exec_()   
            

def qmessagebox_developing():
    m=QMessageBox()
    m.setIcon(QMessageBox.Information)
    m.setText(tr( "This option is being developed"))
    m.exec_()    
    
def qmessagebox_error_ordering():
    m=QMessageBox()
    m.setIcon(QMessageBox.Information)
    m.setText(tr( "I couldn't order data due to they have null values"))
    m.exec_()    