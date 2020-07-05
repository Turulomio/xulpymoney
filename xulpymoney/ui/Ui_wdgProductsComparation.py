# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xulpymoney/ui/wdgProductsComparation.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgProductsComparation(object):
    def setupUi(self, wdgProductsComparation):
        wdgProductsComparation.setObjectName("wdgProductsComparation")
        wdgProductsComparation.resize(1422, 520)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(wdgProductsComparation)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl = QtWidgets.QLabel(wdgProductsComparation)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl.setFont(font)
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setObjectName("lbl")
        self.verticalLayout_2.addWidget(self.lbl)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.selector1 = wdgProductSelector(wdgProductsComparation)
        self.selector1.setObjectName("selector1")
        self.verticalLayout_4.addWidget(self.selector1)
        self.selector2 = wdgProductSelector(wdgProductsComparation)
        self.selector2.setObjectName("selector2")
        self.verticalLayout_4.addWidget(self.selector2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.cmdSwap = QtWidgets.QToolButton(wdgProductsComparation)
        self.cmdSwap.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xulpymoney/swap.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmdSwap.setIcon(icon)
        self.cmdSwap.setObjectName("cmdSwap")
        self.horizontalLayout_4.addWidget(self.cmdSwap)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.line_3 = QtWidgets.QFrame(wdgProductsComparation)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_5.addWidget(self.line_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(wdgProductsComparation)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.cmbCompareTypes = QtWidgets.QComboBox(wdgProductsComparation)
        self.cmbCompareTypes.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.cmbCompareTypes.setObjectName("cmbCompareTypes")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/xulpymoney/eye_red.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmbCompareTypes.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/xulpymoney/eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmbCompareTypes.addItem(icon2, "")
        self.cmbCompareTypes.addItem(icon1, "")
        self.cmbCompareTypes.addItem(icon2, "")
        self.cmbCompareTypes.addItem(icon1, "")
        self.cmbCompareTypes.addItem(icon2, "")
        self.cmbCompareTypes.addItem(icon1, "")
        self.cmbCompareTypes.addItem(icon2, "")
        self.cmbCompareTypes.addItem(icon1, "")
        self.horizontalLayout_3.addWidget(self.cmbCompareTypes)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(wdgProductsComparation)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_5.addWidget(self.line)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(wdgProductsComparation)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.cmbDateSelector = QtWidgets.QComboBox(wdgProductsComparation)
        self.cmbDateSelector.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.cmbDateSelector.setObjectName("cmbDateSelector")
        self.cmbDateSelector.addItem("")
        self.cmbDateSelector.addItem("")
        self.cmbDateSelector.addItem("")
        self.cmbDateSelector.addItem("")
        self.cmbDateSelector.addItem("")
        self.cmbDateSelector.addItem("")
        self.cmbDateSelector.addItem("")
        self.horizontalLayout.addWidget(self.cmbDateSelector)
        self.deCompare = QtWidgets.QDateEdit(wdgProductsComparation)
        self.deCompare.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.deCompare.setCalendarPopup(True)
        self.deCompare.setObjectName("deCompare")
        self.horizontalLayout.addWidget(self.deCompare)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(wdgProductsComparation)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.cmbGroupBy = QtWidgets.QComboBox(wdgProductsComparation)
        self.cmbGroupBy.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.cmbGroupBy.setObjectName("cmbGroupBy")
        self.cmbGroupBy.addItem("")
        self.cmbGroupBy.addItem("")
        self.cmbGroupBy.addItem("")
        self.cmbGroupBy.addItem("")
        self.cmbGroupBy.addItem("")
        self.horizontalLayout_2.addWidget(self.cmbGroupBy)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.line_2 = QtWidgets.QFrame(wdgProductsComparation)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_5.addWidget(self.line_2)
        self.cmdReport = QtWidgets.QToolButton(wdgProductsComparation)
        self.cmdReport.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/xulpymoney/history2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmdReport.setIcon(icon3)
        self.cmdReport.setObjectName("cmdReport")
        self.horizontalLayout_5.addWidget(self.cmdReport)
        self.line_4 = QtWidgets.QFrame(wdgProductsComparation)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_5.addWidget(self.line_4)
        self.cmdComparationData = QtWidgets.QToolButton(wdgProductsComparation)
        self.cmdComparationData.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/xulpymoney/database.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmdComparationData.setIcon(icon4)
        self.cmdComparationData.setObjectName("cmdComparationData")
        self.horizontalLayout_5.addWidget(self.cmdComparationData)
        self.cmdComparation = QtWidgets.QPushButton(wdgProductsComparation)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/xulpymoney/compare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmdComparation.setIcon(icon5)
        self.cmdComparation.setObjectName("cmdComparation")
        self.horizontalLayout_5.addWidget(self.cmdComparation)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.viewScatter = VCScatter(wdgProductsComparation)
        self.viewScatter.setObjectName("viewScatter")
        self.verticalLayout_2.addWidget(self.viewScatter)
        self.viewCompare = VCTemporalSeries(wdgProductsComparation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewCompare.sizePolicy().hasHeightForWidth())
        self.viewCompare.setSizePolicy(sizePolicy)
        self.viewCompare.setObjectName("viewCompare")
        self.verticalLayout_2.addWidget(self.viewCompare)
        self.viewTwoAxis = VCTemporalSeriesWithTwoYAxis(wdgProductsComparation)
        self.viewTwoAxis.setObjectName("viewTwoAxis")
        self.verticalLayout_2.addWidget(self.viewTwoAxis)
        self.lblCorrelation = QtWidgets.QLabel(wdgProductsComparation)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblCorrelation.setFont(font)
        self.lblCorrelation.setText("")
        self.lblCorrelation.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCorrelation.setObjectName("lblCorrelation")
        self.verticalLayout_2.addWidget(self.lblCorrelation)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)

        self.retranslateUi(wdgProductsComparation)
        self.cmbCompareTypes.setCurrentIndex(0)
        self.cmbDateSelector.setCurrentIndex(-1)
        self.cmbGroupBy.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(wdgProductsComparation)

    def retranslateUi(self, wdgProductsComparation):
        _translate = QtCore.QCoreApplication.translate
        wdgProductsComparation.setWindowTitle(_translate("wdgProductsComparation", "Form"))
        self.lbl.setText(_translate("wdgProductsComparation", "Products comparation"))
        self.label_2.setText(_translate("wdgProductsComparation", "Select a method to compare"))
        self.cmbCompareTypes.setItemText(0, _translate("wdgProductsComparation", "Not changed data"))
        self.cmbCompareTypes.setItemText(1, _translate("wdgProductsComparation", "Scattering product prices"))
        self.cmbCompareTypes.setItemText(2, _translate("wdgProductsComparation", "Scattering product daily gains percentage"))
        self.cmbCompareTypes.setItemText(3, _translate("wdgProductsComparation", "Controling percentage evolution"))
        self.cmbCompareTypes.setItemText(4, _translate("wdgProductsComparation", "Controlling percentage evolution. Leveraged reduced"))
        self.cmbCompareTypes.setItemText(5, _translate("wdgProductsComparation", "Controling inverse percentage evolution"))
        self.cmbCompareTypes.setItemText(6, _translate("wdgProductsComparation", "Controling inverse percentage evolultion. Leveraged reduced"))
        self.cmbCompareTypes.setItemText(7, _translate("wdgProductsComparation", "Spread of prices joining first value with multiplier"))
        self.cmbCompareTypes.setItemText(8, _translate("wdgProductsComparation", "Price Ratio"))
        self.label_7.setText(_translate("wdgProductsComparation", "Use data from"))
        self.cmbDateSelector.setItemText(0, _translate("wdgProductsComparation", "Last 7 days"))
        self.cmbDateSelector.setItemText(1, _translate("wdgProductsComparation", "Last 30 days"))
        self.cmbDateSelector.setItemText(2, _translate("wdgProductsComparation", "last 90 days"))
        self.cmbDateSelector.setItemText(3, _translate("wdgProductsComparation", "Last 365 days"))
        self.cmbDateSelector.setItemText(4, _translate("wdgProductsComparation", "Last 3 years"))
        self.cmbDateSelector.setItemText(5, _translate("wdgProductsComparation", "Last 10 years"))
        self.cmbDateSelector.setItemText(6, _translate("wdgProductsComparation", "All data"))
        self.deCompare.setDisplayFormat(_translate("wdgProductsComparation", "yyyy-MM-dd"))
        self.label_8.setText(_translate("wdgProductsComparation", "Group data by"))
        self.cmbGroupBy.setItemText(0, _translate("wdgProductsComparation", "Last 7 days"))
        self.cmbGroupBy.setItemText(1, _translate("wdgProductsComparation", "Last 30 days"))
        self.cmbGroupBy.setItemText(2, _translate("wdgProductsComparation", "last 90 days"))
        self.cmbGroupBy.setItemText(3, _translate("wdgProductsComparation", "Last 365 days"))
        self.cmbGroupBy.setItemText(4, _translate("wdgProductsComparation", "Last 3 years"))
        self.cmdReport.setToolTip(_translate("wdgProductsComparation", "Generate report"))
        self.cmdComparationData.setToolTip(_translate("wdgProductsComparation", "Shows comparation data"))
        self.cmdComparation.setText(_translate("wdgProductsComparation", "Compare"))
from xulpymoney.ui.myqcharts import VCScatter, VCTemporalSeries, VCTemporalSeriesWithTwoYAxis
from xulpymoney.ui.wdgProductSelector import wdgProductSelector
import xulpymoney.images.xulpymoney_rc
