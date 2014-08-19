from PyQt4.QtCore import *
from PyQt4.QtGui import *
from libxulpymoney import *
from frmAccountsReport import *
from frmInvestmentReport import *
from Ui_wdgBanks import *

class wdgBanks(QWidget, Ui_wdgBanks):
    def __init__(self, mem,  parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.mem=mem
#        self.selEB=None#id_ebs
#        self.selAccount=None #id_cuentas
#        self.investments.selected=None #Registro
        
        
        
        self.banks=SetBanks(self.mem) #Set
        self.investments=SetInvestments(self.mem, self.mem.data.accounts_active, self.mem.data.products_active, self.mem.data.benchmark) #Set
        self.accounts=SetAccounts(self.mem, self.mem.data.banks_active)#Set

        self.tblEB.settings("wdgBanks",  self.mem)
        self.tblAccounts.settings("wdgBanks",  self.mem)
        self.tblInvestments.settings("wdgBanks",  self.mem)
        
        self.on_chkInactivas_stateChanged(Qt.Unchecked)#Carga eb

        
    def load_eb(self):
        self.tblEB.clearContents()
        self.tblEB.setRowCount(self.banks.length()+1)
        sumsaldos=Decimal(0)
        for i,  e in enumerate(self.banks.arr):
            self.tblEB.setItem(i, 0, QTableWidgetItem(e.name))
            self.tblEB.setItem(i, 1, qbool(e.activa))
            balance=e.balance(self.mem.data.accounts_active, self.mem.data.inversiones_active)
            self.tblEB.setItem(i, 2, self.mem.localcurrency.qtablewidgetitem(balance))
            sumsaldos=sumsaldos+balance     
        self.tblEB.setItem(self.banks.length(), 0, QTableWidgetItem(self.tr('TOTAL')))
        self.tblEB.setItem(self.banks.length(), 2, self.mem.localcurrency.qtablewidgetitem(sumsaldos))        
        
    def load_cuentas(self):
        self.tblAccounts.clearContents()
        self.tblAccounts.setRowCount(self.accounts.length()+1);
        sumsaldos=0
        for i,  c in enumerate(self.accounts.arr):
            self.tblAccounts.setItem(i, 0, QTableWidgetItem(c.name))
            self.tblAccounts.setItem(i, 1, qbool(c.activa))
            self.tblAccounts.setItem(i, 2, self.mem.localcurrency.qtablewidgetitem(c.balance))
            sumsaldos=sumsaldos+c.balance
        self.tblAccounts.setItem(self.accounts.length(), 0, QTableWidgetItem(self.tr('TOTAL')))
        self.tblAccounts.setItem(self.accounts.length(), 2, self.mem.localcurrency.qtablewidgetitem(sumsaldos))                
        
                
    def load_inversiones(self):
        self.tblInvestments.clearContents()
        self.tblInvestments.setRowCount(self.investments.length()+1);
        sumsaldos=0
        for i, inv in enumerate(self.investments.arr):
            self.tblInvestments.setItem(i, 0, QTableWidgetItem(inv.name))
            self.tblInvestments.setItem(i, 1, qbool(inv.activa))
            balance=inv.balance()
            self.tblInvestments.setItem(i, 2, self.mem.localcurrency.qtablewidgetitem(balance))
            sumsaldos=sumsaldos+balance
        self.tblInvestments.setItem(self.investments.length(), 0, QTableWidgetItem(self.tr('TOTAL')))
        self.tblInvestments.setItem(self.investments.length(), 2, self.mem.localcurrency.qtablewidgetitem(sumsaldos))                
        
        
    def on_chkInactivas_stateChanged(self, state):
        self.banks=self.mem.data.banks_set(not c2b(state))
        self.load_eb()
        self.tblEB.clearSelection()   
        self.tblAccounts.setRowCount(0)
        self.tblAccounts.clearContents()
        self.tblInvestments.setRowCount(0);
        self.tblInvestments.clearContents()

    def on_tblEB_itemSelectionChanged(self):
        self.banks.selected=None
        self.investments.clean()
        self.accounts.clean()
        
        for i in self.tblEB.selectedItems():#itera por cada item no row.
            if i.row()<self.banks.length():#Necesario porque tiene fila de total
                self.banks.selected=self.banks.arr[i.row()]
        print ("Seleccionado: " +  str(self.banks.selected))
        
        if self.banks.selected==None:
            self.tblEB.clearSelection()   
            self.tblAccounts.setRowCount(0)
            self.tblAccounts.clearContents()
            self.tblInvestments.setRowCount(0);
            self.tblInvestments.clearContents()
            return
            
        activas=False
        if self.chkInactivas.checkState()==Qt.Unchecked:
            activas=True
        
        for i in self.mem.data.investments_set(activas).arr:
            if i.cuenta.eb.id==self.banks.selected.id:
                self.investments.append(i)
        self.investments.sort_by_name()
        
        for v in self.mem.data.accounts_set(activas).arr:
            if v.eb.id==self.banks.selected.id:
                self.accounts.append(v)
        self.accounts.sort_by_name()
        
        self.load_cuentas()
        self.load_inversiones()

    def on_tblEB_customContextMenuRequested(self,  pos):
        if self.banks.selected==None:
            self.actionBankDelete.setEnabled(False)
            self.actionBankEdit.setEnabled(False)
            self.actionActive.setEnabled(False)
        else:
            self.actionBankDelete.setEnabled(True)
            self.actionBankEdit.setEnabled(True)
            self.actionActive.setEnabled(True)
            
        if self.chkInactivas.checkState()==Qt.Unchecked:
            self.actionActive.setChecked(True)
        else:
            self.actionActive.setChecked(False)
            
        menu=QMenu()
        menu.addAction(self.actionBankAdd)
        menu.addAction(self.actionBankEdit)
        menu.addAction(self.actionBankDelete)
        menu.addSeparator()
        menu.addAction(self.actionActive)
        menu.exec_(self.tblEB.mapToGlobal(pos))
        
    @QtCore.pyqtSlot() 
    def on_actionAccountReport_activated(self):
        w=frmAccountsReport(self.mem, self.accounts.selected)
        w.exec_()        
        self.load_cuentas()

    @QtCore.pyqtSlot() 
    def on_actionInvestmentReport_activated(self):
        w=frmInvestmentReport(self.mem,   self.investments.selected)
        w.exec_()
        self.load_inversiones()

    def on_tblAccounts_itemSelectionChanged(self):
        self.accounts.selected=None
        for i in self.tblAccounts.selectedItems():#itera por cada item no row.
            if i.row()<self.accounts.length():#Necesario porque tiene fila de total
                self.accounts.selected=self.accounts.arr[i.row()]
        print ("Seleccionado: " +  str(self.accounts.selected))

    def on_tblAccounts_customContextMenuRequested(self,  pos):
        if self.accounts.selected==None:
            self.actionAccountReport.setEnabled(False)
        else:
            self.actionAccountReport.setEnabled(True)
        menu=QMenu()
        menu.addAction(self.actionAccountReport)
        menu.exec_(self.tblAccounts.mapToGlobal(pos))


    def on_tblInvestments_itemSelectionChanged(self):
        self.investments.selected=None
        for i in self.tblInvestments.selectedItems():#itera por cada item no row.
            if i.row()<self.investments.length():#Necesario porque tiene fila de total
                self.investments.selected=self.investments.arr[i.row()]
        print ("Seleccionado: " +  str(self.investments.selected))

        
    def on_tblInvestments_customContextMenuRequested(self,  pos):
        if self.investments.selected==None:
            self.actionInvestmentReport.setEnabled(False)
        else:
            self.actionInvestmentReport.setEnabled(True)
        menu=QMenu()
        menu.addAction(self.actionInvestmentReport)        
        menu.exec_(self.tblInvestments.mapToGlobal(pos))
        
    @QtCore.pyqtSlot()  
    def on_actionBankDelete_activated(self):
        if self.banks.selected.qmessagebox_inactive():
            return        
        self.mem.data.load_inactives()
        if self.banks.selected.es_borrable(self.mem.data.accounts_all())==False:
            m=QMessageBox()
            m.setIcon(QMessageBox.Information)
            m.setText(self.tr("This bank has dependent accounts and it can't be deleted"))
            m.exec_()
        else:
            self.banks.selected.borrar(self.mem.dic_cuentas)
            #Se borra de la lista de wdgBanks ebs y del diccionario raiz 
            self.banks.remove(self.banks.selected)
            con.commit()  
            self.load_eb()    
        
    @QtCore.pyqtSlot()  
    def on_actionBankAdd_activated(self):
        tipo=QInputDialog().getText(self,  "Xulpymoney",  self.tr("Add a new bank"))
        if tipo[1]==True:
            eb=Bank(self.mem).init__create(tipo[0])
            eb.save()
            self.mem.con.commit()  
            self.mem.data.banks_active.append(eb)
            self.mem.data.banks_active.sort_by_name()
            self.load_eb()


    @QtCore.pyqtSlot()  
    def on_actionBankEdit_activated(self):
        tipo=QInputDialog().getText(self,  "Xulpymoney", self.tr("Edit selected bank") , QLineEdit.Normal,   (self.banks.selected.name))       
        if tipo[1]==True:
            self.banks.selected.name=tipo[0]
            self.banks.selected.save()
            self.mem.con.commit()
            self.mem.data.banks_active.sort()
            self.load_eb()   
        
    @QtCore.pyqtSlot() 
    def on_actionActive_activated(self):
        self.mem.data.load_inactives()
        self.banks.selected.activa=self.actionActive.isChecked()
        self.banks.selected.save()
        self.mem.con.commit()   
        
        #Recoloca en los SetInvestments
        if self.banks.selected.activa==True:#Está todavía en inactivas
            self.mem.data.banks_active.append(self.banks.selected)
            self.mem.data.banks_inactive.remove(self.banks.selected)
        else:#Está todavía en activas
            self.mem.data.banks_active.remove(self.banks.selected)
            self.mem.data.banks_inactive.append(self.banks.selected)
        
        self.load_eb()
