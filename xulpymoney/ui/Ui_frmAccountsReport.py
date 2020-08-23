# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xulpymoney/ui/frmAccountsReport.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmAccountsReport(object):
    def setupUi(self, frmAccountsReport):
        frmAccountsReport.setObjectName("frmAccountsReport")
        frmAccountsReport.setWindowModality(QtCore.Qt.WindowModal)
        frmAccountsReport.resize(1061, 607)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xulpymoney/report2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmAccountsReport.setWindowIcon(icon)
        frmAccountsReport.setModal(True)
        self._2 = QtWidgets.QVBoxLayout(frmAccountsReport)
        self._2.setObjectName("_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblTitulo = QtWidgets.QLabel(frmAccountsReport)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setStyleSheet("color: rgb(0, 128, 0);")
        self.lblTitulo.setText("")
        self.lblTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitulo.setObjectName("lblTitulo")
        self.verticalLayout_2.addWidget(self.lblTitulo)
        self.tab = QtWidgets.QTabWidget(frmAccountsReport)
        self.tab.setObjectName("tab")
        self.tabMovimientos = QtWidgets.QWidget()
        self.tabMovimientos.setObjectName("tabMovimientos")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tabMovimientos)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.groupBox = QtWidgets.QGroupBox(self.tabMovimientos)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.cmbEB = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbEB.sizePolicy().hasHeightForWidth())
        self.cmbEB.setSizePolicy(sizePolicy)
        self.cmbEB.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.cmbEB.setObjectName("cmbEB")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cmbEB)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txtAccount = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtAccount.sizePolicy().hasHeightForWidth())
        self.txtAccount.setSizePolicy(sizePolicy)
        self.txtAccount.setMinimumSize(QtCore.QSize(300, 0))
        self.txtAccount.setObjectName("txtAccount")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtAccount)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.cmbCurrency = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbCurrency.sizePolicy().hasHeightForWidth())
        self.cmbCurrency.setSizePolicy(sizePolicy)
        self.cmbCurrency.setObjectName("cmbCurrency")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cmbCurrency)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txtNumero = myQLineEditValidatingAccount(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtNumero.sizePolicy().hasHeightForWidth())
        self.txtNumero.setSizePolicy(sizePolicy)
        self.txtNumero.setObjectName("txtNumero")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtNumero)
        self.chkActiva = QtWidgets.QCheckBox(self.groupBox)
        self.chkActiva.setObjectName("chkActiva")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.chkActiva)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.cmdDatos = QtWidgets.QPushButton(self.groupBox)
        self.cmdDatos.setObjectName("cmdDatos")
        self.horizontalLayout_12.addWidget(self.cmdDatos)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_4.addWidget(self.groupBox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tabMovimientos)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.wdgYM = wdgYearMonth(self.groupBox_2)
        self.wdgYM.setObjectName("wdgYM")
        self.horizontalLayout.addWidget(self.wdgYM)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.mqtwOperations = mqtwObjects(self.groupBox_2)
        self.mqtwOperations.setObjectName("mqtwOperations")
        self.verticalLayout_3.addWidget(self.mqtwOperations)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_6.addWidget(self.groupBox_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/xulpymoney/coins.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab.addTab(self.tabMovimientos, icon1, "")
        self.tabTarjetas = QtWidgets.QWidget()
        self.tabTarjetas.setObjectName("tabTarjetas")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tabTarjetas)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tabTarjetas)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.chkCreditCards = QtWidgets.QCheckBox(self.groupBox_3)
        self.chkCreditCards.setObjectName("chkCreditCards")
        self.verticalLayout_4.addWidget(self.chkCreditCards)
        self.mqtwCreditCards = mqtwObjects(self.groupBox_3)
        self.mqtwCreditCards.setObjectName("mqtwCreditCards")
        self.verticalLayout_4.addWidget(self.mqtwCreditCards)
        self.horizontalLayout_9.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.layDiferido = QtWidgets.QHBoxLayout()
        self.layDiferido.setObjectName("layDiferido")
        self.tabOpercreditcardsDiferidas = QtWidgets.QTabWidget(self.tabTarjetas)
        self.tabOpercreditcardsDiferidas.setEnabled(False)
        self.tabOpercreditcardsDiferidas.setObjectName("tabOpercreditcardsDiferidas")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.grpOperTarjetas = QtWidgets.QGroupBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grpOperTarjetas.sizePolicy().hasHeightForWidth())
        self.grpOperTarjetas.setSizePolicy(sizePolicy)
        self.grpOperTarjetas.setCheckable(False)
        self.grpOperTarjetas.setObjectName("grpOperTarjetas")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.grpOperTarjetas)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.mqtwCreditCardOperations = mqtwObjects(self.grpOperTarjetas)
        self.mqtwCreditCardOperations.setObjectName("mqtwCreditCardOperations")
        self.verticalLayout_7.addWidget(self.mqtwCreditCardOperations)
        self.horizontalLayout_6.addWidget(self.grpOperTarjetas)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem6)
        self.grpPago = QtWidgets.QGroupBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grpPago.sizePolicy().hasHeightForWidth())
        self.grpPago.setSizePolicy(sizePolicy)
        self.grpPago.setObjectName("grpPago")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.grpPago)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lblPago = QtWidgets.QLabel(self.grpPago)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblPago.sizePolicy().hasHeightForWidth())
        self.lblPago.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblPago.setFont(font)
        self.lblPago.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPago.setObjectName("lblPago")
        self.verticalLayout_8.addWidget(self.lblPago)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.wdgDtPago = wdgDatetime(self.grpPago)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wdgDtPago.sizePolicy().hasHeightForWidth())
        self.wdgDtPago.setSizePolicy(sizePolicy)
        self.wdgDtPago.setObjectName("wdgDtPago")
        self.horizontalLayout_10.addWidget(self.wdgDtPago)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.cmdPago = QtWidgets.QPushButton(self.grpPago)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmdPago.sizePolicy().hasHeightForWidth())
        self.cmdPago.setSizePolicy(sizePolicy)
        self.cmdPago.setObjectName("cmdPago")
        self.verticalLayout_8.addWidget(self.cmdPago)
        self.horizontalLayout_11.addLayout(self.verticalLayout_8)
        self.verticalLayout_10.addWidget(self.grpPago)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem7)
        self.horizontalLayout_6.addLayout(self.verticalLayout_10)
        self.tabOpercreditcardsDiferidas.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_13.addWidget(self.label_6)
        self.cmbFechasPago = QtWidgets.QComboBox(self.tab_3)
        self.cmbFechasPago.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.cmbFechasPago.setObjectName("cmbFechasPago")
        self.horizontalLayout_13.addWidget(self.cmbFechasPago)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem8)
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_13.addWidget(self.label_7)
        self.cmdDevolverPago = QtWidgets.QPushButton(self.tab_3)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/xulpmoney/tools-wizard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmdDevolverPago.setIcon(icon2)
        self.cmdDevolverPago.setObjectName("cmdDevolverPago")
        self.horizontalLayout_13.addWidget(self.cmdDevolverPago)
        self.verticalLayout_9.addLayout(self.horizontalLayout_13)
        self.mqtwCreditCardOperationsHistorical = mqtwObjects(self.tab_3)
        self.mqtwCreditCardOperationsHistorical.setObjectName("mqtwCreditCardOperationsHistorical")
        self.verticalLayout_9.addWidget(self.mqtwCreditCardOperationsHistorical)
        self.horizontalLayout_14.addLayout(self.verticalLayout_9)
        self.tabOpercreditcardsDiferidas.addTab(self.tab_3, "")
        self.layDiferido.addWidget(self.tabOpercreditcardsDiferidas)
        self.verticalLayout_5.addLayout(self.layDiferido)
        self.horizontalLayout_8.addLayout(self.verticalLayout_5)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/xulpymoney/visa2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab.addTab(self.tabTarjetas, icon3, "")
        self.verticalLayout_2.addWidget(self.tab)
        self._2.addLayout(self.verticalLayout_2)
        self.actionOperationAdd = QtWidgets.QAction(frmAccountsReport)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/xulpymoney/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOperationAdd.setIcon(icon4)
        self.actionOperationAdd.setObjectName("actionOperationAdd")
        self.actionOperationDelete = QtWidgets.QAction(frmAccountsReport)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/xulpymoney/list-remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOperationDelete.setIcon(icon5)
        self.actionOperationDelete.setObjectName("actionOperationDelete")
        self.actionCreditCardAdd = QtWidgets.QAction(frmAccountsReport)
        self.actionCreditCardAdd.setIcon(icon4)
        self.actionCreditCardAdd.setObjectName("actionCreditCardAdd")
        self.actionCreditCardDelete = QtWidgets.QAction(frmAccountsReport)
        self.actionCreditCardDelete.setIcon(icon5)
        self.actionCreditCardDelete.setObjectName("actionCreditCardDelete")
        self.actionCreditCardOperAdd = QtWidgets.QAction(frmAccountsReport)
        self.actionCreditCardOperAdd.setIcon(icon4)
        self.actionCreditCardOperAdd.setObjectName("actionCreditCardOperAdd")
        self.actionCreditCardOperDelete = QtWidgets.QAction(frmAccountsReport)
        self.actionCreditCardOperDelete.setIcon(icon5)
        self.actionCreditCardOperDelete.setObjectName("actionCreditCardOperDelete")
        self.actionCreditCardEdit = QtWidgets.QAction(frmAccountsReport)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/xulpymoney/editar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCreditCardEdit.setIcon(icon6)
        self.actionCreditCardEdit.setObjectName("actionCreditCardEdit")
        self.actionCreditCardActivate = QtWidgets.QAction(frmAccountsReport)
        self.actionCreditCardActivate.setCheckable(True)
        self.actionCreditCardActivate.setObjectName("actionCreditCardActivate")
        self.actionOperationEdit = QtWidgets.QAction(frmAccountsReport)
        self.actionOperationEdit.setIcon(icon6)
        self.actionOperationEdit.setObjectName("actionOperationEdit")
        self.actionCreditCardOperEdit = QtWidgets.QAction(frmAccountsReport)
        self.actionCreditCardOperEdit.setIcon(icon6)
        self.actionCreditCardOperEdit.setObjectName("actionCreditCardOperEdit")
        self.actionTransferDelete = QtWidgets.QAction(frmAccountsReport)
        self.actionTransferDelete.setIcon(icon5)
        self.actionTransferDelete.setObjectName("actionTransferDelete")
        self.actionInvestmentOperationEdit = QtWidgets.QAction(frmAccountsReport)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/xulpymoney/document-edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInvestmentOperationEdit.setIcon(icon7)
        self.actionInvestmentOperationEdit.setObjectName("actionInvestmentOperationEdit")
        self.actionInvestmentOperationDelete = QtWidgets.QAction(frmAccountsReport)
        self.actionInvestmentOperationDelete.setIcon(icon5)
        self.actionInvestmentOperationDelete.setObjectName("actionInvestmentOperationDelete")
        self.actionCreditCardOperRefund = QtWidgets.QAction(frmAccountsReport)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/xulpymoney/Money.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCreditCardOperRefund.setIcon(icon8)
        self.actionCreditCardOperRefund.setObjectName("actionCreditCardOperRefund")
        self.actionConceptReport = QtWidgets.QAction(frmAccountsReport)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/xulpymoney/hucha.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConceptReport.setIcon(icon9)
        self.actionConceptReport.setObjectName("actionConceptReport")

        self.retranslateUi(frmAccountsReport)
        self.tab.setCurrentIndex(1)
        self.tabOpercreditcardsDiferidas.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmAccountsReport)

    def retranslateUi(self, frmAccountsReport):
        _translate = QtCore.QCoreApplication.translate
        frmAccountsReport.setWindowTitle(_translate("frmAccountsReport", "Account report"))
        self.groupBox.setTitle(_translate("frmAccountsReport", "Account data"))
        self.label.setText(_translate("frmAccountsReport", "Select the bank it belongs to"))
        self.label_2.setText(_translate("frmAccountsReport", "Account name"))
        self.label_8.setText(_translate("frmAccountsReport", "Account currency"))
        self.label_3.setText(_translate("frmAccountsReport", "Account number"))
        self.chkActiva.setText(_translate("frmAccountsReport", "Is active?"))
        self.cmdDatos.setText(_translate("frmAccountsReport", "Update"))
        self.groupBox_2.setTitle(_translate("frmAccountsReport", "Account movements"))
        self.tab.setTabText(self.tab.indexOf(self.tabMovimientos), _translate("frmAccountsReport", "Account"))
        self.groupBox_3.setTitle(_translate("frmAccountsReport", "Credit card list"))
        self.chkCreditCards.setText(_translate("frmAccountsReport", "Show inactive credit cards"))
        self.grpOperTarjetas.setTitle(_translate("frmAccountsReport", "Selected Credit Card delayed operations"))
        self.grpPago.setTitle(_translate("frmAccountsReport", "Selected operations delayed payment"))
        self.lblPago.setText(_translate("frmAccountsReport", "XXXX €"))
        self.cmdPago.setText(_translate("frmAccountsReport", "Pay"))
        self.tabOpercreditcardsDiferidas.setTabText(self.tabOpercreditcardsDiferidas.indexOf(self.tab_2), _translate("frmAccountsReport", "Selected Credit Card delayed operations"))
        self.label_6.setText(_translate("frmAccountsReport", "Select a payment"))
        self.label_7.setText(_translate("frmAccountsReport", "Pay back"))
        self.cmdDevolverPago.setText(_translate("frmAccountsReport", "Pay back"))
        self.tabOpercreditcardsDiferidas.setTabText(self.tabOpercreditcardsDiferidas.indexOf(self.tab_3), _translate("frmAccountsReport", "Deferred payments for the selected card report"))
        self.tab.setTabText(self.tab.indexOf(self.tabTarjetas), _translate("frmAccountsReport", "Associated credit cards"))
        self.actionOperationAdd.setText(_translate("frmAccountsReport", "New operation"))
        self.actionOperationAdd.setToolTip(_translate("frmAccountsReport", "New operation"))
        self.actionOperationDelete.setText(_translate("frmAccountsReport", "Delete operation"))
        self.actionOperationDelete.setToolTip(_translate("frmAccountsReport", "Delete operation"))
        self.actionCreditCardAdd.setText(_translate("frmAccountsReport", "New credit card"))
        self.actionCreditCardDelete.setText(_translate("frmAccountsReport", "Delete credit card"))
        self.actionCreditCardDelete.setToolTip(_translate("frmAccountsReport", "Delete credit card"))
        self.actionCreditCardOperAdd.setText(_translate("frmAccountsReport", "New credit card operation"))
        self.actionCreditCardOperAdd.setToolTip(_translate("frmAccountsReport", "New credit card operation"))
        self.actionCreditCardOperDelete.setText(_translate("frmAccountsReport", "Delete credit card operation"))
        self.actionCreditCardOperDelete.setToolTip(_translate("frmAccountsReport", "Delete credit card operation"))
        self.actionCreditCardEdit.setText(_translate("frmAccountsReport", "Update credit card"))
        self.actionCreditCardEdit.setToolTip(_translate("frmAccountsReport", "Update credit card"))
        self.actionCreditCardActivate.setText(_translate("frmAccountsReport", "Is active?"))
        self.actionOperationEdit.setText(_translate("frmAccountsReport", "Update operation"))
        self.actionOperationEdit.setToolTip(_translate("frmAccountsReport", "Update operation"))
        self.actionCreditCardOperEdit.setText(_translate("frmAccountsReport", "Update credit card operation"))
        self.actionCreditCardOperEdit.setToolTip(_translate("frmAccountsReport", "Update credit card operation"))
        self.actionTransferDelete.setText(_translate("frmAccountsReport", "Delete transfer"))
        self.actionTransferDelete.setToolTip(_translate("frmAccountsReport", "Delete transfer"))
        self.actionInvestmentOperationEdit.setText(_translate("frmAccountsReport", "Edit associated investment operation"))
        self.actionInvestmentOperationEdit.setToolTip(_translate("frmAccountsReport", "Edit associated investment operation"))
        self.actionInvestmentOperationDelete.setText(_translate("frmAccountsReport", "Delete associated investment operation"))
        self.actionInvestmentOperationDelete.setToolTip(_translate("frmAccountsReport", "Delete associated investment operation"))
        self.actionCreditCardOperRefund.setText(_translate("frmAccountsReport", "Credit card operation refund"))
        self.actionCreditCardOperRefund.setToolTip(_translate("frmAccountsReport", "Credit card operation refund"))
        self.actionConceptReport.setText(_translate("frmAccountsReport", "Show concept historical report"))
        self.actionConceptReport.setToolTip(_translate("frmAccountsReport", "Show concept historical report"))
from xulpymoney.ui.myqlineedit import myQLineEditValidatingAccount
from xulpymoney.ui.myqtablewidget import mqtwObjects
from xulpymoney.ui.wdgDatetime import wdgDatetime
from xulpymoney.ui.wdgYearMonth import wdgYearMonth
import xulpymoney.images.xulpymoney_rc
