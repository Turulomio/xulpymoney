# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xulpymoney/ui/wdgProductHistoricalChart.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgProductHistoricalChart(object):
    def setupUi(self, wdgProductHistoricalChart):
        wdgProductHistoricalChart.setObjectName("wdgProductHistoricalChart")
        wdgProductHistoricalChart.resize(984, 607)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(wdgProductHistoricalChart)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(wdgProductHistoricalChart)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.cmbChartType = QtWidgets.QComboBox(wdgProductHistoricalChart)
        self.cmbChartType.setObjectName("cmbChartType")
        self.cmbChartType.addItem("")
        self.cmbChartType.addItem("")
        self.horizontalLayout_2.addWidget(self.cmbChartType)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.line_3 = QtWidgets.QFrame(wdgProductHistoricalChart)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(wdgProductHistoricalChart)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.cmbOHCLDuration = QtWidgets.QComboBox(wdgProductHistoricalChart)
        self.cmbOHCLDuration.setObjectName("cmbOHCLDuration")
        self.horizontalLayout_4.addWidget(self.cmbOHCLDuration)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(wdgProductHistoricalChart)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cmdFromLeftMax = QtWidgets.QToolButton(wdgProductHistoricalChart)
        self.cmdFromLeftMax.setObjectName("cmdFromLeftMax")
        self.horizontalLayout.addWidget(self.cmdFromLeftMax)
        self.cmdFromLeft = QtWidgets.QToolButton(wdgProductHistoricalChart)
        self.cmdFromLeft.setObjectName("cmdFromLeft")
        self.horizontalLayout.addWidget(self.cmdFromLeft)
        self.dtFrom = QtWidgets.QDateEdit(wdgProductHistoricalChart)
        self.dtFrom.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dtFrom.setCalendarPopup(True)
        self.dtFrom.setObjectName("dtFrom")
        self.horizontalLayout.addWidget(self.dtFrom)
        self.cmdFromRight = QtWidgets.QToolButton(wdgProductHistoricalChart)
        self.cmdFromRight.setObjectName("cmdFromRight")
        self.horizontalLayout.addWidget(self.cmdFromRight)
        self.cmdFromRightMax = QtWidgets.QToolButton(wdgProductHistoricalChart)
        self.cmdFromRightMax.setObjectName("cmdFromRightMax")
        self.horizontalLayout.addWidget(self.cmdFromRightMax)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.line_2 = QtWidgets.QFrame(wdgProductHistoricalChart)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lblGainsPercentage = QtWidgets.QLabel(wdgProductHistoricalChart)
        self.lblGainsPercentage.setObjectName("lblGainsPercentage")
        self.horizontalLayout_7.addWidget(self.lblGainsPercentage)
        self.spnGainsPercentage = QtWidgets.QDoubleSpinBox(wdgProductHistoricalChart)
        self.spnGainsPercentage.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnGainsPercentage.setMaximum(300.0)
        self.spnGainsPercentage.setSingleStep(0.5)
        self.spnGainsPercentage.setProperty("value", 10.0)
        self.spnGainsPercentage.setObjectName("spnGainsPercentage")
        self.horizontalLayout_7.addWidget(self.spnGainsPercentage)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.chkSMA10 = QtWidgets.QCheckBox(wdgProductHistoricalChart)
        self.chkSMA10.setChecked(True)
        self.chkSMA10.setObjectName("chkSMA10")
        self.horizontalLayout_3.addWidget(self.chkSMA10)
        self.chkSMA50 = QtWidgets.QCheckBox(wdgProductHistoricalChart)
        self.chkSMA50.setChecked(True)
        self.chkSMA50.setObjectName("chkSMA50")
        self.horizontalLayout_3.addWidget(self.chkSMA50)
        self.chkSMA200 = QtWidgets.QCheckBox(wdgProductHistoricalChart)
        self.chkSMA200.setChecked(True)
        self.chkSMA200.setObjectName("chkSMA200")
        self.horizontalLayout_3.addWidget(self.chkSMA200)
        self.chkMedian = QtWidgets.QCheckBox(wdgProductHistoricalChart)
        self.chkMedian.setObjectName("chkMedian")
        self.horizontalLayout_3.addWidget(self.chkMedian)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(wdgProductHistoricalChart)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.chkAdjustSplits = QtWidgets.QCheckBox(wdgProductHistoricalChart)
        self.chkAdjustSplits.setChecked(True)
        self.chkAdjustSplits.setObjectName("chkAdjustSplits")
        self.horizontalLayout_5.addWidget(self.chkAdjustSplits)
        self.chkAdjustDividends = QtWidgets.QCheckBox(wdgProductHistoricalChart)
        self.chkAdjustDividends.setObjectName("chkAdjustDividends")
        self.horizontalLayout_5.addWidget(self.chkAdjustDividends)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.wdgTS = VCTemporalSeries(wdgProductHistoricalChart)
        self.wdgTS.setObjectName("wdgTS")
        self.verticalLayout.addWidget(self.wdgTS)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.horizontalLayout_8.addLayout(self.verticalLayout_5)
        self.actionProductReport = QtWidgets.QAction(wdgProductHistoricalChart)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xulpymoney/books.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProductReport.setIcon(icon)
        self.actionProductReport.setObjectName("actionProductReport")
        self.actionSortTPCDiario = QtWidgets.QAction(wdgProductHistoricalChart)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/document-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSortTPCDiario.setIcon(icon1)
        self.actionSortTPCDiario.setObjectName("actionSortTPCDiario")
        self.actionSortTPCAnual = QtWidgets.QAction(wdgProductHistoricalChart)
        self.actionSortTPCAnual.setIcon(icon1)
        self.actionSortTPCAnual.setObjectName("actionSortTPCAnual")
        self.actionSortName = QtWidgets.QAction(wdgProductHistoricalChart)
        self.actionSortName.setIcon(icon1)
        self.actionSortName.setObjectName("actionSortName")
        self.actionSortDividend = QtWidgets.QAction(wdgProductHistoricalChart)
        self.actionSortDividend.setIcon(icon1)
        self.actionSortDividend.setObjectName("actionSortDividend")
        self.actionSortHour = QtWidgets.QAction(wdgProductHistoricalChart)
        self.actionSortHour.setIcon(icon1)
        self.actionSortHour.setObjectName("actionSortHour")
        self.actionIbex35 = QtWidgets.QAction(wdgProductHistoricalChart)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/countries/spain.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionIbex35.setIcon(icon2)
        self.actionIbex35.setObjectName("actionIbex35")
        self.actionProductNew = QtWidgets.QAction(wdgProductHistoricalChart)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/xulpymoney/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProductNew.setIcon(icon3)
        self.actionProductNew.setObjectName("actionProductNew")
        self.actionProductDelete = QtWidgets.QAction(wdgProductHistoricalChart)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/xulpymoney/list-remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProductDelete.setIcon(icon4)
        self.actionProductDelete.setObjectName("actionProductDelete")
        self.actionFavorites = QtWidgets.QAction(wdgProductHistoricalChart)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/xulpymoney/star.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFavorites.setIcon(icon5)
        self.actionFavorites.setObjectName("actionFavorites")
        self.actionMergeCodes = QtWidgets.QAction(wdgProductHistoricalChart)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/cakes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMergeCodes.setIcon(icon6)
        self.actionMergeCodes.setObjectName("actionMergeCodes")
        self.actionQuoteNew = QtWidgets.QAction(wdgProductHistoricalChart)
        self.actionQuoteNew.setIcon(icon3)
        self.actionQuoteNew.setObjectName("actionQuoteNew")
        self.actionEstimationDPSNew = QtWidgets.QAction(wdgProductHistoricalChart)
        self.actionEstimationDPSNew.setIcon(icon3)
        self.actionEstimationDPSNew.setObjectName("actionEstimationDPSNew")
        self.actionPurge = QtWidgets.QAction(wdgProductHistoricalChart)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/xulpymoney/tools-wizard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPurge.setIcon(icon7)
        self.actionPurge.setObjectName("actionPurge")
        self.actionPurchaseGraphic = QtWidgets.QAction(wdgProductHistoricalChart)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/xulpymoney/report.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPurchaseGraphic.setIcon(icon8)
        self.actionPurchaseGraphic.setObjectName("actionPurchaseGraphic")
        self.actionProductPriceLastRemove = QtWidgets.QAction(wdgProductHistoricalChart)
        self.actionProductPriceLastRemove.setIcon(icon4)
        self.actionProductPriceLastRemove.setObjectName("actionProductPriceLastRemove")

        self.retranslateUi(wdgProductHistoricalChart)
        self.cmbChartType.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(wdgProductHistoricalChart)

    def retranslateUi(self, wdgProductHistoricalChart):
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("wdgProductHistoricalChart", "Chart type"))
        self.cmbChartType.setItemText(0, _translate("wdgProductHistoricalChart", "Lines"))
        self.cmbChartType.setItemText(1, _translate("wdgProductHistoricalChart", "Candles"))
        self.label_3.setText(_translate("wdgProductHistoricalChart", "Select time range"))
        self.label.setText(_translate("wdgProductHistoricalChart", "Show from selected date"))
        self.cmdFromLeftMax.setText(_translate("wdgProductHistoricalChart", "<<"))
        self.cmdFromLeft.setText(_translate("wdgProductHistoricalChart", "<"))
        self.dtFrom.setDisplayFormat(_translate("wdgProductHistoricalChart", "yyyy-MM-dd"))
        self.cmdFromRight.setText(_translate("wdgProductHistoricalChart", ">"))
        self.cmdFromRightMax.setText(_translate("wdgProductHistoricalChart", ">>"))
        self.lblGainsPercentage.setText(_translate("wdgProductHistoricalChart", "Gains percentage"))
        self.spnGainsPercentage.setSuffix(_translate("wdgProductHistoricalChart", " %"))
        self.chkSMA10.setText(_translate("wdgProductHistoricalChart", "SMA10"))
        self.chkSMA50.setText(_translate("wdgProductHistoricalChart", "SMA50"))
        self.chkSMA200.setText(_translate("wdgProductHistoricalChart", "SMA200"))
        self.chkMedian.setText(_translate("wdgProductHistoricalChart", "Median"))
        self.chkAdjustSplits.setText(_translate("wdgProductHistoricalChart", "Adjust splits"))
        self.chkAdjustDividends.setText(_translate("wdgProductHistoricalChart", "Adjust splits and dividends"))
        self.actionProductReport.setText(_translate("wdgProductHistoricalChart", "Product report"))
        self.actionProductReport.setToolTip(_translate("wdgProductHistoricalChart", "Product report"))
        self.actionSortTPCDiario.setText(_translate("wdgProductHistoricalChart", "% Daily"))
        self.actionSortTPCDiario.setToolTip(_translate("wdgProductHistoricalChart", "% Daily"))
        self.actionSortTPCAnual.setText(_translate("wdgProductHistoricalChart", "% Annual"))
        self.actionSortTPCAnual.setToolTip(_translate("wdgProductHistoricalChart", "% Annual"))
        self.actionSortName.setText(_translate("wdgProductHistoricalChart", "Name"))
        self.actionSortName.setToolTip(_translate("wdgProductHistoricalChart", "Name"))
        self.actionSortDividend.setText(_translate("wdgProductHistoricalChart", "Dividend"))
        self.actionSortDividend.setToolTip(_translate("wdgProductHistoricalChart", "Dividend"))
        self.actionSortHour.setText(_translate("wdgProductHistoricalChart", "Hour"))
        self.actionSortHour.setToolTip(_translate("wdgProductHistoricalChart", "Hour"))
        self.actionIbex35.setText(_translate("wdgProductHistoricalChart", "Ibex 35"))
        self.actionProductNew.setText(_translate("wdgProductHistoricalChart", "New product"))
        self.actionProductNew.setToolTip(_translate("wdgProductHistoricalChart", "New user product"))
        self.actionProductDelete.setText(_translate("wdgProductHistoricalChart", "Delete product"))
        self.actionProductDelete.setToolTip(_translate("wdgProductHistoricalChart", "Delete user product"))
        self.actionFavorites.setText(_translate("wdgProductHistoricalChart", "Add to favorites"))
        self.actionFavorites.setToolTip(_translate("wdgProductHistoricalChart", "Add to favorites"))
        self.actionMergeCodes.setText(_translate("wdgProductHistoricalChart", "Merge selected codes"))
        self.actionMergeCodes.setToolTip(_translate("wdgProductHistoricalChart", "Merge selected codes"))
        self.actionQuoteNew.setText(_translate("wdgProductHistoricalChart", "New price"))
        self.actionQuoteNew.setToolTip(_translate("wdgProductHistoricalChart", "New price"))
        self.actionEstimationDPSNew.setText(_translate("wdgProductHistoricalChart", "New DPS estimation"))
        self.actionEstimationDPSNew.setToolTip(_translate("wdgProductHistoricalChart", "New Dividend per share estimation"))
        self.actionPurge.setText(_translate("wdgProductHistoricalChart", "Purge investment"))
        self.actionPurge.setToolTip(_translate("wdgProductHistoricalChart", "Deletes quotes innecesary. Leaves open, high, low and close quotes."))
        self.actionPurchaseGraphic.setText(_translate("wdgProductHistoricalChart", "Show purchase graphic"))
        self.actionPurchaseGraphic.setToolTip(_translate("wdgProductHistoricalChart", "Show purchase graphic"))
        self.actionProductPriceLastRemove.setText(_translate("wdgProductHistoricalChart", "Remove last product price"))
        self.actionProductPriceLastRemove.setToolTip(_translate("wdgProductHistoricalChart", "Remove last product price"))
from xulpymoney.ui.myqcharts import VCTemporalSeries
import xulpymoney.images.xulpymoney_rc
