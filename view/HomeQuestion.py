# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeQuestion.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1577, 827)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.tab = QtWidgets.QTabWidget(self.centralwidget)
        self.tab.setEnabled(True)
        self.tab.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab.setObjectName("tab")
        self.Add = QtWidgets.QWidget()
        self.Add.setObjectName("Add")
        self.label_5 = QtWidgets.QLabel(self.Add)
        self.label_5.setGeometry(QtCore.QRect(760, 100, 51, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.IDAddQuestion = QtWidgets.QLabel(self.Add)
        self.IDAddQuestion.setGeometry(QtCore.QRect(840, 100, 221, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.IDAddQuestion.setFont(font)
        self.IDAddQuestion.setObjectName("IDAddQuestion")
        self.QLineAQuestion = QtWidgets.QLineEdit(self.Add)
        self.QLineAQuestion.setGeometry(QtCore.QRect(840, 170, 501, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QLineAQuestion.setFont(font)
        self.QLineAQuestion.setText("")
        self.QLineAQuestion.setObjectName("QLineAQuestion")
        self.QLineAOPA = QtWidgets.QLineEdit(self.Add)
        self.QLineAOPA.setGeometry(QtCore.QRect(840, 220, 501, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QLineAOPA.setFont(font)
        self.QLineAOPA.setObjectName("QLineAOPA")
        self.QLineAOPB = QtWidgets.QLineEdit(self.Add)
        self.QLineAOPB.setGeometry(QtCore.QRect(840, 270, 501, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QLineAOPB.setFont(font)
        self.QLineAOPB.setObjectName("QLineAOPB")
        self.QLineAOPC = QtWidgets.QLineEdit(self.Add)
        self.QLineAOPC.setGeometry(QtCore.QRect(840, 320, 501, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QLineAOPC.setFont(font)
        self.QLineAOPC.setObjectName("QLineAOPC")
        self.QLineAOPD = QtWidgets.QLineEdit(self.Add)
        self.QLineAOPD.setGeometry(QtCore.QRect(840, 370, 501, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QLineAOPD.setFont(font)
        self.QLineAOPD.setObjectName("QLineAOPD")
        self.label_7 = QtWidgets.QLabel(self.Add)
        self.label_7.setGeometry(QtCore.QRect(700, 170, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.Add)
        self.label_8.setGeometry(QtCore.QRect(721, 220, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.Add)
        self.label_9.setGeometry(QtCore.QRect(721, 270, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.Add)
        self.label_10.setGeometry(QtCore.QRect(721, 370, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.Add)
        self.label_11.setGeometry(QtCore.QRect(700, 420, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.Add)
        self.label_12.setGeometry(QtCore.QRect(660, 470, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.Add)
        self.label_13.setGeometry(QtCore.QRect(721, 320, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.ClearQuestion = QtWidgets.QPushButton(self.Add)
        self.ClearQuestion.setGeometry(QtCore.QRect(990, 560, 75, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ClearQuestion.setFont(font)
        self.ClearQuestion.setObjectName("ClearQuestion")
        self.AddQuestion = QtWidgets.QPushButton(self.Add)
        self.AddQuestion.setGeometry(QtCore.QRect(840, 560, 75, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AddQuestion.setFont(font)
        self.AddQuestion.setObjectName("AddQuestion")
        self.QComboBoxAAnswer = QtWidgets.QComboBox(self.Add)
        self.QComboBoxAAnswer.setGeometry(QtCore.QRect(840, 420, 51, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.QComboBoxAAnswer.setFont(font)
        self.QComboBoxAAnswer.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.QComboBoxAAnswer.setAutoFillBackground(False)
        self.QComboBoxAAnswer.setObjectName("QComboBoxAAnswer")
        self.QComboBoxAAnswer.addItem("")
        self.QComboBoxAAnswer.addItem("")
        self.QComboBoxAAnswer.addItem("")
        self.QComboBoxAAnswer.addItem("")
        self.QComboxAMaMH = QtWidgets.QComboBox(self.Add)
        self.QComboxAMaMH.setGeometry(QtCore.QRect(840, 480, 501, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QComboxAMaMH.setFont(font)
        self.QComboxAMaMH.setObjectName("QComboxAMaMH")
        self.tab.addTab(self.Add, "")
        self.Update = QtWidgets.QWidget()
        self.Update.setObjectName("Update")
        self.UpdateQuestion = QtWidgets.QPushButton(self.Update)
        self.UpdateQuestion.setGeometry(QtCore.QRect(430, 590, 95, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.UpdateQuestion.setFont(font)
        self.UpdateQuestion.setObjectName("UpdateQuestion")
        self.ClearUpdate = QtWidgets.QPushButton(self.Update)
        self.ClearUpdate.setGeometry(QtCore.QRect(580, 590, 90, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ClearUpdate.setFont(font)
        self.ClearUpdate.setObjectName("ClearUpdate")
        self.QTableUpdate = QtWidgets.QTableWidget(self.Update)
        self.QTableUpdate.setGeometry(QtCore.QRect(785, 190, 731, 311))
        self.QTableUpdate.setMinimumSize(QtCore.QSize(10, 20))
        self.QTableUpdate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.QTableUpdate.setAutoScrollMargin(16)
        self.QTableUpdate.setObjectName("QTableUpdate")
        self.QTableUpdate.setColumnCount(8)
        self.QTableUpdate.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableUpdate.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableUpdate.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableUpdate.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableUpdate.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableUpdate.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableUpdate.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableUpdate.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableUpdate.setHorizontalHeaderItem(7, item)
        self.QTableUpdate.horizontalHeader().setDefaultSectionSize(85)
        self.QTableUpdate.horizontalHeader().setMinimumSectionSize(24)
        self.QTableUpdate.verticalHeader().setDefaultSectionSize(1)
        self.QLineUIDCauHoi = QtWidgets.QLineEdit(self.Update)
        self.QLineUIDCauHoi.setGeometry(QtCore.QRect(400, 160, 361, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QLineUIDCauHoi.setFont(font)
        self.QLineUIDCauHoi.setInputMask("")
        self.QLineUIDCauHoi.setText("")
        self.QLineUIDCauHoi.setObjectName("QLineUIDCauHoi")
        self.label = QtWidgets.QLabel(self.Update)
        self.label.setGeometry(QtCore.QRect(940, 130, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Update)
        self.label_2.setGeometry(QtCore.QRect(350, 100, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_25 = QtWidgets.QLabel(self.Update)
        self.label_25.setGeometry(QtCore.QRect(280, 210, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.Update)
        self.label_26.setGeometry(QtCore.QRect(290, 310, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.Update)
        self.label_27.setGeometry(QtCore.QRect(290, 410, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.Update)
        self.label_28.setGeometry(QtCore.QRect(290, 260, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.Update)
        self.label_29.setGeometry(QtCore.QRect(280, 460, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.Update)
        self.label_30.setGeometry(QtCore.QRect(230, 510, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setWordWrap(True)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.Update)
        self.label_31.setGeometry(QtCore.QRect(290, 360, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.Update)
        self.label_32.setGeometry(QtCore.QRect(340, 160, 51, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.QLineUQuestion = QtWidgets.QLineEdit(self.Update)
        self.QLineUQuestion.setGeometry(QtCore.QRect(400, 210, 361, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QLineUQuestion.setFont(font)
        self.QLineUQuestion.setObjectName("QLineUQuestion")
        self.QLineUOPA = QtWidgets.QLineEdit(self.Update)
        self.QLineUOPA.setGeometry(QtCore.QRect(400, 260, 361, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QLineUOPA.setFont(font)
        self.QLineUOPA.setObjectName("QLineUOPA")
        self.QLineUOPB = QtWidgets.QLineEdit(self.Update)
        self.QLineUOPB.setGeometry(QtCore.QRect(400, 310, 361, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QLineUOPB.setFont(font)
        self.QLineUOPB.setObjectName("QLineUOPB")
        self.QLineUOPC = QtWidgets.QLineEdit(self.Update)
        self.QLineUOPC.setGeometry(QtCore.QRect(400, 360, 361, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QLineUOPC.setFont(font)
        self.QLineUOPC.setObjectName("QLineUOPC")
        self.QLineUOPD = QtWidgets.QLineEdit(self.Update)
        self.QLineUOPD.setGeometry(QtCore.QRect(400, 410, 361, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QLineUOPD.setFont(font)
        self.QLineUOPD.setObjectName("QLineUOPD")
        self.QComboxUAnswer = QtWidgets.QComboBox(self.Update)
        self.QComboxUAnswer.setGeometry(QtCore.QRect(400, 460, 69, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.QComboxUAnswer.setFont(font)
        self.QComboxUAnswer.setObjectName("QComboxUAnswer")
        self.QComboxUAnswer.addItem("")
        self.QComboxUAnswer.addItem("")
        self.QComboxUAnswer.addItem("")
        self.QComboxUAnswer.addItem("")
        self.QComboxUMaMH = QtWidgets.QComboBox(self.Update)
        self.QComboxUMaMH.setGeometry(QtCore.QRect(400, 520, 361, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QComboxUMaMH.setFont(font)
        self.QComboxUMaMH.setObjectName("QComboxUMaMH")
        self.tab.addTab(self.Update, "")
        self.Delete = QtWidgets.QWidget()
        self.Delete.setObjectName("Delete")
        self.ClearDelete = QtWidgets.QPushButton(self.Delete)
        self.ClearDelete.setGeometry(QtCore.QRect(1320, 150, 75, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ClearDelete.setFont(font)
        self.ClearDelete.setObjectName("ClearDelete")
        self.DeleteQuestion = QtWidgets.QPushButton(self.Delete)
        self.DeleteQuestion.setGeometry(QtCore.QRect(1220, 150, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DeleteQuestion.setFont(font)
        self.DeleteQuestion.setObjectName("DeleteQuestion")
        self.label_4 = QtWidgets.QLabel(self.Delete)
        self.label_4.setGeometry(QtCore.QRect(880, 90, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.QTableDelete = QtWidgets.QTableWidget(self.Delete)
        self.QTableDelete.setGeometry(QtCore.QRect(620, 190, 761, 351))
        self.QTableDelete.setMinimumSize(QtCore.QSize(10, 20))
        self.QTableDelete.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.QTableDelete.setAutoScrollMargin(16)
        self.QTableDelete.setObjectName("QTableDelete")
        self.QTableDelete.setColumnCount(8)
        self.QTableDelete.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableDelete.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableDelete.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableDelete.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableDelete.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableDelete.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableDelete.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableDelete.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableDelete.setHorizontalHeaderItem(7, item)
        self.QTableDelete.horizontalHeader().setDefaultSectionSize(85)
        self.QTableDelete.horizontalHeader().setMinimumSectionSize(24)
        self.QTableDelete.verticalHeader().setDefaultSectionSize(1)
        self.label_3 = QtWidgets.QLabel(self.Delete)
        self.label_3.setGeometry(QtCore.QRect(930, 150, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.Delete)
        self.label_6.setGeometry(QtCore.QRect(609, 150, 141, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.QLineDIDCauHoi = QtWidgets.QLineEdit(self.Delete)
        self.QLineDIDCauHoi.setGeometry(QtCore.QRect(740, 150, 161, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.QLineDIDCauHoi.setFont(font)
        self.QLineDIDCauHoi.setObjectName("QLineDIDCauHoi")
        self.QLineDCauHoi = QtWidgets.QLineEdit(self.Delete)
        self.QLineDCauHoi.setGeometry(QtCore.QRect(1020, 150, 151, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.QLineDCauHoi.setFont(font)
        self.QLineDCauHoi.setObjectName("QLineDCauHoi")
        self.tab.addTab(self.Delete, "")
        self.ShowAll = QtWidgets.QWidget()
        self.ShowAll.setObjectName("ShowAll")
        self.QTableShowAll = QtWidgets.QTableWidget(self.ShowAll)
        self.QTableShowAll.setGeometry(QtCore.QRect(560, 140, 871, 381))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.QTableShowAll.setFont(font)
        self.QTableShowAll.setObjectName("QTableShowAll")
        self.QTableShowAll.setColumnCount(8)
        self.QTableShowAll.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.QTableShowAll.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.QTableShowAll.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.QTableShowAll.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.QTableShowAll.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.QTableShowAll.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.QTableShowAll.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.QTableShowAll.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.QTableShowAll.setHorizontalHeaderItem(7, item)
        self.ButtonSASearch = QtWidgets.QPushButton(self.ShowAll)
        self.ButtonSASearch.setGeometry(QtCore.QRect(1229, 100, 91, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ButtonSASearch.setFont(font)
        self.ButtonSASearch.setObjectName("ButtonSASearch")
        self.ButtonSAClear = QtWidgets.QPushButton(self.ShowAll)
        self.ButtonSAClear.setGeometry(QtCore.QRect(1340, 100, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ButtonSAClear.setFont(font)
        self.ButtonSAClear.setObjectName("ButtonSAClear")
        self.label_14 = QtWidgets.QLabel(self.ShowAll)
        self.label_14.setGeometry(QtCore.QRect(920, 100, 101, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.QLineSACauHoi = QtWidgets.QLineEdit(self.ShowAll)
        self.QLineSACauHoi.setGeometry(QtCore.QRect(1030, 100, 151, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QLineSACauHoi.setFont(font)
        self.QLineSACauHoi.setObjectName("QLineSACauHoi")
        self.QLineSAMaCH = QtWidgets.QLineEdit(self.ShowAll)
        self.QLineSAMaCH.setGeometry(QtCore.QRect(730, 100, 161, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QLineSAMaCH.setFont(font)
        self.QLineSAMaCH.setObjectName("QLineSAMaCH")
        self.label_15 = QtWidgets.QLabel(self.ShowAll)
        self.label_15.setGeometry(QtCore.QRect(579, 100, 161, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.tab.addTab(self.ShowAll, "")
        self.gridLayout.addWidget(self.tab, 0, 0, 1, 1)
        self.ButtonBacked = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonBacked.setFont(font)
        self.ButtonBacked.setObjectName("ButtonBacked")
        self.gridLayout.addWidget(self.ButtonBacked, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.QLineAQuestion, self.QLineAOPA)
        MainWindow.setTabOrder(self.QLineAOPA, self.QLineAOPB)
        MainWindow.setTabOrder(self.QLineAOPB, self.QLineAOPC)
        MainWindow.setTabOrder(self.QLineAOPC, self.QLineAOPD)
        MainWindow.setTabOrder(self.QLineAOPD, self.QComboBoxAAnswer)
        MainWindow.setTabOrder(self.QComboBoxAAnswer, self.QComboxAMaMH)
        MainWindow.setTabOrder(self.QComboxAMaMH, self.ClearQuestion)
        MainWindow.setTabOrder(self.ClearQuestion, self.AddQuestion)
        MainWindow.setTabOrder(self.AddQuestion, self.QLineDCauHoi)
        MainWindow.setTabOrder(self.QLineDCauHoi, self.UpdateQuestion)
        MainWindow.setTabOrder(self.UpdateQuestion, self.QTableUpdate)
        MainWindow.setTabOrder(self.QTableUpdate, self.QLineUIDCauHoi)
        MainWindow.setTabOrder(self.QLineUIDCauHoi, self.QLineUQuestion)
        MainWindow.setTabOrder(self.QLineUQuestion, self.QLineUOPA)
        MainWindow.setTabOrder(self.QLineUOPA, self.QLineUOPB)
        MainWindow.setTabOrder(self.QLineUOPB, self.QLineUOPC)
        MainWindow.setTabOrder(self.QLineUOPC, self.QLineUOPD)
        MainWindow.setTabOrder(self.QLineUOPD, self.ClearDelete)
        MainWindow.setTabOrder(self.ClearDelete, self.DeleteQuestion)
        MainWindow.setTabOrder(self.DeleteQuestion, self.QTableDelete)
        MainWindow.setTabOrder(self.QTableDelete, self.QLineDIDCauHoi)
        MainWindow.setTabOrder(self.QLineDIDCauHoi, self.QTableShowAll)
        MainWindow.setTabOrder(self.QTableShowAll, self.ButtonSASearch)
        MainWindow.setTabOrder(self.ButtonSASearch, self.ButtonSAClear)
        MainWindow.setTabOrder(self.ButtonSAClear, self.ClearUpdate)
        MainWindow.setTabOrder(self.ClearUpdate, self.QComboxUAnswer)
        MainWindow.setTabOrder(self.QComboxUAnswer, self.QComboxUMaMH)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "ID:"))
        self.IDAddQuestion.setText(_translate("MainWindow", "111"))
        self.QLineAQuestion.setPlaceholderText(_translate("MainWindow", "Câu Hỏi"))
        self.QLineAOPA.setPlaceholderText(_translate("MainWindow", "Câu A"))
        self.QLineAOPB.setPlaceholderText(_translate("MainWindow", "Câu B"))
        self.QLineAOPC.setPlaceholderText(_translate("MainWindow", "Câu C"))
        self.QLineAOPD.setPlaceholderText(_translate("MainWindow", "Câu D"))
        self.label_7.setText(_translate("MainWindow", "Câu Hỏi:"))
        self.label_8.setText(_translate("MainWindow", "Câu A:"))
        self.label_9.setText(_translate("MainWindow", "Câu B:"))
        self.label_10.setText(_translate("MainWindow", "Câu D:"))
        self.label_11.setText(_translate("MainWindow", "Đáp Án:"))
        self.label_12.setText(_translate("MainWindow", "Câu Hỏi Của Môn:"))
        self.label_13.setText(_translate("MainWindow", "Câu C:"))
        self.ClearQuestion.setText(_translate("MainWindow", "Clear"))
        self.AddQuestion.setText(_translate("MainWindow", "Add"))
        self.QComboBoxAAnswer.setItemText(0, _translate("MainWindow", "A"))
        self.QComboBoxAAnswer.setItemText(1, _translate("MainWindow", "B"))
        self.QComboBoxAAnswer.setItemText(2, _translate("MainWindow", "C"))
        self.QComboBoxAAnswer.setItemText(3, _translate("MainWindow", "D"))
        self.tab.setTabText(self.tab.indexOf(self.Add), _translate("MainWindow", "Add"))
        self.UpdateQuestion.setText(_translate("MainWindow", "Update"))
        self.ClearUpdate.setText(_translate("MainWindow", "Clear"))
        item = self.QTableUpdate.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "MaCH"))
        item = self.QTableUpdate.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "CAU HOI"))
        item = self.QTableUpdate.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "CAU A"))
        item = self.QTableUpdate.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "CAU B"))
        item = self.QTableUpdate.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "CAU C"))
        item = self.QTableUpdate.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "CAU D"))
        item = self.QTableUpdate.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "DAP AN"))
        item = self.QTableUpdate.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "MaMH"))
        self.QLineUIDCauHoi.setPlaceholderText(_translate("MainWindow", "ID_CAU_HOI"))
        self.label.setText(_translate("MainWindow", "SUGGEST"))
        self.label_2.setText(_translate("MainWindow", "Press Enter for suggest"))
        self.label_25.setText(_translate("MainWindow", "Câu Hỏi:"))
        self.label_26.setText(_translate("MainWindow", "Câu B:"))
        self.label_27.setText(_translate("MainWindow", "Câu D:"))
        self.label_28.setText(_translate("MainWindow", "Câu A:"))
        self.label_29.setText(_translate("MainWindow", "Đáp Án:"))
        self.label_30.setText(_translate("MainWindow", "Câu Hỏi Của Môn:"))
        self.label_31.setText(_translate("MainWindow", "Câu C:"))
        self.label_32.setText(_translate("MainWindow", "ID:"))
        self.QLineUQuestion.setPlaceholderText(_translate("MainWindow", "CAU HOI"))
        self.QLineUOPA.setPlaceholderText(_translate("MainWindow", "CAU A"))
        self.QLineUOPB.setPlaceholderText(_translate("MainWindow", "CAU B"))
        self.QLineUOPC.setPlaceholderText(_translate("MainWindow", "CAU C"))
        self.QLineUOPD.setPlaceholderText(_translate("MainWindow", "CAU D"))
        self.QComboxUAnswer.setItemText(0, _translate("MainWindow", "A"))
        self.QComboxUAnswer.setItemText(1, _translate("MainWindow", "B"))
        self.QComboxUAnswer.setItemText(2, _translate("MainWindow", "C"))
        self.QComboxUAnswer.setItemText(3, _translate("MainWindow", "D"))
        self.tab.setTabText(self.tab.indexOf(self.Update), _translate("MainWindow", "Update"))
        self.ClearDelete.setText(_translate("MainWindow", "Clear"))
        self.DeleteQuestion.setText(_translate("MainWindow", "Delete"))
        self.label_4.setText(_translate("MainWindow", "Press Enter For Suggest"))
        item = self.QTableDelete.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "MaCH"))
        item = self.QTableDelete.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "CAU HOI"))
        item = self.QTableDelete.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "CAU A"))
        item = self.QTableDelete.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "CAU B"))
        item = self.QTableDelete.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "CAU C"))
        item = self.QTableDelete.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "CAU D"))
        item = self.QTableDelete.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "DAP AN"))
        item = self.QTableDelete.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "MaMH"))
        self.label_3.setText(_translate("MainWindow", "Câu Hỏi:"))
        self.label_6.setText(_translate("MainWindow", "Mã Câu Hỏi:"))
        self.QLineDIDCauHoi.setPlaceholderText(_translate("MainWindow", "Mã Câu Hỏi"))
        self.QLineDCauHoi.setPlaceholderText(_translate("MainWindow", "Câu Hỏi"))
        self.tab.setTabText(self.tab.indexOf(self.Delete), _translate("MainWindow", "Delete"))
        item = self.QTableShowAll.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "MaCH"))
        item = self.QTableShowAll.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Cau Hoi"))
        item = self.QTableShowAll.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Cau A"))
        item = self.QTableShowAll.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Cau B"))
        item = self.QTableShowAll.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Cau C"))
        item = self.QTableShowAll.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Cau D"))
        item = self.QTableShowAll.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Dap An"))
        item = self.QTableShowAll.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "MaMH"))
        self.ButtonSASearch.setText(_translate("MainWindow", "Search"))
        self.ButtonSAClear.setText(_translate("MainWindow", "Clear"))
        self.label_14.setText(_translate("MainWindow", "Câu Hỏi:"))
        self.QLineSACauHoi.setPlaceholderText(_translate("MainWindow", "Câu Hỏi"))
        self.QLineSAMaCH.setPlaceholderText(_translate("MainWindow", "Mã Câu Hỏi"))
        self.label_15.setText(_translate("MainWindow", "Mã Câu Hỏi:"))
        self.tab.setTabText(self.tab.indexOf(self.ShowAll), _translate("MainWindow", "ShowAll"))
        self.ButtonBacked.setText(_translate("MainWindow", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
