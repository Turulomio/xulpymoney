# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xulpymoney/ui/wdgStrategySpreads.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgStrategySpreads(object):
    def setupUi(self, wdgStrategySpreads):
        wdgStrategySpreads.setObjectName("wdgStrategySpreads")
        wdgStrategySpreads.resize(1048, 499)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(wdgStrategySpreads)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblTitulo = QtWidgets.QLabel(wdgStrategySpreads)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitulo.setObjectName("lblTitulo")
        self.verticalLayout_2.addWidget(self.lblTitulo)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.lblPixmap = QtWidgets.QLabel(wdgStrategySpreads)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblPixmap.sizePolicy().hasHeightForWidth())
        self.lblPixmap.setSizePolicy(sizePolicy)
        self.lblPixmap.setMinimumSize(QtCore.QSize(48, 48))
        self.lblPixmap.setMaximumSize(QtCore.QSize(48, 48))
        self.lblPixmap.setPixmap(QtGui.QPixmap(":/xulpymoney/compare.png"))
        self.lblPixmap.setScaledContents(True)
        self.lblPixmap.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPixmap.setObjectName("lblPixmap")
        self.horizontalLayout_4.addWidget(self.lblPixmap)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.groupBox = QtWidgets.QGroupBox(wdgStrategySpreads)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.wdgA = wdgProductSelector(self.groupBox)
        self.wdgA.setObjectName("wdgA")
        self.horizontalLayout.addWidget(self.wdgA)
        self.wdgIndexA = wdgProductSelector(self.groupBox)
        self.wdgIndexA.setObjectName("wdgIndexA")
        self.horizontalLayout.addWidget(self.wdgIndexA)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.wdgB = wdgProductSelector(self.groupBox)
        self.wdgB.setObjectName("wdgB")
        self.horizontalLayout_2.addWidget(self.wdgB)
        self.wdgIndexB = wdgProductSelector(self.groupBox)
        self.wdgIndexB.setObjectName("wdgIndexB")
        self.horizontalLayout_2.addWidget(self.wdgIndexB)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.mqtwInformation = QtWidgets.QWidget(wdgStrategySpreads)
        self.mqtwInformation.setObjectName("mqtwInformation")
        self.verticalLayout_2.addWidget(self.mqtwInformation)
        self.tabWidget = QtWidgets.QTabWidget(wdgStrategySpreads)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.retranslateUi(wdgStrategySpreads)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(wdgStrategySpreads)

    def retranslateUi(self, wdgStrategySpreads):
        _translate = QtCore.QCoreApplication.translate
        wdgStrategySpreads.setWindowTitle(_translate("wdgStrategySpreads", "Form"))
        self.lblTitulo.setText(_translate("wdgStrategySpreads", "Spreads strategy"))
        self.groupBox.setTitle(_translate("wdgStrategySpreads", "Analysis products"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("wdgStrategySpreads", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("wdgStrategySpreads", "Tab 2"))
from xulpymoney.ui.wdgProductSelector import wdgProductSelector
import xulpymoney.images.xulpymoney_rc