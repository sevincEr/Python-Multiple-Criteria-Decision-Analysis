# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MCDA_Project_1.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(932, 771)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("#tabWidget{\n"
"border-image: url(:/addBacground/icons/istockphoto-952039286-170667a.jpg);\n"
"}")
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_wayCalculate = QtWidgets.QWidget()
        self.tab_wayCalculate.setStyleSheet("#tab_wayCalculate{\n"
"    border-image: url(:/background image/istockphoto-952039286-170667a.jpg);\n"
"}")
        self.tab_wayCalculate.setObjectName("tab_wayCalculate")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_wayCalculate)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalFrame_selectFile = QtWidgets.QFrame(self.tab_wayCalculate)
        self.horizontalFrame_selectFile.setObjectName("horizontalFrame_selectFile")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame_selectFile)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_fileName = QtWidgets.QLabel(self.horizontalFrame_selectFile)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_fileName.setFont(font)
        self.label_fileName.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_fileName.setObjectName("label_fileName")
        self.horizontalLayout.addWidget(self.label_fileName)
        self.label_selectedFileName = QtWidgets.QLabel(self.horizontalFrame_selectFile)
        self.label_selectedFileName.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 0, 127);\n"
"font: 25 9pt \"Microsoft JhengHei Light\";\n"
"font: 87 8pt \"Arial Black\";\n"
"border-radius:5px")
        self.label_selectedFileName.setAlignment(QtCore.Qt.AlignCenter)
        self.label_selectedFileName.setObjectName("label_selectedFileName")
        self.horizontalLayout.addWidget(self.label_selectedFileName)
        self.btn_fileway = QtWidgets.QPushButton(self.horizontalFrame_selectFile)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_fileway.setFont(font)
        self.btn_fileway.setStyleSheet("background-image: url(:/background image/istockphoto-952039286-170667a.jpg);\n"
"\n"
"color: rgb(255, 255, 255);")
        self.btn_fileway.setObjectName("btn_fileway")
        self.horizontalLayout.addWidget(self.btn_fileway)
        self.horizontalLayout.setStretch(0, 15)
        self.horizontalLayout.setStretch(1, 60)
        self.horizontalLayout.setStretch(2, 20)
        self.gridLayout_3.addWidget(self.horizontalFrame_selectFile, 0, 0, 1, 1)
        self.horizontalFrame_wayProcess = QtWidgets.QFrame(self.tab_wayCalculate)
        self.horizontalFrame_wayProcess.setObjectName("horizontalFrame_wayProcess")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalFrame_wayProcess)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalFrame_selectWay = QtWidgets.QFrame(self.horizontalFrame_wayProcess)
        self.horizontalFrame_selectWay.setObjectName("horizontalFrame_selectWay")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalFrame_selectWay)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_selectWay = QtWidgets.QLabel(self.horizontalFrame_selectWay)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_selectWay.setFont(font)
        self.label_selectWay.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_selectWay.setObjectName("label_selectWay")
        self.horizontalLayout_2.addWidget(self.label_selectWay)
        self.cBox_yontem = QtWidgets.QComboBox(self.horizontalFrame_selectWay)
        self.cBox_yontem.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cBox_yontem.setFont(font)
        self.cBox_yontem.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px")
        self.cBox_yontem.setObjectName("cBox_yontem")
        self.cBox_yontem.addItem("")
        self.cBox_yontem.addItem("")
        self.cBox_yontem.addItem("")
        self.horizontalLayout_2.addWidget(self.cBox_yontem)
        self.horizontalLayout_2.setStretch(0, 20)
        self.horizontalLayout_2.setStretch(1, 80)
        self.horizontalLayout_3.addWidget(self.horizontalFrame_selectWay)
        self.horizontalLayout_3.setStretch(0, 70)
        self.gridLayout_3.addWidget(self.horizontalFrame_wayProcess, 1, 0, 1, 1)
        self.gridFrame_showsCharts = QtWidgets.QFrame(self.tab_wayCalculate)
        self.gridFrame_showsCharts.setObjectName("gridFrame_showsCharts")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame_showsCharts)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalFrame_rButton_forCharts = QtWidgets.QFrame(self.gridFrame_showsCharts)
        self.horizontalFrame_rButton_forCharts.setObjectName("horizontalFrame_rButton_forCharts")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalFrame_rButton_forCharts)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout.addWidget(self.horizontalFrame_rButton_forCharts, 2, 1, 1, 1)
        self.tableWidget_xlsTable = QtWidgets.QTableWidget(self.gridFrame_showsCharts)
        self.tableWidget_xlsTable.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius : 10px")
        self.tableWidget_xlsTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_xlsTable.setObjectName("tableWidget_xlsTable")
        self.tableWidget_xlsTable.setColumnCount(0)
        self.tableWidget_xlsTable.setRowCount(0)
        self.tableWidget_xlsTable.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_xlsTable.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget_xlsTable.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_xlsTable.verticalHeader().setDefaultSectionSize(100)
        self.tableWidget_xlsTable.verticalHeader().setMinimumSectionSize(60)
        self.gridLayout.addWidget(self.tableWidget_xlsTable, 1, 0, 1, 1)
        self.tableWidget_results = QtWidgets.QTableWidget(self.gridFrame_showsCharts)
        self.tableWidget_results.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius : 10px")
        self.tableWidget_results.setObjectName("tableWidget_results")
        self.tableWidget_results.setColumnCount(0)
        self.tableWidget_results.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_results, 1, 1, 1, 1)
        self.horizontalLayout_weightCalculate = QtWidgets.QHBoxLayout()
        self.horizontalLayout_weightCalculate.setObjectName("horizontalLayout_weightCalculate")
        self.cBox_isThereWeight = QtWidgets.QCheckBox(self.gridFrame_showsCharts)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cBox_isThereWeight.setFont(font)
        self.cBox_isThereWeight.setStyleSheet("color: rgb(255, 255, 38);")
        self.cBox_isThereWeight.setObjectName("cBox_isThereWeight")
        self.horizontalLayout_weightCalculate.addWidget(self.cBox_isThereWeight)
        self.btn_weightCalculete = QtWidgets.QPushButton(self.gridFrame_showsCharts)
        self.btn_weightCalculete.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_weightCalculete.setFont(font)
        self.btn_weightCalculete.setMouseTracking(False)
        self.btn_weightCalculete.setStyleSheet("background-image: url(:/background image/istockphoto-952039286-170667a.jpg);\n"
"color: rgb(255, 255, 51);\n"
"")
        self.btn_weightCalculete.setObjectName("btn_weightCalculete")
        self.horizontalLayout_weightCalculate.addWidget(self.btn_weightCalculete)
        self.horizontalLayout_weightCalculate.setStretch(0, 40)
        self.horizontalLayout_weightCalculate.setStretch(1, 60)
        self.gridLayout.addLayout(self.horizontalLayout_weightCalculate, 2, 0, 1, 1)
        self.btn_hesapla = QtWidgets.QPushButton(self.gridFrame_showsCharts)
        self.btn_hesapla.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btn_hesapla.setFont(font)
        self.btn_hesapla.setStyleSheet("background-image: url(:/background image/istockphoto-952039286-170667a.jpg);\n"
"color: rgb(255, 255, 255);")
        self.btn_hesapla.setObjectName("btn_hesapla")
        self.gridLayout.addWidget(self.btn_hesapla, 3, 0, 1, 1)
        self.btn_writeResults = QtWidgets.QPushButton(self.gridFrame_showsCharts)
        self.btn_writeResults.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_writeResults.setFont(font)
        self.btn_writeResults.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-image: url(:/background image/istockphoto-952039286-170667a.jpg);")
        self.btn_writeResults.setObjectName("btn_writeResults")
        self.gridLayout.addWidget(self.btn_writeResults, 3, 1, 1, 1)
        self.gridLayout_3.addWidget(self.gridFrame_showsCharts, 2, 0, 1, 1)
        self.verticalFrame_writeResults = QtWidgets.QFrame(self.tab_wayCalculate)
        self.verticalFrame_writeResults.setObjectName("verticalFrame_writeResults")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame_writeResults)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalFrame_rButtonSelectWriteWay = QtWidgets.QFrame(self.verticalFrame_writeResults)
        self.horizontalFrame_rButtonSelectWriteWay.setEnabled(False)
        self.horizontalFrame_rButtonSelectWriteWay.setObjectName("horizontalFrame_rButtonSelectWriteWay")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalFrame_rButtonSelectWriteWay)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout.addWidget(self.horizontalFrame_rButtonSelectWriteWay)
        self.gridLayout_3.addWidget(self.verticalFrame_writeResults, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab_wayCalculate, "")
        self.tab_weightCalculate = QtWidgets.QWidget()
        self.tab_weightCalculate.setEnabled(False)
        self.tab_weightCalculate.setStyleSheet("#tab_weightCalculate{\n"
"    border-image: url(:/background image/istockphoto-952039286-170667a.jpg);\n"
"}")
        self.tab_weightCalculate.setObjectName("tab_weightCalculate")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_weightCalculate)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_4.addItem(spacerItem1, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 2, 0, 1, 1)
        self.tableWidget_weights = QtWidgets.QTableWidget(self.tab_weightCalculate)
        self.tableWidget_weights.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.tableWidget_weights.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableWidget_weights.setAlternatingRowColors(True)
        self.tableWidget_weights.setObjectName("tableWidget_weights")
        self.tableWidget_weights.setColumnCount(0)
        self.tableWidget_weights.setRowCount(0)
        self.gridLayout_4.addWidget(self.tableWidget_weights, 2, 1, 1, 1)
        self.tableWidget_resultWeight = QtWidgets.QTableWidget(self.tab_weightCalculate)
        self.tableWidget_resultWeight.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.tableWidget_resultWeight.setColumnCount(2)
        self.tableWidget_resultWeight.setObjectName("tableWidget_resultWeight")
        self.tableWidget_resultWeight.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_resultWeight.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_resultWeight.setHorizontalHeaderItem(1, item)
        self.tableWidget_resultWeight.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_resultWeight.verticalHeader().setCascadingSectionResizes(True)
        self.gridLayout_4.addWidget(self.tableWidget_resultWeight, 2, 3, 1, 1)
        self.label_weightRank = QtWidgets.QLabel(self.tab_weightCalculate)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_weightRank.setFont(font)
        self.label_weightRank.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 5px")
        self.label_weightRank.setText("")
        self.label_weightRank.setObjectName("label_weightRank")
        self.gridLayout_4.addWidget(self.label_weightRank, 0, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_weightCalculate)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 5px\n"
"")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 1, 1, 1)
        self.btn_wCalculate = QtWidgets.QPushButton(self.tab_weightCalculate)
        self.btn_wCalculate.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_wCalculate.setFont(font)
        self.btn_wCalculate.setStyleSheet("background-image: url(:/background image/istockphoto-952039286-170667a.jpg);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btn_wCalculate.setObjectName("btn_wCalculate")
        self.gridLayout_4.addWidget(self.btn_wCalculate, 4, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 2, 4, 1, 1)
        self.btn_addWayCal = QtWidgets.QPushButton(self.tab_weightCalculate)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_addWayCal.setFont(font)
        self.btn_addWayCal.setStyleSheet("background-image: url(:/background image/istockphoto-952039286-170667a.jpg);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btn_addWayCal.setObjectName("btn_addWayCal")
        self.gridLayout_4.addWidget(self.btn_addWayCal, 4, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_4.addItem(spacerItem5, 5, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_4.addItem(spacerItem6, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_4)
        self.btn_saveWeights = QtWidgets.QPushButton(self.tab_weightCalculate)
        self.btn_saveWeights.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_saveWeights.setFont(font)
        self.btn_saveWeights.setStyleSheet("background-image: url(:/background image/istockphoto-952039286-170667a.jpg);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btn_saveWeights.setObjectName("btn_saveWeights")
        self.verticalLayout_3.addWidget(self.btn_saveWeights)
        self.tabWidget.addTab(self.tab_weightCalculate, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.btn_writeResults.clicked.connect(MainWindow.btn_save_results_clicked)
        self.btn_hesapla.clicked.connect(MainWindow.calculate)
        self.btn_fileway.clicked.connect(MainWindow.btn_fileway_clicked)
        self.btn_fileway.clicked.connect(self.tableWidget_xlsTable.resizeColumnsToContents)
        self.btn_fileway.clicked.connect(self.tableWidget_xlsTable.resizeRowsToContents)
        self.tableWidget_xlsTable.itemChanged['QTableWidgetItem*'].connect(self.tableWidget_xlsTable.update)
        self.btn_weightCalculete.clicked.connect(MainWindow.cellValue_WCalculate)
        self.cBox_isThereWeight.stateChanged['int'].connect(MainWindow.checked_CBox)
        self.tableWidget_weights.itemDoubleClicked['QTableWidgetItem*'].connect(MainWindow.cellValue)
        self.tableWidget_weights.itemChanged['QTableWidgetItem*'].connect(MainWindow.cellValue_change)
        self.tableWidget_weights.currentItemChanged['QTableWidgetItem*','QTableWidgetItem*'].connect(MainWindow.current_item)
        self.btn_wCalculate.clicked.connect(MainWindow.findWeight)
        self.btn_saveWeights.clicked.connect(MainWindow.btn_save_results_clicked)
        self.btn_addWayCal.clicked.connect(MainWindow.addRowInTable)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TOPSIS - ARAS - VIKOR  HESAPLAMASI"))
        self.label_fileName.setText(_translate("MainWindow", "Dosya Adı: "))
        self.label_selectedFileName.setText(_translate("MainWindow", "Sadece xls(excel) dosya tipi seçiniz..."))
        self.btn_fileway.setText(_translate("MainWindow", "DOSYA SEÇ"))
        self.label_selectWay.setText(_translate("MainWindow", "Yöntem Seç: "))
        self.cBox_yontem.setCurrentText(_translate("MainWindow", "TOPSIS"))
        self.cBox_yontem.setItemText(0, _translate("MainWindow", "TOPSIS"))
        self.cBox_yontem.setItemText(1, _translate("MainWindow", "ARAS"))
        self.cBox_yontem.setItemText(2, _translate("MainWindow", "VIKOR"))
        self.cBox_isThereWeight.setText(_translate("MainWindow", "Ağırlık Değeri Yok"))
        self.btn_weightCalculete.setText(_translate("MainWindow", "Ağırlık Hesapla"))
        self.btn_hesapla.setText(_translate("MainWindow", "HESAPLA"))
        self.btn_writeResults.setText(_translate("MainWindow", " Excele Sonuç Yazdır"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_wayCalculate), _translate("MainWindow", "ÇKKVT Hesaplaması"))
        item = self.tableWidget_resultWeight.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "KRİTERLER"))
        item = self.tableWidget_resultWeight.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "AĞIRLIKLAR"))
        self.label_2.setText(_translate("MainWindow", "TUTARLILIK ORANI DEĞERİ : "))
        self.btn_wCalculate.setText(_translate("MainWindow", "AĞIRLIK HESAPLA"))
        self.btn_addWayCal.setText(_translate("MainWindow", "Ağırlıkları Matrise Ekle"))
        self.btn_saveWeights.setText(_translate("MainWindow", "Ağırlıkları Excele Kaydet"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_weightCalculate), _translate("MainWindow", "Ağırlık Hesaplaması"))
import image_rc