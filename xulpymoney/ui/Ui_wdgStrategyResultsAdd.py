# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xulpymoney/ui/wdgStrategyResultsAdd.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgStrategyResultsAdd(object):
    def setupUi(self, wdgStrategyResultsAdd):
        wdgStrategyResultsAdd.setObjectName("wdgStrategyResultsAdd")
        wdgStrategyResultsAdd.resize(1048, 499)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(wdgStrategyResultsAdd)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblTitulo = QtWidgets.QLabel(wdgStrategyResultsAdd)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitulo.setObjectName("lblTitulo")
        self.verticalLayout.addWidget(self.lblTitulo)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.lblPixmap = QtWidgets.QLabel(wdgStrategyResultsAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblPixmap.sizePolicy().hasHeightForWidth())
        self.lblPixmap.setSizePolicy(sizePolicy)
        self.lblPixmap.setMinimumSize(QtCore.QSize(48, 48))
        self.lblPixmap.setMaximumSize(QtCore.QSize(48, 48))
        self.lblPixmap.setPixmap(QtGui.QPixmap(":/xulpymoney/tools-wizard.png"))
        self.lblPixmap.setScaledContents(True)
        self.lblPixmap.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPixmap.setObjectName("lblPixmap")
        self.horizontalLayout_4.addWidget(self.lblPixmap)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(wdgStrategyResultsAdd)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.txtName = QtWidgets.QLineEdit(wdgStrategyResultsAdd)
        self.txtName.setObjectName("txtName")
        self.horizontalLayout_5.addWidget(self.txtName)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.groupBox = QtWidgets.QGroupBox(wdgStrategyResultsAdd)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.wdgDtFrom = wdgDatetime(self.groupBox)
        self.wdgDtFrom.setObjectName("wdgDtFrom")
        self.verticalLayout_2.addWidget(self.wdgDtFrom)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(wdgStrategyResultsAdd)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.wdgDtTo = wdgDatetime(self.groupBox_2)
        self.wdgDtTo.setObjectName("wdgDtTo")
        self.horizontalLayout.addWidget(self.wdgDtTo)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_2 = QtWidgets.QLabel(wdgStrategyResultsAdd)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_8.addWidget(self.label_2)
        self.cmsInvestments = cmbManagerSelector(wdgStrategyResultsAdd)
        self.cmsInvestments.setObjectName("cmsInvestments")
        self.horizontalLayout_8.addWidget(self.cmsInvestments)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.cmdSave = QtWidgets.QPushButton(wdgStrategyResultsAdd)
        self.cmdSave.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xulpymoney/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmdSave.setIcon(icon)
        self.cmdSave.setObjectName("cmdSave")
        self.verticalLayout.addWidget(self.cmdSave)
        self.tab_4 = QtWidgets.QTabWidget(wdgStrategyResultsAdd)
        self.tab_4.setObjectName("tab_4")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.mqtwCurrent = mqtwObjects(self.tab)
        self.mqtwCurrent.setObjectName("mqtwCurrent")
        self.horizontalLayout_3.addWidget(self.mqtwCurrent)
        self.tab_4.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.mqtwHistorical = mqtwObjects(self.tab_2)
        self.mqtwHistorical.setObjectName("mqtwHistorical")
        self.horizontalLayout_6.addWidget(self.mqtwHistorical)
        self.tab_4.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.mqtwDividends = mqtwObjects(self.tab_3)
        self.mqtwDividends.setObjectName("mqtwDividends")
        self.horizontalLayout_7.addWidget(self.mqtwDividends)
        self.tab_4.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tab_4)
        self.lblResults = QtWidgets.QLabel(wdgStrategyResultsAdd)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblResults.setFont(font)
        self.lblResults.setAlignment(QtCore.Qt.AlignCenter)
        self.lblResults.setObjectName("lblResults")
        self.verticalLayout.addWidget(self.lblResults)
        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(wdgStrategyResultsAdd)
        self.tab_4.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(wdgStrategyResultsAdd)

    def retranslateUi(self, wdgStrategyResultsAdd):
        _translate = QtCore.QCoreApplication.translate
        wdgStrategyResultsAdd.setWindowTitle(_translate("wdgStrategyResultsAdd", "Form"))
        self.lblTitulo.setText(_translate("wdgStrategyResultsAdd", "Strategy results"))
        self.label.setText(_translate("wdgStrategyResultsAdd", "Strategy name"))
        self.groupBox.setTitle(_translate("wdgStrategyResultsAdd", "From"))
        self.groupBox_2.setTitle(_translate("wdgStrategyResultsAdd", "To"))
        self.label_2.setText(_translate("wdgStrategyResultsAdd", "Select strategy investments"))
        self.cmdSave.setText(_translate("wdgStrategyResultsAdd", "Save strategy"))
        self.tab_4.setTabText(self.tab_4.indexOf(self.tab), _translate("wdgStrategyResultsAdd", "Current operations"))
        self.tab_4.setTabText(self.tab_4.indexOf(self.tab_2), _translate("wdgStrategyResultsAdd", "Historical Operations"))
        self.tab_4.setTabText(self.tab_4.indexOf(self.tab_3), _translate("wdgStrategyResultsAdd", "Dividends"))
from xulpymoney.ui.frmSelector import cmbManagerSelector
from xulpymoney.ui.myqtablewidget import mqtwObjects
from xulpymoney.ui.wdgDatetime import wdgDatetime
import xulpymoney.images.xulpymoney_rc
