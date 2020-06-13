# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xulpymoney/ui/wdgStrategyResults.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgStrategyResults(object):
    def setupUi(self, wdgStrategyResults):
        wdgStrategyResults.setObjectName("wdgStrategyResults")
        wdgStrategyResults.resize(656, 497)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xulpymoney/bank.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        wdgStrategyResults.setWindowIcon(icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout(wdgStrategyResults)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl = QtWidgets.QLabel(wdgStrategyResults)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl.setFont(font)
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setObjectName("lbl")
        self.verticalLayout.addWidget(self.lbl)
        self.chkFinished = QtWidgets.QCheckBox(wdgStrategyResults)
        self.chkFinished.setObjectName("chkFinished")
        self.verticalLayout.addWidget(self.chkFinished)
        self.mqtwStrategies = mqtwObjects(wdgStrategyResults)
        self.mqtwStrategies.setObjectName("mqtwStrategies")
        self.verticalLayout.addWidget(self.mqtwStrategies)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.actionStrategyNew = QtWidgets.QAction(wdgStrategyResults)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/xulpymoney/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStrategyNew.setIcon(icon1)
        self.actionStrategyNew.setObjectName("actionStrategyNew")
        self.actionStrategyDelete = QtWidgets.QAction(wdgStrategyResults)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/xulpymoney/button_cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStrategyDelete.setIcon(icon2)
        self.actionStrategyDelete.setObjectName("actionStrategyDelete")
        self.actionStrategyEdit = QtWidgets.QAction(wdgStrategyResults)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/xulpymoney/editar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStrategyEdit.setIcon(icon3)
        self.actionStrategyEdit.setObjectName("actionStrategyEdit")

        self.retranslateUi(wdgStrategyResults)
        QtCore.QMetaObject.connectSlotsByName(wdgStrategyResults)

    def retranslateUi(self, wdgStrategyResults):
        _translate = QtCore.QCoreApplication.translate
        self.lbl.setText(_translate("wdgStrategyResults", "Strategies results"))
        self.chkFinished.setText(_translate("wdgStrategyResults", "Show finished strategies"))
        self.actionStrategyNew.setText(_translate("wdgStrategyResults", "New strategy"))
        self.actionStrategyNew.setToolTip(_translate("wdgStrategyResults", "New strategy"))
        self.actionStrategyDelete.setText(_translate("wdgStrategyResults", "Delete strategy"))
        self.actionStrategyDelete.setToolTip(_translate("wdgStrategyResults", "Delete strategy"))
        self.actionStrategyEdit.setText(_translate("wdgStrategyResults", "Edit strategy"))
        self.actionStrategyEdit.setToolTip(_translate("wdgStrategyResults", "Edit strategy"))
from xulpymoney.ui.myqtablewidget import mqtwObjects
import xulpymoney.images.xulpymoney_rc
