from libxulpymoney import *
from libqmessagebox import qmessagebox_error_ordering
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Ui_wdgLastCurrent import *
from frmInvestmentReport import *
from frmQuotesIBM import *
from frmProductReport import *
from wdgCalculator import *
from wdgDisReinvest import *

class wdgLastCurrent(QWidget, Ui_wdgLastCurrent):
    def __init__(self, mem,  parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.mem=mem
        self.investments=None
        self.tblInvestments.settings(self.mem, "wdgLastCurrent")
        self.spin.setValue(int(self.mem.settingsdb.value("wdgLastCurrent/spin", "-25")))
        self.tblInvestments_reload()
        
    def tblInvestments_reload(self):
        firsttime=False#Switch to inictializate and default sorting
        if self.investments==None:
            firsttime=True
        
        if self.chkSameProduct.checkState()==Qt.Unchecked:
            self.investments=self.mem.data.investments_active()
        else:
            self.investments=self.mem.data.investments_active().setInvestments_merging_investments_with_same_product_merging_current_operations()
            
    
            
#        #Now removes op_actual with no shares
#        indextoremove=[]
#        for i in self.investments.arr:
#            if i.op_actual.acciones()>0:
#                indextoremove.append(i.id)
        if firsttime==True:
            self.on_actionSortTPCLast_triggered()
        self.investments.myqtablewidget_lastCurrent(self.tblInvestments, self.spin.value())
        
    @QtCore.pyqtSlot() 
    def on_actionInvestmentReport_triggered(self):
        w=frmInvestmentReport(self.mem, self.investments.selected, self)
        w.exec_()
        self.tblInvestments_reload()
        
    @QtCore.pyqtSlot() 
    def on_actionCalculate_triggered(self):
        d=QDialog(self)        
        d.setFixedSize(850, 850)
        d.setWindowTitle(self.tr("Investment last operation calculator"))
        w=wdgCalculator(self.mem)
        w.setInvestment(self.investments.selected)
        price=self.investments.selected.op_actual.last().valor_accion*(1+self.spin.value()/Decimal(100))#Is + because -·-
        w.txtFinalPrice.setText(price)
        lay = QVBoxLayout(d)
        lay.addWidget(w)
        d.show()        
        
    @QtCore.pyqtSlot() 
    def on_actionReinvest_triggered(self):
        d=QDialog()       
        d.resize(self.mem.settings.value("frmInvestmentReport/qdialog_disreinvest", QSize(1024, 768)))
        d.setWindowTitle(self.tr("Divest / Reinvest simulation"))
        w=wdgDisReinvest(self.mem, self.investments.selected, False,  d)
        price=self.investments.selected.op_actual.last().valor_accion*(1+self.spin.value()/Decimal(100))#Is + because -·-        
        w.txtValorAccion.setText(price)
        lay = QVBoxLayout(d)
        lay.addWidget(w)
        d.exec_()
        self.mem.settings.setValue("frmInvestmentReport/qdialog_disreinvest", d.size())        
        
    @QtCore.pyqtSlot() 
    def on_actionReinvestCurrent_triggered(self):
        d=QDialog()       
        d.resize(self.mem.settings.value("frmInvestmentReport/qdialog_disreinvest", QSize(1024, 768)))
        d.setWindowTitle(self.tr("Divest / Reinvest simulation"))
        w=wdgDisReinvest(self.mem, self.investments.selected, False,  d)
        lay = QVBoxLayout(d)
        lay.addWidget(w)
        d.exec_()
        self.mem.settings.setValue("frmInvestmentReport/qdialog_disreinvest", d.size())
                
    @QtCore.pyqtSlot() 
    def on_actionProduct_triggered(self):
        w=frmProductReport(self.mem, self.investments.selected.product, self.investments.selected, self)
        w.exec_()
        self.tblInvestments_reload()
      
   
    @QtCore.pyqtSlot() 
    def on_actionSortTPCVenta_triggered(self):
        if self.investments.order_by_percentage_sellingpoint()==False:
            qmessagebox_error_ordering()     
        self.tblInvestments_reload()
        
    @QtCore.pyqtSlot() 
    def on_actionSortTPC_triggered(self):
        if self.investments.order_by_percentage_invested()==False:
            qmessagebox_error_ordering()     
        self.tblInvestments_reload()
        
    @QtCore.pyqtSlot() 
    def on_actionSortHour_triggered(self):
        if self.investments.order_by_datetime_last_operation()==False:
            qmessagebox_error_ordering()     
        self.tblInvestments_reload()
        
    @QtCore.pyqtSlot() 
    def on_actionSortName_triggered(self):            
        if self.investments.order_by_name()==False:
            qmessagebox_error_ordering()     
        self.tblInvestments_reload()    

    @QtCore.pyqtSlot() 
    def on_actionSortTPCLast_triggered(self):
        if self.investments.order_by_percentage_last_operation()==False:
            qmessagebox_error_ordering()     
        self.tblInvestments_reload()    
            

    def on_tblInvestments_customContextMenuRequested(self,  pos):
        if self.investments.selected==None:
            self.actionInvestmentReport.setEnabled(False)
            self.actionProduct.setEnabled(False)
        else:
            self.actionInvestmentReport.setEnabled(True)
            self.actionProduct.setEnabled(True)


        self.actionCalculate.setText("Calculate order at {} since last operation".format(tpc(self.spin.value())))
        self.actionReinvest.setText("Simulate reinvestment at {} since last operation".format(tpc(self.spin.value())))
        menu=QMenu()
        menu.addAction(self.actionCalculate)
        menu.addSeparator()
        menu.addAction(self.actionReinvestCurrent)
        menu.addAction(self.actionReinvest)
        menu.addSeparator()
        menu.addAction(self.actionInvestmentReport)        
        menu.addAction(self.actionProduct)
        menu.addSeparator()
        ordenar=QMenu(self.tr("Order by"))
        ordenar.addAction(self.actionSortName)
        ordenar.addAction(self.actionSortHour)
        ordenar.addAction(self.actionSortTPCLast)
        ordenar.addAction(self.actionSortTPC)
        ordenar.addAction(self.actionSortTPCVenta)
        menu.addMenu(ordenar)        
        menu.exec_(self.tblInvestments.mapToGlobal(pos))

    def on_cmd_released(self):
        self.tblInvestments_reload()
        self.mem.settingsdb.setValue("wdgLastCurrent/spin", self.spin.value())

    def on_tblInvestments_itemSelectionChanged(self):
        self.investments.selected=None
        for i in self.tblInvestments.selectedItems():#itera por cada item no row.
            self.investments.selected=self.investments.arr[i.row()]

    @QtCore.pyqtSlot(int, int) 
    def on_tblInvestments_cellDoubleClicked(self, row, column):
        if column==8:#TPC Venta
            m=QMessageBox()
            m.setWindowIcon(QIcon(":/xulpymoney/coins.png"))
            m.setIcon(QMessageBox.Information)
            m.setText(self.tr("Shares number: {0}").format(self.investments.selected.acciones())+"\n"+
                    self.tr("Purchase price average: {0}").format(self.investments.selected.product.currency.string(self.investments.selected.op_actual.average_price()))+"\n"+
                    self.tr("Selling point: {}").format(self.investments.selected.product.currency.string(self.investments.selected.venta))+"\n"+
                    self.tr("Selling all shares you get {}").format(self.investments.selected.product.currency.string(self.investments.selected.op_actual.pendiente(Quote(self.mem).init__create(self.investments.selected.product, self.mem.localzone.now(),  self.investments.selected.venta))))
            )
            m.exec_()     
        else:
            self.on_actionCalculate_triggered()

    def on_chkSameProduct_stateChanged(self, state):
        self.tblInvestments_reload()
