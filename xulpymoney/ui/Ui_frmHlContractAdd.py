# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xulpymoney/ui/frmHlContractAdd.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmHlContractAdd(object):
    def setupUi(self, frmHlContractAdd):
        frmHlContractAdd.setObjectName("frmHlContractAdd")
        frmHlContractAdd.setWindowModality(QtCore.Qt.WindowModal)
        frmHlContractAdd.resize(450, 290)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xulpymoney/dividends.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmHlContractAdd.setWindowIcon(icon)
        frmHlContractAdd.setModal(True)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(frmHlContractAdd)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblTitulo = QtWidgets.QLabel(frmHlContractAdd)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setStyleSheet("color: rgb(0, 128, 0);")
        self.lblTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitulo.setObjectName("lblTitulo")
        self.verticalLayout.addWidget(self.lblTitulo)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.wdgDT = wdgDatetime(frmHlContractAdd)
        self.wdgDT.setObjectName("wdgDT")
        self.horizontalLayout.addWidget(self.wdgDT)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(frmHlContractAdd)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txtGuarantee = myQLineEdit(frmHlContractAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtGuarantee.sizePolicy().hasHeightForWidth())
        self.txtGuarantee.setSizePolicy(sizePolicy)
        self.txtGuarantee.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtGuarantee.setObjectName("txtGuarantee")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtGuarantee)
        self.lblLiquido_7 = QtWidgets.QLabel(frmHlContractAdd)
        self.lblLiquido_7.setObjectName("lblLiquido_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblLiquido_7)
        self.txtAdjustment = myQLineEdit(frmHlContractAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtAdjustment.sizePolicy().hasHeightForWidth())
        self.txtAdjustment.setSizePolicy(sizePolicy)
        self.txtAdjustment.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtAdjustment.setObjectName("txtAdjustment")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtAdjustment)
        self.lblGross = QtWidgets.QLabel(frmHlContractAdd)
        self.lblGross.setObjectName("lblGross")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblGross)
        self.txtInterest = myQLineEdit(frmHlContractAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtInterest.sizePolicy().hasHeightForWidth())
        self.txtInterest.setSizePolicy(sizePolicy)
        self.txtInterest.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtInterest.setObjectName("txtInterest")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtInterest)
        self.lblLiquido = QtWidgets.QLabel(frmHlContractAdd)
        self.lblLiquido.setObjectName("lblLiquido")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblLiquido)
        self.txtCommission = myQLineEdit(frmHlContractAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtCommission.sizePolicy().hasHeightForWidth())
        self.txtCommission.setSizePolicy(sizePolicy)
        self.txtCommission.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtCommission.setObjectName("txtCommission")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtCommission)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.cmd = QtWidgets.QPushButton(frmHlContractAdd)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/xulpymoney/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmd.setIcon(icon1)
        self.cmd.setObjectName("cmd")
        self.horizontalLayout_2.addWidget(self.cmd)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(frmHlContractAdd)
        QtCore.QMetaObject.connectSlotsByName(frmHlContractAdd)
        frmHlContractAdd.setTabOrder(self.txtInterest, self.txtCommission)
        frmHlContractAdd.setTabOrder(self.txtCommission, self.cmd)

    def retranslateUi(self, frmHlContractAdd):
        _translate = QtCore.QCoreApplication.translate
        frmHlContractAdd.setWindowTitle(_translate("frmHlContractAdd", "Daily high-low investment contract"))
        self.lblTitulo.setText(_translate("frmHlContractAdd", "Daily high-low investment contract"))
        self.label.setText(_translate("frmHlContractAdd", "Guarantee amount"))
        self.txtGuarantee.setText(_translate("frmHlContractAdd", "0"))
        self.lblLiquido_7.setText(_translate("frmHlContractAdd", "Adjustment amount"))
        self.txtAdjustment.setText(_translate("frmHlContractAdd", "0"))
        self.lblGross.setText(_translate("frmHlContractAdd", "Interest amount"))
        self.txtInterest.setText(_translate("frmHlContractAdd", "0"))
        self.lblLiquido.setText(_translate("frmHlContractAdd", "Commission amount"))
        self.txtCommission.setText(_translate("frmHlContractAdd", "0"))

from xulpymoney.ui.myqlineedit import myQLineEdit
from xulpymoney.ui.wdgDatetime import wdgDatetime
import xulpymoney.images.xulpymoney_rc
