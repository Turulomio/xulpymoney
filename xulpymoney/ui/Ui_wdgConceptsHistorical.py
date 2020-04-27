# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xulpymoney/ui/wdgConceptsHistorical.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgConceptsHistorical(object):
    def setupUi(self, wdgConceptsHistorical):
        wdgConceptsHistorical.setObjectName("wdgConceptsHistorical")
        wdgConceptsHistorical.resize(1280, 612)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xulpymoney/history.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        wdgConceptsHistorical.setWindowIcon(icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout(wdgConceptsHistorical)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tab = QtWidgets.QTabWidget(wdgConceptsHistorical)
        self.tab.setTabsClosable(True)
        self.tab.setObjectName("tab")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mqtwReport = mqtw(self.widget)
        self.mqtwReport.setObjectName("mqtwReport")
        self.horizontalLayout_2.addWidget(self.mqtwReport)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/xulpymoney/hucha.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab.addTab(self.widget, icon1, "")
        self.verticalLayout.addWidget(self.tab)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.actionShowMonth = QtWidgets.QAction(wdgConceptsHistorical)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/xulpymoney/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShowMonth.setIcon(icon2)
        self.actionShowMonth.setObjectName("actionShowMonth")
        self.actionShowYear = QtWidgets.QAction(wdgConceptsHistorical)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/xulpymoney/document-preview-archive.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShowYear.setIcon(icon3)
        self.actionShowYear.setObjectName("actionShowYear")

        self.retranslateUi(wdgConceptsHistorical)
        self.tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(wdgConceptsHistorical)

    def retranslateUi(self, wdgConceptsHistorical):
        _translate = QtCore.QCoreApplication.translate
        wdgConceptsHistorical.setWindowTitle(_translate("wdgConceptsHistorical", "Historical concepts report"))
        self.tab.setTabText(self.tab.indexOf(self.widget), _translate("wdgConceptsHistorical", "Historical report"))
        self.actionShowMonth.setText(_translate("wdgConceptsHistorical", "Show month operations"))
        self.actionShowMonth.setToolTip(_translate("wdgConceptsHistorical", "Show month operations"))
        self.actionShowYear.setText(_translate("wdgConceptsHistorical", "Show year operations"))
        self.actionShowYear.setToolTip(_translate("wdgConceptsHistorical", "Show year operations"))
from xulpymoney.ui.myqtablewidget import mqtw
import xulpymoney.images.xulpymoney_rc
