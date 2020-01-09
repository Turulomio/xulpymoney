# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xulpymoney/ui/frmCreditCardsAdd.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmCreditCardsAdd(object):
    def setupUi(self, frmCreditCardsAdd):
        frmCreditCardsAdd.setObjectName("frmCreditCardsAdd")
        frmCreditCardsAdd.setWindowModality(QtCore.Qt.WindowModal)
        frmCreditCardsAdd.resize(426, 250)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xulpymoney/visa2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmCreditCardsAdd.setWindowIcon(icon)
        frmCreditCardsAdd.setModal(True)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(frmCreditCardsAdd)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblTitle = QtWidgets.QLabel(frmCreditCardsAdd)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setStyleSheet("color: rgb(0, 128, 0);")
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.verticalLayout.addWidget(self.lblTitle)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(frmCreditCardsAdd)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.txtCreditCard = QtWidgets.QLineEdit(frmCreditCardsAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtCreditCard.sizePolicy().hasHeightForWidth())
        self.txtCreditCard.setSizePolicy(sizePolicy)
        self.txtCreditCard.setObjectName("txtCreditCard")
        self.horizontalLayout_5.addWidget(self.txtCreditCard)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chkDelayed = QtWidgets.QCheckBox(frmCreditCardsAdd)
        self.chkDelayed.setObjectName("chkDelayed")
        self.horizontalLayout.addWidget(self.chkDelayed)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(frmCreditCardsAdd)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.txtMaximum = myQLineEdit(frmCreditCardsAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtMaximum.sizePolicy().hasHeightForWidth())
        self.txtMaximum.setSizePolicy(sizePolicy)
        self.txtMaximum.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtMaximum.setObjectName("txtMaximum")
        self.horizontalLayout_7.addWidget(self.txtMaximum)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(frmCreditCardsAdd)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.txtNumber = myQLineEditValidatingCreditCard(frmCreditCardsAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtNumber.sizePolicy().hasHeightForWidth())
        self.txtNumber.setSizePolicy(sizePolicy)
        self.txtNumber.setObjectName("txtNumber")
        self.horizontalLayout_4.addWidget(self.txtNumber)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.cmd = QtWidgets.QPushButton(frmCreditCardsAdd)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/xulpymoney/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmd.setIcon(icon1)
        self.cmd.setObjectName("cmd")
        self.verticalLayout.addWidget(self.cmd)
        self.horizontalLayout_8.addLayout(self.verticalLayout)

        self.retranslateUi(frmCreditCardsAdd)
        QtCore.QMetaObject.connectSlotsByName(frmCreditCardsAdd)

    def retranslateUi(self, frmCreditCardsAdd):
        _translate = QtCore.QCoreApplication.translate
        frmCreditCardsAdd.setWindowTitle(_translate("frmCreditCardsAdd", "New credit card"))
        self.label_5.setText(_translate("frmCreditCardsAdd", "Credit card name"))
        self.chkDelayed.setText(_translate("frmCreditCardsAdd", "Has it delayed payment?"))
        self.label_7.setText(_translate("frmCreditCardsAdd", "Maximum balance"))
        self.txtMaximum.setText(_translate("frmCreditCardsAdd", "0"))
        self.label_4.setText(_translate("frmCreditCardsAdd", "Credit card number"))
        self.cmd.setText(_translate("frmCreditCardsAdd", "Save"))
from xulpymoney.ui.myqlineedit import myQLineEdit, myQLineEditValidatingCreditCard
import xulpymoney.images.xulpymoney_rc
