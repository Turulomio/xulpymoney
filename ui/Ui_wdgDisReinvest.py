# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/wdgDisReinvest.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_wdgDisReinvest(object):
    def setupUi(self, wdgDisReinvest):
        wdgDisReinvest.setObjectName("wdgDisReinvest")
        wdgDisReinvest.resize(818, 585)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xulpymoney/tools-wizard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        wdgDisReinvest.setWindowIcon(icon)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(wdgDisReinvest)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblTitulo = QtWidgets.QLabel(wdgDisReinvest)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setStyleSheet("color: rgb(0, 128, 0);")
        self.lblTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitulo.setObjectName("lblTitulo")
        self.verticalLayout_3.addWidget(self.lblTitulo)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.grp = QtWidgets.QGroupBox(wdgDisReinvest)
        self.grp.setTitle("")
        self.grp.setObjectName("grp")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.grp)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radRe = QtWidgets.QRadioButton(self.grp)
        self.radRe.setChecked(True)
        self.radRe.setObjectName("radRe")
        self.horizontalLayout.addWidget(self.radRe)
        self.radDes = QtWidgets.QRadioButton(self.grp)
        self.radDes.setChecked(False)
        self.radDes.setObjectName("radDes")
        self.horizontalLayout.addWidget(self.radDes)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox = QtWidgets.QGroupBox(self.grp)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lblSimulacion = QtWidgets.QLabel(self.groupBox)
        self.lblSimulacion.setObjectName("lblSimulacion")
        self.horizontalLayout_12.addWidget(self.lblSimulacion)
        self.txtSimulacion = myQLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtSimulacion.sizePolicy().hasHeightForWidth())
        self.txtSimulacion.setSizePolicy(sizePolicy)
        self.txtSimulacion.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtSimulacion.setObjectName("txtSimulacion")
        self.horizontalLayout_12.addWidget(self.txtSimulacion)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lblValor = QtWidgets.QLabel(self.groupBox)
        self.lblValor.setObjectName("lblValor")
        self.horizontalLayout_5.addWidget(self.lblValor)
        self.txtValorAccion = myQLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtValorAccion.sizePolicy().hasHeightForWidth())
        self.txtValorAccion.setSizePolicy(sizePolicy)
        self.txtValorAccion.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtValorAccion.setObjectName("txtValorAccion")
        self.horizontalLayout_5.addWidget(self.txtValorAccion)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.txtComision = myQLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtComision.sizePolicy().hasHeightForWidth())
        self.txtComision.setSizePolicy(sizePolicy)
        self.txtComision.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtComision.setObjectName("txtComision")
        self.horizontalLayout_4.addWidget(self.txtComision)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_11.addWidget(self.label_5)
        self.txtAcciones = myQLineEdit(self.groupBox)
        self.txtAcciones.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtAcciones.sizePolicy().hasHeightForWidth())
        self.txtAcciones.setSizePolicy(sizePolicy)
        self.txtAcciones.setText("")
        self.txtAcciones.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtAcciones.setObjectName("txtAcciones")
        self.horizontalLayout_11.addWidget(self.txtAcciones)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.txtImporte = myQLineEdit(self.groupBox)
        self.txtImporte.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtImporte.sizePolicy().hasHeightForWidth())
        self.txtImporte.setSizePolicy(sizePolicy)
        self.txtImporte.setText("")
        self.txtImporte.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtImporte.setObjectName("txtImporte")
        self.horizontalLayout_3.addWidget(self.txtImporte)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cmdOrder = QtWidgets.QPushButton(self.grp)
        self.cmdOrder.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/xulpymoney/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmdOrder.setIcon(icon1)
        self.cmdOrder.setObjectName("cmdOrder")
        self.horizontalLayout_2.addWidget(self.cmdOrder)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.cmd = QtWidgets.QPushButton(self.grp)
        self.cmd.setIcon(icon)
        self.cmd.setObjectName("cmd")
        self.horizontalLayout_2.addWidget(self.cmd)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.horizontalLayout_8.addWidget(self.grp)
        self.cmdGraph = QtWidgets.QToolButton(wdgDisReinvest)
        self.cmdGraph.setEnabled(False)
        self.cmdGraph.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/xulpymoney/report.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmdGraph.setIcon(icon2)
        self.cmdGraph.setIconSize(QtCore.QSize(64, 64))
        self.cmdGraph.setObjectName("cmdGraph")
        self.horizontalLayout_8.addWidget(self.cmdGraph)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.tabAB = QtWidgets.QTabWidget(wdgDisReinvest)
        self.tabAB.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabAB.setObjectName("tabAB")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.tabOpAcHi = QtWidgets.QTabWidget(self.tab_5)
        self.tabOpAcHi.setObjectName("tabOpAcHi")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.tab_9)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.tblOperaciones = myQTableWidget(self.tab_9)
        self.tblOperaciones.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblOperaciones.setAlternatingRowColors(True)
        self.tblOperaciones.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tblOperaciones.setObjectName("tblOperaciones")
        self.tblOperaciones.setColumnCount(8)
        self.tblOperaciones.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblOperaciones.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblOperaciones.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblOperaciones.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblOperaciones.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblOperaciones.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblOperaciones.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblOperaciones.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblOperaciones.setHorizontalHeaderItem(7, item)
        self.tblOperaciones.verticalHeader().setVisible(False)
        self.horizontalLayout_17.addWidget(self.tblOperaciones)
        self.tabOpAcHi.addTab(self.tab_9, "")
        self.Situac_2 = QtWidgets.QWidget()
        self.Situac_2.setObjectName("Situac_2")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.Situac_2)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.tblInvestmentsActualDespues = myQTableWidget(self.Situac_2)
        self.tblInvestmentsActualDespues.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblInvestmentsActualDespues.setAlternatingRowColors(True)
        self.tblInvestmentsActualDespues.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tblInvestmentsActualDespues.setObjectName("tblInvestmentsActualDespues")
        self.tblInvestmentsActualDespues.setColumnCount(9)
        self.tblInvestmentsActualDespues.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualDespues.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualDespues.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualDespues.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualDespues.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualDespues.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualDespues.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualDespues.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualDespues.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualDespues.setHorizontalHeaderItem(8, item)
        self.tblInvestmentsActualDespues.verticalHeader().setVisible(False)
        self.horizontalLayout_15.addWidget(self.tblInvestmentsActualDespues)
        self.tabOpAcHi.addTab(self.Situac_2, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.tab_8)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.tblInvestmentsHistoricas = myQTableWidget(self.tab_8)
        self.tblInvestmentsHistoricas.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblInvestmentsHistoricas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblInvestmentsHistoricas.setAlternatingRowColors(True)
        self.tblInvestmentsHistoricas.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tblInvestmentsHistoricas.setObjectName("tblInvestmentsHistoricas")
        self.tblInvestmentsHistoricas.setColumnCount(11)
        self.tblInvestmentsHistoricas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsHistoricas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsHistoricas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsHistoricas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsHistoricas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsHistoricas.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsHistoricas.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsHistoricas.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsHistoricas.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsHistoricas.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsHistoricas.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsHistoricas.setHorizontalHeaderItem(10, item)
        self.tblInvestmentsHistoricas.verticalHeader().setVisible(False)
        self.horizontalLayout_16.addWidget(self.tblInvestmentsHistoricas)
        self.tabOpAcHi.addTab(self.tab_8, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.tblGainsAfter = myQTableWidget(self.tab_2)
        self.tblGainsAfter.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblGainsAfter.setAlternatingRowColors(True)
        self.tblGainsAfter.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblGainsAfter.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblGainsAfter.setObjectName("tblGainsAfter")
        self.tblGainsAfter.setColumnCount(3)
        self.tblGainsAfter.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblGainsAfter.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblGainsAfter.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblGainsAfter.setHorizontalHeaderItem(2, item)
        self.tblGainsAfter.verticalHeader().setVisible(False)
        self.horizontalLayout_10.addWidget(self.tblGainsAfter)
        self.tabOpAcHi.addTab(self.tab_2, "")
        self.horizontalLayout_18.addWidget(self.tabOpAcHi)
        self.tabAB.addTab(self.tab_5, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.tab_11)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.tabResultados_3 = QtWidgets.QTabWidget(self.tab_11)
        self.tabResultados_3.setObjectName("tabResultados_3")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.tab_12)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.tblInvestmentsActualDespuesAt = myQTableWidget(self.tab_12)
        self.tblInvestmentsActualDespuesAt.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblInvestmentsActualDespuesAt.setAlternatingRowColors(True)
        self.tblInvestmentsActualDespuesAt.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tblInvestmentsActualDespuesAt.setObjectName("tblInvestmentsActualDespuesAt")
        self.tblInvestmentsActualDespuesAt.setColumnCount(9)
        self.tblInvestmentsActualDespuesAt.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualDespuesAt.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualDespuesAt.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualDespuesAt.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualDespuesAt.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualDespuesAt.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualDespuesAt.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualDespuesAt.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualDespuesAt.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualDespuesAt.setHorizontalHeaderItem(8, item)
        self.tblInvestmentsActualDespuesAt.verticalHeader().setVisible(False)
        self.horizontalLayout_23.addWidget(self.tblInvestmentsActualDespuesAt)
        self.tabResultados_3.addTab(self.tab_12, "")
        self.horizontalLayout_25.addWidget(self.tabResultados_3)
        self.tabAB.addTab(self.tab_11, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.tabResultados_2 = QtWidgets.QTabWidget(self.tab_3)
        self.tabResultados_2.setObjectName("tabResultados_2")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.tab_7)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.tblInvestmentsActualAntesAt = myQTableWidget(self.tab_7)
        self.tblInvestmentsActualAntesAt.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblInvestmentsActualAntesAt.setAlternatingRowColors(True)
        self.tblInvestmentsActualAntesAt.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tblInvestmentsActualAntesAt.setObjectName("tblInvestmentsActualAntesAt")
        self.tblInvestmentsActualAntesAt.setColumnCount(9)
        self.tblInvestmentsActualAntesAt.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualAntesAt.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualAntesAt.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualAntesAt.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualAntesAt.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualAntesAt.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualAntesAt.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualAntesAt.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualAntesAt.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualAntesAt.setHorizontalHeaderItem(8, item)
        self.tblInvestmentsActualAntesAt.verticalHeader().setVisible(False)
        self.horizontalLayout_20.addWidget(self.tblInvestmentsActualAntesAt)
        self.tabResultados_2.addTab(self.tab_7, "")
        self.horizontalLayout_22.addWidget(self.tabResultados_2)
        self.tabAB.addTab(self.tab_3, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.tab_6)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.tabResultados = QtWidgets.QTabWidget(self.tab_6)
        self.tabResultados.setObjectName("tabResultados")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.tblInvestmentsActualAntes = myQTableWidget(self.tab_4)
        self.tblInvestmentsActualAntes.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblInvestmentsActualAntes.setAlternatingRowColors(True)
        self.tblInvestmentsActualAntes.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tblInvestmentsActualAntes.setObjectName("tblInvestmentsActualAntes")
        self.tblInvestmentsActualAntes.setColumnCount(9)
        self.tblInvestmentsActualAntes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualAntes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualAntes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualAntes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualAntes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualAntes.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualAntes.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualAntes.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualAntes.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestmentsActualAntes.setHorizontalHeaderItem(8, item)
        self.tblInvestmentsActualAntes.verticalHeader().setVisible(False)
        self.horizontalLayout_13.addWidget(self.tblInvestmentsActualAntes)
        self.tabResultados.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.tblGainsBefore = myQTableWidget(self.tab)
        self.tblGainsBefore.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblGainsBefore.setAlternatingRowColors(True)
        self.tblGainsBefore.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblGainsBefore.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblGainsBefore.setObjectName("tblGainsBefore")
        self.tblGainsBefore.setColumnCount(3)
        self.tblGainsBefore.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblGainsBefore.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblGainsBefore.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblGainsBefore.setHorizontalHeaderItem(2, item)
        self.tblGainsBefore.verticalHeader().setVisible(False)
        self.horizontalLayout_9.addWidget(self.tblGainsBefore)
        self.tabResultados.addTab(self.tab, "")
        self.horizontalLayout_19.addWidget(self.tabResultados)
        self.tabAB.addTab(self.tab_6, "")
        self.verticalLayout_3.addWidget(self.tabAB)
        self.horizontalLayout_14.addLayout(self.verticalLayout_3)

        self.retranslateUi(wdgDisReinvest)
        self.tabAB.setCurrentIndex(3)
        self.tabOpAcHi.setCurrentIndex(1)
        self.tabResultados_3.setCurrentIndex(0)
        self.tabResultados_2.setCurrentIndex(0)
        self.tabResultados.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(wdgDisReinvest)

    def retranslateUi(self, wdgDisReinvest):
        _translate = QtCore.QCoreApplication.translate
        self.radRe.setText(_translate("wdgDisReinvest", "Reinvest simulation"))
        self.radDes.setText(_translate("wdgDisReinvest", "Disinvest simulation"))
        self.groupBox.setTitle(_translate("wdgDisReinvest", "Operation data"))
        self.txtSimulacion.setText(_translate("wdgDisReinvest", "1000"))
        self.txtValorAccion.setText(_translate("wdgDisReinvest", "0"))
        self.label_3.setText(_translate("wdgDisReinvest", "Bank comission"))
        self.txtComision.setText(_translate("wdgDisReinvest", "10"))
        self.label_5.setText(_translate("wdgDisReinvest", "Shares number"))
        self.label_2.setText(_translate("wdgDisReinvest", "Amount"))
        self.cmdOrder.setText(_translate("wdgDisReinvest", "Add order annotations"))
        self.cmd.setText(_translate("wdgDisReinvest", "Make simulation"))
        self.cmdGraph.setToolTip(_translate("wdgDisReinvest", "Show operations in a graph"))
        item = self.tblOperaciones.horizontalHeaderItem(0)
        item.setText(_translate("wdgDisReinvest", "Id"))
        item = self.tblOperaciones.horizontalHeaderItem(1)
        item.setText(_translate("wdgDisReinvest", "Date"))
        item = self.tblOperaciones.horizontalHeaderItem(2)
        item.setText(_translate("wdgDisReinvest", "Operation type"))
        item = self.tblOperaciones.horizontalHeaderItem(3)
        item.setText(_translate("wdgDisReinvest", "Shares"))
        item = self.tblOperaciones.horizontalHeaderItem(4)
        item.setText(_translate("wdgDisReinvest", "Price"))
        item = self.tblOperaciones.horizontalHeaderItem(5)
        item.setText(_translate("wdgDisReinvest", "Balance"))
        item = self.tblOperaciones.horizontalHeaderItem(6)
        item.setText(_translate("wdgDisReinvest", "Comission"))
        item = self.tblOperaciones.horizontalHeaderItem(7)
        item.setText(_translate("wdgDisReinvest", "Taxes"))
        self.tabOpAcHi.setTabText(self.tabOpAcHi.indexOf(self.tab_9), _translate("wdgDisReinvest", "Investment operations"))
        item = self.tblInvestmentsActualDespues.horizontalHeaderItem(0)
        item.setText(_translate("wdgDisReinvest", "Date"))
        item = self.tblInvestmentsActualDespues.horizontalHeaderItem(1)
        item.setText(_translate("wdgDisReinvest", "Shares"))
        item = self.tblInvestmentsActualDespues.horizontalHeaderItem(2)
        item.setText(_translate("wdgDisReinvest", "Price"))
        item = self.tblInvestmentsActualDespues.horizontalHeaderItem(3)
        item.setText(_translate("wdgDisReinvest", "Balance"))
        item = self.tblInvestmentsActualDespues.horizontalHeaderItem(4)
        item.setText(_translate("wdgDisReinvest", "Pending"))
        item = self.tblInvestmentsActualDespues.horizontalHeaderItem(5)
        item.setText(_translate("wdgDisReinvest", "% Annual"))
        item = self.tblInvestmentsActualDespues.horizontalHeaderItem(6)
        item.setText(_translate("wdgDisReinvest", "% APR"))
        item = self.tblInvestmentsActualDespues.horizontalHeaderItem(7)
        item.setText(_translate("wdgDisReinvest", "% Total"))
        item = self.tblInvestmentsActualDespues.horizontalHeaderItem(8)
        item.setText(_translate("wdgDisReinvest", "Benchmark"))
        self.tabOpAcHi.setTabText(self.tabOpAcHi.indexOf(self.Situac_2), _translate("wdgDisReinvest", "Investment current state"))
        item = self.tblInvestmentsHistoricas.horizontalHeaderItem(0)
        item.setText(_translate("wdgDisReinvest", "Date"))
        item = self.tblInvestmentsHistoricas.horizontalHeaderItem(1)
        item.setText(_translate("wdgDisReinvest", "Years"))
        item = self.tblInvestmentsHistoricas.horizontalHeaderItem(2)
        item.setText(_translate("wdgDisReinvest", "Investment"))
        item = self.tblInvestmentsHistoricas.horizontalHeaderItem(3)
        item.setText(_translate("wdgDisReinvest", "Operation type"))
        item = self.tblInvestmentsHistoricas.horizontalHeaderItem(4)
        item.setText(_translate("wdgDisReinvest", "Initial balance"))
        item = self.tblInvestmentsHistoricas.horizontalHeaderItem(5)
        item.setText(_translate("wdgDisReinvest", "Final balance"))
        item = self.tblInvestmentsHistoricas.horizontalHeaderItem(6)
        item.setText(_translate("wdgDisReinvest", "Gross"))
        item = self.tblInvestmentsHistoricas.horizontalHeaderItem(7)
        item.setText(_translate("wdgDisReinvest", "Comissions"))
        item = self.tblInvestmentsHistoricas.horizontalHeaderItem(8)
        item.setText(_translate("wdgDisReinvest", "Taxes"))
        item = self.tblInvestmentsHistoricas.horizontalHeaderItem(9)
        item.setText(_translate("wdgDisReinvest", "Net"))
        item = self.tblInvestmentsHistoricas.horizontalHeaderItem(10)
        item.setText(_translate("wdgDisReinvest", "% Total"))
        self.tabOpAcHi.setTabText(self.tabOpAcHi.indexOf(self.tab_8), _translate("wdgDisReinvest", "Historical operations"))
        item = self.tblGainsAfter.horizontalHeaderItem(0)
        item.setText(_translate("wdgDisReinvest", "% Gains"))
        item = self.tblGainsAfter.horizontalHeaderItem(1)
        item.setText(_translate("wdgDisReinvest", "Price"))
        item = self.tblGainsAfter.horizontalHeaderItem(2)
        item.setText(_translate("wdgDisReinvest", "Gains"))
        self.tabOpAcHi.setTabText(self.tabOpAcHi.indexOf(self.tab_2), _translate("wdgDisReinvest", "Gains estimations"))
        self.tabAB.setTabText(self.tabAB.indexOf(self.tab_5), _translate("wdgDisReinvest", "After"))
        item = self.tblInvestmentsActualDespuesAt.horizontalHeaderItem(0)
        item.setText(_translate("wdgDisReinvest", "Date"))
        item = self.tblInvestmentsActualDespuesAt.horizontalHeaderItem(1)
        item.setText(_translate("wdgDisReinvest", "Shares"))
        item = self.tblInvestmentsActualDespuesAt.horizontalHeaderItem(2)
        item.setText(_translate("wdgDisReinvest", "Price"))
        item = self.tblInvestmentsActualDespuesAt.horizontalHeaderItem(3)
        item.setText(_translate("wdgDisReinvest", "Balance"))
        item = self.tblInvestmentsActualDespuesAt.horizontalHeaderItem(4)
        item.setText(_translate("wdgDisReinvest", "Pending"))
        item = self.tblInvestmentsActualDespuesAt.horizontalHeaderItem(5)
        item.setText(_translate("wdgDisReinvest", "% Year to Date"))
        item = self.tblInvestmentsActualDespuesAt.horizontalHeaderItem(6)
        item.setText(_translate("wdgDisReinvest", "% APR"))
        item = self.tblInvestmentsActualDespuesAt.horizontalHeaderItem(7)
        item.setText(_translate("wdgDisReinvest", "% Total"))
        item = self.tblInvestmentsActualDespuesAt.horizontalHeaderItem(8)
        item.setText(_translate("wdgDisReinvest", "Benchmark"))
        self.tabResultados_3.setTabText(self.tabResultados_3.indexOf(self.tab_12), _translate("wdgDisReinvest", "Investment situation"))
        self.tabAB.setTabText(self.tabAB.indexOf(self.tab_11), _translate("wdgDisReinvest", "After at"))
        item = self.tblInvestmentsActualAntesAt.horizontalHeaderItem(0)
        item.setText(_translate("wdgDisReinvest", "Date"))
        item = self.tblInvestmentsActualAntesAt.horizontalHeaderItem(1)
        item.setText(_translate("wdgDisReinvest", "Shares"))
        item = self.tblInvestmentsActualAntesAt.horizontalHeaderItem(2)
        item.setText(_translate("wdgDisReinvest", "Price"))
        item = self.tblInvestmentsActualAntesAt.horizontalHeaderItem(3)
        item.setText(_translate("wdgDisReinvest", "Balance"))
        item = self.tblInvestmentsActualAntesAt.horizontalHeaderItem(4)
        item.setText(_translate("wdgDisReinvest", "Pending"))
        item = self.tblInvestmentsActualAntesAt.horizontalHeaderItem(5)
        item.setText(_translate("wdgDisReinvest", "% Year to Date"))
        item = self.tblInvestmentsActualAntesAt.horizontalHeaderItem(6)
        item.setText(_translate("wdgDisReinvest", "% APR"))
        item = self.tblInvestmentsActualAntesAt.horizontalHeaderItem(7)
        item.setText(_translate("wdgDisReinvest", "% Total"))
        item = self.tblInvestmentsActualAntesAt.horizontalHeaderItem(8)
        item.setText(_translate("wdgDisReinvest", "Benchmark"))
        self.tabResultados_2.setTabText(self.tabResultados_2.indexOf(self.tab_7), _translate("wdgDisReinvest", "Investment situation"))
        self.tabAB.setTabText(self.tabAB.indexOf(self.tab_3), _translate("wdgDisReinvest", "Before at"))
        item = self.tblInvestmentsActualAntes.horizontalHeaderItem(0)
        item.setText(_translate("wdgDisReinvest", "Date"))
        item = self.tblInvestmentsActualAntes.horizontalHeaderItem(1)
        item.setText(_translate("wdgDisReinvest", "Shares"))
        item = self.tblInvestmentsActualAntes.horizontalHeaderItem(2)
        item.setText(_translate("wdgDisReinvest", "Price"))
        item = self.tblInvestmentsActualAntes.horizontalHeaderItem(3)
        item.setText(_translate("wdgDisReinvest", "Balance"))
        item = self.tblInvestmentsActualAntes.horizontalHeaderItem(4)
        item.setText(_translate("wdgDisReinvest", "Pending"))
        item = self.tblInvestmentsActualAntes.horizontalHeaderItem(5)
        item.setText(_translate("wdgDisReinvest", "% Year to Date"))
        item = self.tblInvestmentsActualAntes.horizontalHeaderItem(6)
        item.setText(_translate("wdgDisReinvest", "% APR"))
        item = self.tblInvestmentsActualAntes.horizontalHeaderItem(7)
        item.setText(_translate("wdgDisReinvest", "% Total"))
        item = self.tblInvestmentsActualAntes.horizontalHeaderItem(8)
        item.setText(_translate("wdgDisReinvest", "Benchmark"))
        self.tabResultados.setTabText(self.tabResultados.indexOf(self.tab_4), _translate("wdgDisReinvest", "Investment situation"))
        item = self.tblGainsBefore.horizontalHeaderItem(0)
        item.setText(_translate("wdgDisReinvest", "% Gains"))
        item = self.tblGainsBefore.horizontalHeaderItem(1)
        item.setText(_translate("wdgDisReinvest", "Price"))
        item = self.tblGainsBefore.horizontalHeaderItem(2)
        item.setText(_translate("wdgDisReinvest", "Gains"))
        self.tabResultados.setTabText(self.tabResultados.indexOf(self.tab), _translate("wdgDisReinvest", "Gains estimations"))
        self.tabAB.setTabText(self.tabAB.indexOf(self.tab_6), _translate("wdgDisReinvest", "Before"))

from myqlineedit import myQLineEdit
from myqtablewidget import myQTableWidget
import xulpymoney_rc
