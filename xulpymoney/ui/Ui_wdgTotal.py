# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xulpymoney/ui/wdgTotal.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgTotal(object):
    def setupUi(self, wdgTotal):
        wdgTotal.setObjectName("wdgTotal")
        wdgTotal.resize(1512, 815)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(wdgTotal)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblTitulo = QtWidgets.QLabel(wdgTotal)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitulo.setObjectName("lblTitulo")
        self.verticalLayout_2.addWidget(self.lblTitulo)
        self.tab = QtWidgets.QTabWidget(wdgTotal)
        self.tab.setTabsClosable(True)
        self.tab.setObjectName("tab")
        self.tabDatos = QtWidgets.QWidget()
        self.tabDatos.setObjectName("tabDatos")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tabDatos)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.wyData = wdgYear(self.tabDatos)
        self.wyData.setObjectName("wyData")
        self.horizontalLayout.addWidget(self.wyData)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.tabData = QtWidgets.QTabWidget(self.tabDatos)
        self.tabData.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabData.setObjectName("tabData")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblPreviousYear = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lblPreviousYear.setFont(font)
        self.lblPreviousYear.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPreviousYear.setObjectName("lblPreviousYear")
        self.verticalLayout.addWidget(self.lblPreviousYear)
        self.table = myQTableWidget(self.tab_3)
        self.table.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.table.setObjectName("table")
        self.table.setColumnCount(13)
        self.table.setRowCount(12)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(12, item)
        self.verticalLayout.addWidget(self.table)
        self.lblInvested = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblInvested.setFont(font)
        self.lblInvested.setText("")
        self.lblInvested.setAlignment(QtCore.Qt.AlignCenter)
        self.lblInvested.setObjectName("lblInvested")
        self.verticalLayout.addWidget(self.lblInvested)
        self.horizontalLayout_8.addLayout(self.verticalLayout)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xulpymoney/coins.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabData.addTab(self.tab_3, icon, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.lblTarget = QtWidgets.QLabel(self.tab_4)
        self.lblTarget.setObjectName("lblTarget")
        self.horizontalLayout_5.addWidget(self.lblTarget)
        self.spinTarget = QtWidgets.QDoubleSpinBox(self.tab_4)
        self.spinTarget.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinTarget.setObjectName("spinTarget")
        self.horizontalLayout_5.addWidget(self.spinTarget)
        self.cmdTargets = QtWidgets.QToolButton(self.tab_4)
        self.cmdTargets.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/xulpymoney/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmdTargets.setIcon(icon1)
        self.cmdTargets.setObjectName("cmdTargets")
        self.horizontalLayout_5.addWidget(self.cmdTargets)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.tabPlus = QtWidgets.QTabWidget(self.tab_4)
        self.tabPlus.setObjectName("tabPlus")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.tab_6)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tblTargets = myQTableWidget(self.tab_6)
        self.tblTargets.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblTargets.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblTargets.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblTargets.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tblTargets.setObjectName("tblTargets")
        self.tblTargets.setColumnCount(13)
        self.tblTargets.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargets.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargets.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargets.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargets.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargets.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargets.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargets.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargets.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargets.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargets.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargets.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargets.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargets.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargets.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargets.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargets.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargets.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargets.setHorizontalHeaderItem(12, item)
        self.verticalLayout_3.addWidget(self.tblTargets)
        self.lblTargets = QtWidgets.QLabel(self.tab_6)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblTargets.setFont(font)
        self.lblTargets.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTargets.setObjectName("lblTargets")
        self.verticalLayout_3.addWidget(self.lblTargets)
        self.horizontalLayout_10.addLayout(self.verticalLayout_3)
        self.tabPlus.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.tab_7)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.tblTargetsPlus = myQTableWidget(self.tab_7)
        self.tblTargetsPlus.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblTargetsPlus.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblTargetsPlus.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblTargetsPlus.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tblTargetsPlus.setObjectName("tblTargetsPlus")
        self.tblTargetsPlus.setColumnCount(13)
        self.tblTargetsPlus.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargetsPlus.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargetsPlus.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargetsPlus.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargetsPlus.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargetsPlus.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargetsPlus.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargetsPlus.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargetsPlus.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargetsPlus.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargetsPlus.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargetsPlus.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargetsPlus.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargetsPlus.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargetsPlus.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargetsPlus.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargetsPlus.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargetsPlus.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargetsPlus.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargetsPlus.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTargetsPlus.setHorizontalHeaderItem(12, item)
        self.verticalLayout_9.addWidget(self.tblTargetsPlus)
        self.lblTargetsPlus = QtWidgets.QLabel(self.tab_7)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblTargetsPlus.setFont(font)
        self.lblTargetsPlus.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTargetsPlus.setObjectName("lblTargetsPlus")
        self.verticalLayout_9.addWidget(self.lblTargetsPlus)
        self.horizontalLayout_11.addLayout(self.verticalLayout_9)
        self.tabPlus.addTab(self.tab_7, "")
        self.verticalLayout_8.addWidget(self.tabPlus)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/xulpymoney/gafas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabData.addTab(self.tab_4, icon2, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tblInvestOrWork = myQTableWidget(self.tab_2)
        self.tblInvestOrWork.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblInvestOrWork.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblInvestOrWork.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblInvestOrWork.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tblInvestOrWork.setObjectName("tblInvestOrWork")
        self.tblInvestOrWork.setColumnCount(13)
        self.tblInvestOrWork.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestOrWork.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestOrWork.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestOrWork.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestOrWork.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestOrWork.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestOrWork.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestOrWork.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestOrWork.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestOrWork.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestOrWork.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestOrWork.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestOrWork.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestOrWork.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestOrWork.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestOrWork.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestOrWork.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestOrWork.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestOrWork.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestOrWork.setHorizontalHeaderItem(12, item)
        self.verticalLayout_5.addWidget(self.tblInvestOrWork)
        self.lblInvestOrWork = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblInvestOrWork.setFont(font)
        self.lblInvestOrWork.setText("")
        self.lblInvestOrWork.setAlignment(QtCore.Qt.AlignCenter)
        self.lblInvestOrWork.setObjectName("lblInvestOrWork")
        self.verticalLayout_5.addWidget(self.lblInvestOrWork)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/xulpymoney/tools-wizard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabData.addTab(self.tab_2, icon3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tblMakeEndsMeet = myQTableWidget(self.tab_5)
        self.tblMakeEndsMeet.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblMakeEndsMeet.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblMakeEndsMeet.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblMakeEndsMeet.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tblMakeEndsMeet.setObjectName("tblMakeEndsMeet")
        self.tblMakeEndsMeet.setColumnCount(13)
        self.tblMakeEndsMeet.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tblMakeEndsMeet.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMakeEndsMeet.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMakeEndsMeet.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMakeEndsMeet.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMakeEndsMeet.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMakeEndsMeet.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMakeEndsMeet.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMakeEndsMeet.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMakeEndsMeet.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMakeEndsMeet.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMakeEndsMeet.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMakeEndsMeet.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMakeEndsMeet.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMakeEndsMeet.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMakeEndsMeet.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMakeEndsMeet.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMakeEndsMeet.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMakeEndsMeet.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMakeEndsMeet.setHorizontalHeaderItem(12, item)
        self.verticalLayout_6.addWidget(self.tblMakeEndsMeet)
        self.lblMakeEndsMeet = QtWidgets.QLabel(self.tab_5)
        self.lblMakeEndsMeet.setText("")
        self.lblMakeEndsMeet.setObjectName("lblMakeEndsMeet")
        self.verticalLayout_6.addWidget(self.lblMakeEndsMeet)
        self.horizontalLayout_9.addLayout(self.verticalLayout_6)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/xulpymoney/books.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabData.addTab(self.tab_5, icon4, "")
        self.verticalLayout_7.addWidget(self.tabData)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.tab.addTab(self.tabDatos, icon, "")
        self.tabGraphic = QtWidgets.QWidget()
        self.tabGraphic.setObjectName("tabGraphic")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabGraphic)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabGraphTotal = QtWidgets.QVBoxLayout()
        self.tabGraphTotal.setObjectName("tabGraphTotal")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.wyChart = wdgYear(self.tabGraphic)
        self.wyChart.setObjectName("wyChart")
        self.horizontalLayout_6.addWidget(self.wyChart)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.tabGraphTotal.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addLayout(self.tabGraphTotal)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/xulpymoney/pie.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab.addTab(self.tabGraphic, icon5, "")
        self.verticalLayout_2.addWidget(self.tab)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.actionShowIncomes = QtWidgets.QAction(wdgTotal)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/xulpymoney/bundle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShowIncomes.setIcon(icon6)
        self.actionShowIncomes.setObjectName("actionShowIncomes")
        self.actionShowExpenses = QtWidgets.QAction(wdgTotal)
        self.actionShowExpenses.setObjectName("actionShowExpenses")
        self.actionShowDividends = QtWidgets.QAction(wdgTotal)
        self.actionShowDividends.setIcon(icon)
        self.actionShowDividends.setObjectName("actionShowDividends")
        self.actionShowSellingOperations = QtWidgets.QAction(wdgTotal)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/xulpymoney/dinero.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShowSellingOperations.setIcon(icon7)
        self.actionShowSellingOperations.setObjectName("actionShowSellingOperations")
        self.actionShowComissions = QtWidgets.QAction(wdgTotal)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/xulpymoney/bank.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShowComissions.setIcon(icon8)
        self.actionShowComissions.setObjectName("actionShowComissions")
        self.actionShowTaxes = QtWidgets.QAction(wdgTotal)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/xulpymoney/study.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShowTaxes.setIcon(icon9)
        self.actionShowTaxes.setObjectName("actionShowTaxes")
        self.actionGainsByProductType = QtWidgets.QAction(wdgTotal)
        self.actionGainsByProductType.setIcon(icon)
        self.actionGainsByProductType.setObjectName("actionGainsByProductType")

        self.retranslateUi(wdgTotal)
        self.tab.setCurrentIndex(0)
        self.tabData.setCurrentIndex(1)
        self.tabPlus.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(wdgTotal)

    def retranslateUi(self, wdgTotal):
        _translate = QtCore.QCoreApplication.translate
        self.lblTitulo.setText(_translate("wdgTotal", "Total report"))
        self.table.setSortingEnabled(False)
        item = self.table.verticalHeaderItem(0)
        item.setText(_translate("wdgTotal", "Incomes"))
        item = self.table.verticalHeaderItem(1)
        item.setText(_translate("wdgTotal", "Gains"))
        item = self.table.verticalHeaderItem(2)
        item.setText(_translate("wdgTotal", "Dividends"))
        item = self.table.verticalHeaderItem(3)
        item.setText(_translate("wdgTotal", "Expenses"))
        item = self.table.verticalHeaderItem(4)
        item.setText(_translate("wdgTotal", "I+G+D-E"))
        item = self.table.verticalHeaderItem(6)
        item.setText(_translate("wdgTotal", "Accounts"))
        item = self.table.verticalHeaderItem(7)
        item.setText(_translate("wdgTotal", "Investments"))
        item = self.table.verticalHeaderItem(8)
        item.setText(_translate("wdgTotal", "Total"))
        item = self.table.verticalHeaderItem(9)
        item.setText(_translate("wdgTotal", "Monthly difference"))
        item = self.table.verticalHeaderItem(11)
        item.setText(_translate("wdgTotal", "% Year to date"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("wdgTotal", "January"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("wdgTotal", "February"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("wdgTotal", "March"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("wdgTotal", "April"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("wdgTotal", "May"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("wdgTotal", "June"))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("wdgTotal", "July"))
        item = self.table.horizontalHeaderItem(7)
        item.setText(_translate("wdgTotal", "August"))
        item = self.table.horizontalHeaderItem(8)
        item.setText(_translate("wdgTotal", "September"))
        item = self.table.horizontalHeaderItem(9)
        item.setText(_translate("wdgTotal", "October"))
        item = self.table.horizontalHeaderItem(10)
        item.setText(_translate("wdgTotal", "November"))
        item = self.table.horizontalHeaderItem(11)
        item.setText(_translate("wdgTotal", "December"))
        item = self.table.horizontalHeaderItem(12)
        item.setText(_translate("wdgTotal", "Total"))
        self.tabData.setTabText(self.tabData.indexOf(self.tab_3), _translate("wdgTotal", "Data in the year"))
        self.lblTarget.setText(_translate("wdgTotal", "Annual target percentage"))
        self.spinTarget.setSuffix(_translate("wdgTotal", " %"))
        self.tblTargets.setSortingEnabled(False)
        item = self.tblTargets.verticalHeaderItem(0)
        item.setText(_translate("wdgTotal", "Monthly target"))
        item = self.tblTargets.verticalHeaderItem(1)
        item.setText(_translate("wdgTotal", "Total Gains"))
        item = self.tblTargets.verticalHeaderItem(3)
        item.setText(_translate("wdgTotal", "Accumulated target"))
        item = self.tblTargets.verticalHeaderItem(4)
        item.setText(_translate("wdgTotal", "Accumulated total gains"))
        item = self.tblTargets.horizontalHeaderItem(0)
        item.setText(_translate("wdgTotal", "January"))
        item = self.tblTargets.horizontalHeaderItem(1)
        item.setText(_translate("wdgTotal", "February"))
        item = self.tblTargets.horizontalHeaderItem(2)
        item.setText(_translate("wdgTotal", "March"))
        item = self.tblTargets.horizontalHeaderItem(3)
        item.setText(_translate("wdgTotal", "April"))
        item = self.tblTargets.horizontalHeaderItem(4)
        item.setText(_translate("wdgTotal", "May"))
        item = self.tblTargets.horizontalHeaderItem(5)
        item.setText(_translate("wdgTotal", "June"))
        item = self.tblTargets.horizontalHeaderItem(6)
        item.setText(_translate("wdgTotal", "July"))
        item = self.tblTargets.horizontalHeaderItem(7)
        item.setText(_translate("wdgTotal", "August"))
        item = self.tblTargets.horizontalHeaderItem(8)
        item.setText(_translate("wdgTotal", "September"))
        item = self.tblTargets.horizontalHeaderItem(9)
        item.setText(_translate("wdgTotal", "October"))
        item = self.tblTargets.horizontalHeaderItem(10)
        item.setText(_translate("wdgTotal", "November"))
        item = self.tblTargets.horizontalHeaderItem(11)
        item.setText(_translate("wdgTotal", "December"))
        item = self.tblTargets.horizontalHeaderItem(12)
        item.setText(_translate("wdgTotal", "Total"))
        self.tabPlus.setTabText(self.tabPlus.indexOf(self.tab_6), _translate("wdgTotal", "Consolidated Gains"))
        self.tblTargetsPlus.setSortingEnabled(False)
        item = self.tblTargetsPlus.verticalHeaderItem(0)
        item.setText(_translate("wdgTotal", "Monthly target"))
        item = self.tblTargetsPlus.verticalHeaderItem(1)
        item.setText(_translate("wdgTotal", "Total Gains"))
        item = self.tblTargetsPlus.verticalHeaderItem(2)
        item.setText(_translate("wdgTotal", "Funds Revaluation"))
        item = self.tblTargetsPlus.verticalHeaderItem(3)
        item.setText(_translate("wdgTotal", "Total"))
        item = self.tblTargetsPlus.verticalHeaderItem(5)
        item.setText(_translate("wdgTotal", "Accumulated target"))
        item = self.tblTargetsPlus.verticalHeaderItem(6)
        item.setText(_translate("wdgTotal", "Accumulated total gains"))
        item = self.tblTargetsPlus.horizontalHeaderItem(0)
        item.setText(_translate("wdgTotal", "January"))
        item = self.tblTargetsPlus.horizontalHeaderItem(1)
        item.setText(_translate("wdgTotal", "February"))
        item = self.tblTargetsPlus.horizontalHeaderItem(2)
        item.setText(_translate("wdgTotal", "March"))
        item = self.tblTargetsPlus.horizontalHeaderItem(3)
        item.setText(_translate("wdgTotal", "April"))
        item = self.tblTargetsPlus.horizontalHeaderItem(4)
        item.setText(_translate("wdgTotal", "May"))
        item = self.tblTargetsPlus.horizontalHeaderItem(5)
        item.setText(_translate("wdgTotal", "June"))
        item = self.tblTargetsPlus.horizontalHeaderItem(6)
        item.setText(_translate("wdgTotal", "July"))
        item = self.tblTargetsPlus.horizontalHeaderItem(7)
        item.setText(_translate("wdgTotal", "August"))
        item = self.tblTargetsPlus.horizontalHeaderItem(8)
        item.setText(_translate("wdgTotal", "September"))
        item = self.tblTargetsPlus.horizontalHeaderItem(9)
        item.setText(_translate("wdgTotal", "October"))
        item = self.tblTargetsPlus.horizontalHeaderItem(10)
        item.setText(_translate("wdgTotal", "November"))
        item = self.tblTargetsPlus.horizontalHeaderItem(11)
        item.setText(_translate("wdgTotal", "December"))
        item = self.tblTargetsPlus.horizontalHeaderItem(12)
        item.setText(_translate("wdgTotal", "Total"))
        self.tabPlus.setTabText(self.tabPlus.indexOf(self.tab_7), _translate("wdgTotal", "Consolidated Gains + funds revaluation"))
        self.tabData.setTabText(self.tabData.indexOf(self.tab_4), _translate("wdgTotal", "Annual target return"))
        self.tblInvestOrWork.setSortingEnabled(False)
        item = self.tblInvestOrWork.verticalHeaderItem(0)
        item.setText(_translate("wdgTotal", "Total Gains"))
        item = self.tblInvestOrWork.verticalHeaderItem(1)
        item.setText(_translate("wdgTotal", "Expenses"))
        item = self.tblInvestOrWork.verticalHeaderItem(3)
        item.setText(_translate("wdgTotal", "Total Gains - Expenses"))
        item = self.tblInvestOrWork.verticalHeaderItem(5)
        item.setText(_translate("wdgTotal", "Result"))
        item = self.tblInvestOrWork.horizontalHeaderItem(0)
        item.setText(_translate("wdgTotal", "January"))
        item = self.tblInvestOrWork.horizontalHeaderItem(1)
        item.setText(_translate("wdgTotal", "February"))
        item = self.tblInvestOrWork.horizontalHeaderItem(2)
        item.setText(_translate("wdgTotal", "March"))
        item = self.tblInvestOrWork.horizontalHeaderItem(3)
        item.setText(_translate("wdgTotal", "April"))
        item = self.tblInvestOrWork.horizontalHeaderItem(4)
        item.setText(_translate("wdgTotal", "May"))
        item = self.tblInvestOrWork.horizontalHeaderItem(5)
        item.setText(_translate("wdgTotal", "June"))
        item = self.tblInvestOrWork.horizontalHeaderItem(6)
        item.setText(_translate("wdgTotal", "July"))
        item = self.tblInvestOrWork.horizontalHeaderItem(7)
        item.setText(_translate("wdgTotal", "August"))
        item = self.tblInvestOrWork.horizontalHeaderItem(8)
        item.setText(_translate("wdgTotal", "September"))
        item = self.tblInvestOrWork.horizontalHeaderItem(9)
        item.setText(_translate("wdgTotal", "October"))
        item = self.tblInvestOrWork.horizontalHeaderItem(10)
        item.setText(_translate("wdgTotal", "November"))
        item = self.tblInvestOrWork.horizontalHeaderItem(11)
        item.setText(_translate("wdgTotal", "December"))
        item = self.tblInvestOrWork.horizontalHeaderItem(12)
        item.setText(_translate("wdgTotal", "Total"))
        self.tabData.setTabText(self.tabData.indexOf(self.tab_2), _translate("wdgTotal", "Invest or work?"))
        self.tblMakeEndsMeet.setSortingEnabled(False)
        item = self.tblMakeEndsMeet.verticalHeaderItem(0)
        item.setText(_translate("wdgTotal", "Incomes"))
        item = self.tblMakeEndsMeet.verticalHeaderItem(1)
        item.setText(_translate("wdgTotal", "Expenses"))
        item = self.tblMakeEndsMeet.verticalHeaderItem(3)
        item.setText(_translate("wdgTotal", "Incomes - Expenses"))
        item = self.tblMakeEndsMeet.verticalHeaderItem(5)
        item.setText(_translate("wdgTotal", "Result"))
        item = self.tblMakeEndsMeet.horizontalHeaderItem(0)
        item.setText(_translate("wdgTotal", "January"))
        item = self.tblMakeEndsMeet.horizontalHeaderItem(1)
        item.setText(_translate("wdgTotal", "February"))
        item = self.tblMakeEndsMeet.horizontalHeaderItem(2)
        item.setText(_translate("wdgTotal", "March"))
        item = self.tblMakeEndsMeet.horizontalHeaderItem(3)
        item.setText(_translate("wdgTotal", "April"))
        item = self.tblMakeEndsMeet.horizontalHeaderItem(4)
        item.setText(_translate("wdgTotal", "May"))
        item = self.tblMakeEndsMeet.horizontalHeaderItem(5)
        item.setText(_translate("wdgTotal", "June"))
        item = self.tblMakeEndsMeet.horizontalHeaderItem(6)
        item.setText(_translate("wdgTotal", "July"))
        item = self.tblMakeEndsMeet.horizontalHeaderItem(7)
        item.setText(_translate("wdgTotal", "August"))
        item = self.tblMakeEndsMeet.horizontalHeaderItem(8)
        item.setText(_translate("wdgTotal", "September"))
        item = self.tblMakeEndsMeet.horizontalHeaderItem(9)
        item.setText(_translate("wdgTotal", "October"))
        item = self.tblMakeEndsMeet.horizontalHeaderItem(10)
        item.setText(_translate("wdgTotal", "November"))
        item = self.tblMakeEndsMeet.horizontalHeaderItem(11)
        item.setText(_translate("wdgTotal", "December"))
        item = self.tblMakeEndsMeet.horizontalHeaderItem(12)
        item.setText(_translate("wdgTotal", "Total"))
        self.tabData.setTabText(self.tabData.indexOf(self.tab_5), _translate("wdgTotal", "Make ends meet?"))
        self.tab.setTabText(self.tab.indexOf(self.tabDatos), _translate("wdgTotal", "Data"))
        self.tab.setTabText(self.tab.indexOf(self.tabGraphic), _translate("wdgTotal", "Chart"))
        self.actionShowIncomes.setText(_translate("wdgTotal", "Show income operations"))
        self.actionShowIncomes.setToolTip(_translate("wdgTotal", "Show income operations"))
        self.actionShowExpenses.setText(_translate("wdgTotal", "Show expense operations"))
        self.actionShowDividends.setText(_translate("wdgTotal", "Show dividends"))
        self.actionShowDividends.setToolTip(_translate("wdgTotal", "Show dividends"))
        self.actionShowSellingOperations.setText(_translate("wdgTotal", "Show selling operations"))
        self.actionShowSellingOperations.setToolTip(_translate("wdgTotal", "Show selling operations"))
        self.actionShowComissions.setText(_translate("wdgTotal", "Show Comissions"))
        self.actionShowComissions.setToolTip(_translate("wdgTotal", "Show Comissions"))
        self.actionShowTaxes.setText(_translate("wdgTotal", "Show taxes"))
        self.actionShowTaxes.setToolTip(_translate("wdgTotal", "Show taxes"))
        self.actionGainsByProductType.setText(_translate("wdgTotal", "Gains by product type"))
        self.actionGainsByProductType.setToolTip(_translate("wdgTotal", "Gains by product type"))
from xulpymoney.ui.myqtablewidget import myQTableWidget
from xulpymoney.ui.wdgYear import wdgYear
import xulpymoney.images.xulpymoney_rc
