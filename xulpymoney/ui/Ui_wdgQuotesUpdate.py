# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xulpymoney/ui/wdgQuotesUpdate.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgQuotesUpdate(object):
    def setupUi(self, wdgQuotesUpdate):
        wdgQuotesUpdate.setObjectName("wdgQuotesUpdate")
        wdgQuotesUpdate.resize(1109, 795)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(wdgQuotesUpdate)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.cmdUsed = QtWidgets.QPushButton(wdgQuotesUpdate)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xulpymoney/transfer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmdUsed.setIcon(icon)
        self.cmdUsed.setObjectName("cmdUsed")
        self.horizontalLayout_3.addWidget(self.cmdUsed)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.cmdAll = QtWidgets.QPushButton(wdgQuotesUpdate)
        self.cmdAll.setIcon(icon)
        self.cmdAll.setObjectName("cmdAll")
        self.horizontalLayout_3.addWidget(self.cmdAll)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.wdgquotessaveresult = wdgQuotesSaveResult(wdgQuotesUpdate)
        self.wdgquotessaveresult.setObjectName("wdgquotessaveresult")
        self.horizontalLayout.addWidget(self.wdgquotessaveresult)
        self.txtCR2Q = QtWidgets.QTextBrowser(wdgQuotesUpdate)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setBold(True)
        font.setWeight(75)
        self.txtCR2Q.setFont(font)
        self.txtCR2Q.setUndoRedoEnabled(True)
        self.txtCR2Q.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.txtCR2Q.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.txtCR2Q.setObjectName("txtCR2Q")
        self.horizontalLayout.addWidget(self.txtCR2Q)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_6.addLayout(self.verticalLayout)

        self.retranslateUi(wdgQuotesUpdate)
        QtCore.QMetaObject.connectSlotsByName(wdgQuotesUpdate)

    def retranslateUi(self, wdgQuotesUpdate):
        _translate = QtCore.QCoreApplication.translate
        self.cmdUsed.setText(_translate("wdgQuotesUpdate", "Update used products"))
        self.cmdAll.setText(_translate("wdgQuotesUpdate", "Update all products"))
from xulpymoney.ui.wdgQuotesSaveResult import wdgQuotesSaveResult
import xulpymoney.images.xulpymoney_rc
