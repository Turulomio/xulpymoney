# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xulpymoney/ui/wdgProducts.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgProducts(object):
    def setupUi(self, wdgProducts):
        wdgProducts.setObjectName("wdgProducts")
        wdgProducts.resize(892, 263)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(wdgProducts)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl = QtWidgets.QLabel(wdgProducts)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl.setFont(font)
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setObjectName("lbl")
        self.verticalLayout_3.addWidget(self.lbl)
        self.groupBox = QtWidgets.QGroupBox(wdgProducts)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.txt = QtWidgets.QLineEdit(self.groupBox)
        self.txt.setObjectName("txt")
        self.horizontalLayout.addWidget(self.txt)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.chkStockExchange = QtWidgets.QCheckBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkStockExchange.sizePolicy().hasHeightForWidth())
        self.chkStockExchange.setSizePolicy(sizePolicy)
        self.chkStockExchange.setObjectName("chkStockExchange")
        self.horizontalLayout_2.addWidget(self.chkStockExchange)
        self.cmbStockExchange = QtWidgets.QComboBox(self.groupBox)
        self.cmbStockExchange.setEnabled(False)
        self.cmbStockExchange.setObjectName("cmbStockExchange")
        self.horizontalLayout_2.addWidget(self.cmbStockExchange)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.cmd = QtWidgets.QToolButton(self.groupBox)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xulpymoney/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmd.setIcon(icon)
        self.cmd.setObjectName("cmd")
        self.horizontalLayout_3.addWidget(self.cmd)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setEnabled(False)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.mqtwInvestments = mqtwObjects(wdgProducts)
        self.mqtwInvestments.setObjectName("mqtwInvestments")
        self.verticalLayout_3.addWidget(self.mqtwInvestments)
        self.lblFound = QtWidgets.QLabel(wdgProducts)
        self.lblFound.setObjectName("lblFound")
        self.verticalLayout_3.addWidget(self.lblFound)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.actionProductReport = QtWidgets.QAction(wdgProducts)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/xulpymoney/books.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProductReport.setIcon(icon1)
        self.actionProductReport.setObjectName("actionProductReport")
        self.actionIbex35 = QtWidgets.QAction(wdgProducts)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/countries/spain.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionIbex35.setIcon(icon2)
        self.actionIbex35.setObjectName("actionIbex35")
        self.actionProductNew = QtWidgets.QAction(wdgProducts)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/xulpymoney/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProductNew.setIcon(icon3)
        self.actionProductNew.setObjectName("actionProductNew")
        self.actionProductDelete = QtWidgets.QAction(wdgProducts)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/xulpymoney/list-remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProductDelete.setIcon(icon4)
        self.actionProductDelete.setObjectName("actionProductDelete")
        self.actionFavorites = QtWidgets.QAction(wdgProducts)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/xulpymoney/star.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFavorites.setIcon(icon5)
        self.actionFavorites.setObjectName("actionFavorites")
        self.actionMergeCodes = QtWidgets.QAction(wdgProducts)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/xulpymoney/merge.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMergeCodes.setIcon(icon6)
        self.actionMergeCodes.setObjectName("actionMergeCodes")
        self.actionQuoteNew = QtWidgets.QAction(wdgProducts)
        self.actionQuoteNew.setIcon(icon3)
        self.actionQuoteNew.setObjectName("actionQuoteNew")
        self.actionEstimationDPSNew = QtWidgets.QAction(wdgProducts)
        self.actionEstimationDPSNew.setIcon(icon3)
        self.actionEstimationDPSNew.setObjectName("actionEstimationDPSNew")
        self.actionPurge = QtWidgets.QAction(wdgProducts)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/xulpymoney/tools-wizard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPurge.setIcon(icon7)
        self.actionPurge.setObjectName("actionPurge")
        self.actionPurchaseGraphic = QtWidgets.QAction(wdgProducts)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/xulpymoney/report.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPurchaseGraphic.setIcon(icon8)
        self.actionPurchaseGraphic.setObjectName("actionPurchaseGraphic")
        self.actionProductPriceLastRemove = QtWidgets.QAction(wdgProducts)
        self.actionProductPriceLastRemove.setIcon(icon4)
        self.actionProductPriceLastRemove.setObjectName("actionProductPriceLastRemove")

        self.retranslateUi(wdgProducts)
        self.chkStockExchange.toggled['bool'].connect(self.cmbStockExchange.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(wdgProducts)

    def retranslateUi(self, wdgProducts):
        _translate = QtCore.QCoreApplication.translate
        self.lbl.setText(_translate("wdgProducts", "Products list"))
        self.groupBox.setTitle(_translate("wdgProducts", "Select your search"))
        self.label.setText(_translate("wdgProducts", "Search by code, ISIN, ticker or product name"))
        self.chkStockExchange.setText(_translate("wdgProducts", "Filter by stock exchange"))
        self.lblFound.setText(_translate("wdgProducts", "Registers found"))
        self.actionProductReport.setText(_translate("wdgProducts", "Product report"))
        self.actionProductReport.setToolTip(_translate("wdgProducts", "Product report"))
        self.actionIbex35.setText(_translate("wdgProducts", "Ibex 35"))
        self.actionProductNew.setText(_translate("wdgProducts", "New product"))
        self.actionProductNew.setToolTip(_translate("wdgProducts", "New user product"))
        self.actionProductDelete.setText(_translate("wdgProducts", "Delete product"))
        self.actionProductDelete.setToolTip(_translate("wdgProducts", "Delete user product"))
        self.actionFavorites.setText(_translate("wdgProducts", "Add to favorites"))
        self.actionFavorites.setToolTip(_translate("wdgProducts", "Add to favorites"))
        self.actionMergeCodes.setText(_translate("wdgProducts", "Merge selected codes"))
        self.actionMergeCodes.setToolTip(_translate("wdgProducts", "Merge selected codes"))
        self.actionQuoteNew.setText(_translate("wdgProducts", "New price"))
        self.actionQuoteNew.setToolTip(_translate("wdgProducts", "New price"))
        self.actionEstimationDPSNew.setText(_translate("wdgProducts", "New DPS estimation"))
        self.actionEstimationDPSNew.setToolTip(_translate("wdgProducts", "New Dividend per share estimation"))
        self.actionPurge.setText(_translate("wdgProducts", "Purge investment"))
        self.actionPurge.setToolTip(_translate("wdgProducts", "Deletes quotes innecesary. Leaves open, high, low and close quotes."))
        self.actionPurchaseGraphic.setText(_translate("wdgProducts", "Show purchase graphic"))
        self.actionPurchaseGraphic.setToolTip(_translate("wdgProducts", "Show purchase graphic"))
        self.actionProductPriceLastRemove.setText(_translate("wdgProducts", "Remove last product price"))
        self.actionProductPriceLastRemove.setToolTip(_translate("wdgProducts", "Remove last product price"))
from xulpymoney.ui.myqtablewidget import mqtwObjects
import xulpymoney.images.xulpymoney_rc
