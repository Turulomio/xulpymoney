# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xulpymoney/ui/wdgAccounts.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgAccounts(object):
    def setupUi(self, wdgAccounts):
        wdgAccounts.setObjectName("wdgAccounts")
        wdgAccounts.resize(579, 318)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(wdgAccounts)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl = QtWidgets.QLabel(wdgAccounts)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl.setFont(font)
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setObjectName("lbl")
        self.verticalLayout.addWidget(self.lbl)
        self.chkInactivas = QtWidgets.QCheckBox(wdgAccounts)
        self.chkInactivas.setObjectName("chkInactivas")
        self.verticalLayout.addWidget(self.chkInactivas)
        self.tblAccounts = myQTableWidget(wdgAccounts)
        self.tblAccounts.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblAccounts.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblAccounts.setAlternatingRowColors(True)
        self.tblAccounts.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblAccounts.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblAccounts.setObjectName("tblAccounts")
        self.tblAccounts.setColumnCount(4)
        self.tblAccounts.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblAccounts.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAccounts.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAccounts.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAccounts.setHorizontalHeaderItem(3, item)
        self.tblAccounts.verticalHeader().setVisible(False)
        self.tblAccounts.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout.addWidget(self.tblAccounts)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.wdgIBM = QtWidgets.QWidget(wdgAccounts)
        self.wdgIBM.setObjectName("wdgIBM")
        self.verticalLayout_2.addWidget(self.wdgIBM)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.lblTotal = QtWidgets.QLabel(wdgAccounts)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lblTotal.setFont(font)
        self.lblTotal.setText("")
        self.lblTotal.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTotal.setObjectName("lblTotal")
        self.verticalLayout_3.addWidget(self.lblTotal)
        self.actionAccountAdd = QtWidgets.QAction(wdgAccounts)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xulpymoney/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAccountAdd.setIcon(icon)
        self.actionAccountAdd.setObjectName("actionAccountAdd")
        self.actionAccountReport = QtWidgets.QAction(wdgAccounts)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/xulpymoney/coins.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAccountReport.setIcon(icon1)
        self.actionAccountReport.setObjectName("actionAccountReport")
        self.actionAccountDelete = QtWidgets.QAction(wdgAccounts)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/xulpymoney/list-remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAccountDelete.setIcon(icon2)
        self.actionAccountDelete.setObjectName("actionAccountDelete")
        self.actionActive = QtWidgets.QAction(wdgAccounts)
        self.actionActive.setCheckable(True)
        self.actionActive.setObjectName("actionActive")
        self.actionTransfer = QtWidgets.QAction(wdgAccounts)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/xulpymoney/transfer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTransfer.setIcon(icon3)
        self.actionTransfer.setObjectName("actionTransfer")

        self.retranslateUi(wdgAccounts)
        QtCore.QMetaObject.connectSlotsByName(wdgAccounts)

    def retranslateUi(self, wdgAccounts):
        _translate = QtCore.QCoreApplication.translate
        self.lbl.setText(_translate("wdgAccounts", "Account list"))
        self.chkInactivas.setText(_translate("wdgAccounts", "Show inactive accounts"))
        item = self.tblAccounts.horizontalHeaderItem(0)
        item.setText(_translate("wdgAccounts", "Account"))
        item = self.tblAccounts.horizontalHeaderItem(1)
        item.setText(_translate("wdgAccounts", "Bank"))
        item = self.tblAccounts.horizontalHeaderItem(2)
        item.setText(_translate("wdgAccounts", "Account number"))
        item = self.tblAccounts.horizontalHeaderItem(3)
        item.setText(_translate("wdgAccounts", "Balance"))
        self.actionAccountAdd.setText(_translate("wdgAccounts", "New account"))
        self.actionAccountAdd.setToolTip(_translate("wdgAccounts", "New account"))
        self.actionAccountReport.setText(_translate("wdgAccounts", "Account report"))
        self.actionAccountReport.setToolTip(_translate("wdgAccounts", "Account report"))
        self.actionAccountDelete.setText(_translate("wdgAccounts", "Delete account"))
        self.actionAccountDelete.setToolTip(_translate("wdgAccounts", "Delete account"))
        self.actionActive.setText(_translate("wdgAccounts", "Is it active?"))
        self.actionActive.setToolTip(_translate("wdgAccounts", "Is it active?"))
        self.actionTransfer.setText(_translate("wdgAccounts", "Transfer between accounts"))
        self.actionTransfer.setToolTip(_translate("wdgAccounts", "Transfer between accounts"))
from xulpymoney.ui.myqtablewidget import myQTableWidget
import xulpymoney.images.xulpymoney_rc
