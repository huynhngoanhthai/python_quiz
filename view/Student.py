# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Student.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1914, 943)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab = QtWidgets.QTabWidget(self.centralwidget)
        self.tab.setEnabled(True)
        self.tab.setGeometry(QtCore.QRect(290, 180, 1361, 611))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setBaseSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tab.setFont(font)
        self.tab.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tab.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab.setIconSize(QtCore.QSize(20, 20))
        self.tab.setObjectName("tab")
        self.Add = QtWidgets.QWidget()
        self.Add.setObjectName("Add")
        self.QLineAMaSV = QtWidgets.QLineEdit(self.Add)
        self.QLineAMaSV.setGeometry(QtCore.QRect(210, 80, 410, 43))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.QLineAMaSV.setFont(font)
        self.QLineAMaSV.setObjectName("QLineAMaSV")
        self.QLineAHoSV = QtWidgets.QLineEdit(self.Add)
        self.QLineAHoSV.setGeometry(QtCore.QRect(210, 130, 410, 43))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.QLineAHoSV.setFont(font)
        self.QLineAHoSV.setObjectName("QLineAHoSV")
        self.QLineATenSV = QtWidgets.QLineEdit(self.Add)
        self.QLineATenSV.setGeometry(QtCore.QRect(210, 180, 410, 43))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.QLineATenSV.setFont(font)
        self.QLineATenSV.setObjectName("QLineATenSV")
        self.OpNAM = QtWidgets.QRadioButton(self.Add)
        self.OpNAM.setGeometry(QtCore.QRect(240, 240, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.OpNAM.setFont(font)
        self.OpNAM.setObjectName("OpNAM")
        self.OpNU = QtWidgets.QRadioButton(self.Add)
        self.OpNU.setGeometry(QtCore.QRect(360, 240, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.OpNU.setFont(font)
        self.OpNU.setObjectName("OpNU")
        self.QDateANS = QtWidgets.QDateEdit(self.Add)
        self.QDateANS.setGeometry(QtCore.QRect(220, 290, 410, 43))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QDateANS.setFont(font)
        self.QDateANS.setDateTime(QtCore.QDateTime(QtCore.QDate(2001, 11, 4), QtCore.QTime(0, 0, 0)))
        self.QDateANS.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 11, 30), QtCore.QTime(23, 59, 59)))
        self.QDateANS.setMaximumDate(QtCore.QDate(2020, 11, 30))
        self.QDateANS.setDate(QtCore.QDate(2001, 11, 4))
        self.QDateANS.setObjectName("QDateANS")
        self.QLineADC = QtWidgets.QLineEdit(self.Add)
        self.QLineADC.setGeometry(QtCore.QRect(220, 340, 410, 43))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.QLineADC.setFont(font)
        self.QLineADC.setObjectName("QLineADC")
        self.QLineALop = QtWidgets.QLineEdit(self.Add)
        self.QLineALop.setGeometry(QtCore.QRect(220, 390, 410, 43))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.QLineALop.setFont(font)
        self.QLineALop.setObjectName("QLineALop")
        self.label_5 = QtWidgets.QLabel(self.Add)
        self.label_5.setGeometry(QtCore.QRect(90, 80, 110, 43))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.Add)
        self.label_7.setGeometry(QtCore.QRect(90, 130, 110, 43))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.Add)
        self.label_8.setGeometry(QtCore.QRect(90, 180, 110, 43))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.Add)
        self.label_9.setGeometry(QtCore.QRect(90, 230, 110, 43))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.Add)
        self.label_10.setGeometry(QtCore.QRect(70, 290, 131, 43))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.Add)
        self.label_11.setGeometry(QtCore.QRect(70, 340, 121, 43))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.Add)
        self.label_12.setGeometry(QtCore.QRect(110, 390, 110, 43))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.Add)
        self.label_13.setGeometry(QtCore.QRect(720, 110, 561, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.QButtonAAddStudent = QtWidgets.QPushButton(self.Add)
        self.QButtonAAddStudent.setGeometry(QtCore.QRect(310, 500, 85, 34))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.QButtonAAddStudent.setFont(font)
        self.QButtonAAddStudent.setObjectName("QButtonAAddStudent")
        self.QButtonAClear = QtWidgets.QPushButton(self.Add)
        self.QButtonAClear.setGeometry(QtCore.QRect(470, 500, 85, 34))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.QButtonAClear.setFont(font)
        self.QButtonAClear.setObjectName("QButtonAClear")
        self.QLineAEmail = QtWidgets.QLineEdit(self.Add)
        self.QLineAEmail.setGeometry(QtCore.QRect(220, 440, 410, 43))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.QLineAEmail.setFont(font)
        self.QLineAEmail.setObjectName("QLineAEmail")
        self.label_17 = QtWidgets.QLabel(self.Add)
        self.label_17.setGeometry(QtCore.QRect(110, 440, 110, 43))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.tab.addTab(self.Add, "")
        self.Update = QtWidgets.QWidget()
        self.Update.setObjectName("Update")
        self.QButtonUUpdate = QtWidgets.QPushButton(self.Update)
        self.QButtonUUpdate.setGeometry(QtCore.QRect(270, 490, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.QButtonUUpdate.setFont(font)
        self.QButtonUUpdate.setObjectName("QButtonUUpdate")
        self.QButtonUClear = QtWidgets.QPushButton(self.Update)
        self.QButtonUClear.setGeometry(QtCore.QRect(390, 490, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.QButtonUClear.setFont(font)
        self.QButtonUClear.setObjectName("QButtonUClear")
        self.QTableUpdate = QtWidgets.QTableWidget(self.Update)
        self.QTableUpdate.setEnabled(True)
        self.QTableUpdate.setGeometry(QtCore.QRect(585, 150, 731, 281))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QTableUpdate.sizePolicy().hasHeightForWidth())
        self.QTableUpdate.setSizePolicy(sizePolicy)
        self.QTableUpdate.setMinimumSize(QtCore.QSize(731, 20))
        self.QTableUpdate.setMaximumSize(QtCore.QSize(731, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.QTableUpdate.setFont(font)
        self.QTableUpdate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.QTableUpdate.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.CurrentChanged|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.QTableUpdate.setDragEnabled(True)
        self.QTableUpdate.setDragDropOverwriteMode(False)
        self.QTableUpdate.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.QTableUpdate.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.QTableUpdate.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.QTableUpdate.setGridStyle(QtCore.Qt.CustomDashLine)
        self.QTableUpdate.setRowCount(1)
        self.QTableUpdate.setObjectName("QTableUpdate")
        self.QTableUpdate.setColumnCount(8)
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
        self.label = QtWidgets.QLabel(self.Update)
        self.label.setGeometry(QtCore.QRect(780, 100, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Update)
        self.label_2.setGeometry(QtCore.QRect(220, 90, 321, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.QLineUMaSV = QtWidgets.QLineEdit(self.Update)
        self.QLineUMaSV.setGeometry(QtCore.QRect(240, 150, 311, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.QLineUMaSV.setFont(font)
        self.QLineUMaSV.setObjectName("QLineUMaSV")
        self.QLineUHoSV = QtWidgets.QLineEdit(self.Update)
        self.QLineUHoSV.setGeometry(QtCore.QRect(240, 190, 311, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.QLineUHoSV.setFont(font)
        self.QLineUHoSV.setObjectName("QLineUHoSV")
        self.QLineUTenSV = QtWidgets.QLineEdit(self.Update)
        self.QLineUTenSV.setGeometry(QtCore.QRect(240, 230, 311, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.QLineUTenSV.setFont(font)
        self.QLineUTenSV.setObjectName("QLineUTenSV")
        self.label_18 = QtWidgets.QLabel(self.Update)
        self.label_18.setGeometry(QtCore.QRect(130, 150, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.Update)
        self.label_19.setGeometry(QtCore.QRect(130, 190, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.Update)
        self.label_20.setGeometry(QtCore.QRect(130, 230, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.Update)
        self.label_21.setGeometry(QtCore.QRect(130, 270, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.Update)
        self.label_22.setGeometry(QtCore.QRect(90, 310, 151, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.Update)
        self.label_23.setGeometry(QtCore.QRect(90, 350, 131, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.Update)
        self.label_24.setGeometry(QtCore.QRect(130, 390, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.OpUPhai = QtWidgets.QComboBox(self.Update)
        self.OpUPhai.setGeometry(QtCore.QRect(240, 270, 91, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.OpUPhai.setFont(font)
        self.OpUPhai.setObjectName("OpUPhai")
        self.OpUPhai.addItem("")
        self.OpUPhai.addItem("")
        self.QDateUNgaySinh = QtWidgets.QDateEdit(self.Update)
        self.QDateUNgaySinh.setGeometry(QtCore.QRect(240, 310, 171, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QDateUNgaySinh.setFont(font)
        self.QDateUNgaySinh.setDateTime(QtCore.QDateTime(QtCore.QDate(2001, 11, 4), QtCore.QTime(0, 0, 0)))
        self.QDateUNgaySinh.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 12, 31), QtCore.QTime(23, 59, 59)))
        self.QDateUNgaySinh.setDate(QtCore.QDate(2001, 11, 4))
        self.QDateUNgaySinh.setObjectName("QDateUNgaySinh")
        self.QLineUNoiSinh = QtWidgets.QLineEdit(self.Update)
        self.QLineUNoiSinh.setGeometry(QtCore.QRect(240, 350, 311, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.QLineUNoiSinh.setFont(font)
        self.QLineUNoiSinh.setObjectName("QLineUNoiSinh")
        self.QLineULop = QtWidgets.QLineEdit(self.Update)
        self.QLineULop.setGeometry(QtCore.QRect(240, 390, 311, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.QLineULop.setFont(font)
        self.QLineULop.setObjectName("QLineULop")
        self.label_25 = QtWidgets.QLabel(self.Update)
        self.label_25.setGeometry(QtCore.QRect(130, 430, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.QLineUEmail = QtWidgets.QLineEdit(self.Update)
        self.QLineUEmail.setGeometry(QtCore.QRect(240, 430, 311, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.QLineUEmail.setFont(font)
        self.QLineUEmail.setObjectName("QLineUEmail")
        self.tab.addTab(self.Update, "")
        self.Delete = QtWidgets.QWidget()
        self.Delete.setObjectName("Delete")
        self.QButtonDClear = QtWidgets.QPushButton(self.Delete)
        self.QButtonDClear.setGeometry(QtCore.QRect(1100, 90, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.QButtonDClear.setFont(font)
        self.QButtonDClear.setObjectName("QButtonDClear")
        self.QButtonDDelete = QtWidgets.QPushButton(self.Delete)
        self.QButtonDDelete.setGeometry(QtCore.QRect(1010, 90, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.QButtonDDelete.setFont(font)
        self.QButtonDDelete.setObjectName("QButtonDDelete")
        self.label_4 = QtWidgets.QLabel(self.Delete)
        self.label_4.setGeometry(QtCore.QRect(610, 50, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.QTableDelete = QtWidgets.QTableWidget(self.Delete)
        self.QTableDelete.setEnabled(True)
        self.QTableDelete.setGeometry(QtCore.QRect(260, 140, 971, 411))
        self.QTableDelete.setMinimumSize(QtCore.QSize(10, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.QTableDelete.setFont(font)
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
        self.QTableDelete.setHorizontalHeaderItem(7, item)
        self.QTableDelete.horizontalHeader().setDefaultSectionSize(101)
        self.QTableDelete.horizontalHeader().setMinimumSectionSize(24)
        self.QTableDelete.verticalHeader().setDefaultSectionSize(1)
        self.label_3 = QtWidgets.QLabel(self.Delete)
        self.label_3.setGeometry(QtCore.QRect(720, 90, 51, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.Delete)
        self.label_6.setGeometry(QtCore.QRect(350, 90, 161, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.QLineDMaSV = QtWidgets.QLineEdit(self.Delete)
        self.QLineDMaSV.setGeometry(QtCore.QRect(510, 90, 181, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QLineDMaSV.setFont(font)
        self.QLineDMaSV.setObjectName("QLineDMaSV")
        self.QLineDTenSV = QtWidgets.QLineEdit(self.Delete)
        self.QLineDTenSV.setGeometry(QtCore.QRect(770, 90, 191, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QLineDTenSV.setFont(font)
        self.QLineDTenSV.setDragEnabled(False)
        self.QLineDTenSV.setReadOnly(False)
        self.QLineDTenSV.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.QLineDTenSV.setObjectName("QLineDTenSV")
        self.QButtonDClear.raise_()
        self.QButtonDDelete.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.label_6.raise_()
        self.QLineDMaSV.raise_()
        self.QLineDTenSV.raise_()
        self.QTableDelete.raise_()
        self.tab.addTab(self.Delete, "")
        self.ShowAll = QtWidgets.QWidget()
        self.ShowAll.setObjectName("ShowAll")
        self.label_14 = QtWidgets.QLabel(self.ShowAll)
        self.label_14.setGeometry(QtCore.QRect(420, 110, 101, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_16 = QtWidgets.QLabel(self.ShowAll)
        self.label_16.setGeometry(QtCore.QRect(570, 50, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.QButtonShowAll = QtWidgets.QPushButton(self.ShowAll)
        self.QButtonShowAll.setGeometry(QtCore.QRect(870, 110, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.QButtonShowAll.setFont(font)
        self.QButtonShowAll.setObjectName("QButtonShowAll")
        self.QButtonSAClear = QtWidgets.QPushButton(self.ShowAll)
        self.QButtonSAClear.setGeometry(QtCore.QRect(990, 110, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.QButtonSAClear.setFont(font)
        self.QButtonSAClear.setObjectName("QButtonSAClear")
        self.QTableShowAll = QtWidgets.QTableWidget(self.ShowAll)
        self.QTableShowAll.setGeometry(QtCore.QRect(270, 160, 951, 351))
        self.QTableShowAll.setMinimumSize(QtCore.QSize(10, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.QTableShowAll.setFont(font)
        self.QTableShowAll.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.QTableShowAll.setAutoScrollMargin(16)
        self.QTableShowAll.setObjectName("QTableShowAll")
        self.QTableShowAll.setColumnCount(8)
        self.QTableShowAll.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableShowAll.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableShowAll.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableShowAll.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableShowAll.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableShowAll.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableShowAll.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableShowAll.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableShowAll.setHorizontalHeaderItem(7, item)
        self.QTableShowAll.horizontalHeader().setDefaultSectionSize(101)
        self.QTableShowAll.horizontalHeader().setMinimumSectionSize(24)
        self.QTableShowAll.verticalHeader().setDefaultSectionSize(1)
        self.QLineSATenLop = QtWidgets.QLineEdit(self.ShowAll)
        self.QLineSATenLop.setGeometry(QtCore.QRect(530, 110, 161, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.QLineSATenLop.setFont(font)
        self.QLineSATenLop.setObjectName("QLineSATenLop")
        self.tab.addTab(self.ShowAll, "")
        self.ShowDiem = QtWidgets.QWidget()
        self.ShowDiem.setObjectName("ShowDiem")
        self.QLineSDMaMH = QtWidgets.QLineEdit(self.ShowDiem)
        self.QLineSDMaMH.setGeometry(QtCore.QRect(410, 90, 231, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QLineSDMaMH.setFont(font)
        self.QLineSDMaMH.setObjectName("QLineSDMaMH")
        self.QTableShowDiem = QtWidgets.QTableWidget(self.ShowDiem)
        self.QTableShowDiem.setGeometry(QtCore.QRect(200, 140, 841, 331))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.QTableShowDiem.setFont(font)
        self.QTableShowDiem.setObjectName("QTableShowDiem")
        self.QTableShowDiem.setColumnCount(6)
        self.QTableShowDiem.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.QTableShowDiem.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.QTableShowDiem.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.QTableShowDiem.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.QTableShowDiem.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.QTableShowDiem.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.QTableShowDiem.setHorizontalHeaderItem(5, item)
        self.QButtonSDSearch = QtWidgets.QPushButton(self.ShowDiem)
        self.QButtonSDSearch.setGeometry(QtCore.QRect(770, 90, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QButtonSDSearch.setFont(font)
        self.QButtonSDSearch.setObjectName("QButtonSDSearch")
        self.QButtonSDClear = QtWidgets.QPushButton(self.ShowDiem)
        self.QButtonSDClear.setGeometry(QtCore.QRect(870, 90, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QButtonSDClear.setFont(font)
        self.QButtonSDClear.setObjectName("QButtonSDClear")
        self.label_26 = QtWidgets.QLabel(self.ShowDiem)
        self.label_26.setGeometry(QtCore.QRect(270, 90, 131, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.tab.addTab(self.ShowDiem, "")
        self.QButtonBack = QtWidgets.QPushButton(self.centralwidget)
        self.QButtonBack.setGeometry(QtCore.QRect(1510, 820, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.QButtonBack.setFont(font)
        self.QButtonBack.setObjectName("QButtonBack")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.OpNAM.setText(_translate("MainWindow", "NAM"))
        self.OpNU.setText(_translate("MainWindow", "NU"))
        self.QDateANS.setDisplayFormat(_translate("MainWindow", "d/M/yyyy"))
        self.label_5.setText(_translate("MainWindow", "MaSV"))
        self.label_7.setText(_translate("MainWindow", "HoSV"))
        self.label_8.setText(_translate("MainWindow", "TenSV"))
        self.label_9.setText(_translate("MainWindow", "Phai"))
        self.label_10.setText(_translate("MainWindow", "Ngai Sinh"))
        self.label_11.setText(_translate("MainWindow", "Noi Sinh"))
        self.label_12.setText(_translate("MainWindow", "Lop"))
        self.label_13.setText(_translate("MainWindow", "Password Của Sinh Viên Trùng Với MaSV"))
        self.QButtonAAddStudent.setText(_translate("MainWindow", "Add"))
        self.QButtonAClear.setText(_translate("MainWindow", "Clear"))
        self.label_17.setText(_translate("MainWindow", "Email"))
        self.tab.setTabText(self.tab.indexOf(self.Add), _translate("MainWindow", "Add"))
        self.QButtonUUpdate.setText(_translate("MainWindow", "Update"))
        self.QButtonUClear.setText(_translate("MainWindow", "Clear"))
        item = self.QTableUpdate.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "MaSV"))
        item = self.QTableUpdate.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "HoSV"))
        item = self.QTableUpdate.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "TenSV"))
        item = self.QTableUpdate.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "PHAI"))
        item = self.QTableUpdate.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "NGAY SINH"))
        item = self.QTableUpdate.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "NOI SINH"))
        item = self.QTableUpdate.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "LOP"))
        item = self.QTableUpdate.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "EMAIL"))
        self.label.setText(_translate("MainWindow", "SUGGEST"))
        self.label_2.setText(_translate("MainWindow", "Press Enter for suggest"))
        self.label_18.setText(_translate("MainWindow", "MaSV"))
        self.label_19.setText(_translate("MainWindow", "HoSV"))
        self.label_20.setText(_translate("MainWindow", "TenSV"))
        self.label_21.setText(_translate("MainWindow", "Phai"))
        self.label_22.setText(_translate("MainWindow", "Ngay Sinh"))
        self.label_23.setText(_translate("MainWindow", "Noi Sinh"))
        self.label_24.setText(_translate("MainWindow", "Lop"))
        self.OpUPhai.setItemText(0, _translate("MainWindow", "NAM"))
        self.OpUPhai.setItemText(1, _translate("MainWindow", "NU"))
        self.QDateUNgaySinh.setDisplayFormat(_translate("MainWindow", "d/M/yyyy"))
        self.label_25.setText(_translate("MainWindow", "Email"))
        self.tab.setTabText(self.tab.indexOf(self.Update), _translate("MainWindow", "Update"))
        self.QButtonDClear.setText(_translate("MainWindow", "Clear"))
        self.QButtonDDelete.setText(_translate("MainWindow", "Delete"))
        self.label_4.setText(_translate("MainWindow", "Press Enter For Suggest"))
        item = self.QTableDelete.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "MaSV"))
        item = self.QTableDelete.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "HoSV"))
        item = self.QTableDelete.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "TenSV"))
        item = self.QTableDelete.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Phai"))
        item = self.QTableDelete.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "NgaySinh"))
        item = self.QTableDelete.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "NoiSinh"))
        item = self.QTableDelete.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "TenLop"))
        item = self.QTableDelete.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Email"))
        self.label_3.setText(_translate("MainWindow", "TEN"))
        self.label_6.setText(_translate("MainWindow", "MA SINH VIEN"))
        self.QLineDMaSV.setPlaceholderText(_translate("MainWindow", "Ma Sinh Vien"))
        self.QLineDTenSV.setPlaceholderText(_translate("MainWindow", "Ten Sinh Vien"))
        self.tab.setTabText(self.tab.indexOf(self.Delete), _translate("MainWindow", "Delete"))
        self.label_14.setText(_translate("MainWindow", "Ten Lop"))
        self.label_16.setText(_translate("MainWindow", "Press Enter for suggest"))
        self.QButtonShowAll.setText(_translate("MainWindow", "Show"))
        self.QButtonSAClear.setText(_translate("MainWindow", "Clear"))
        item = self.QTableShowAll.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "MaSV"))
        item = self.QTableShowAll.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "HoSV"))
        item = self.QTableShowAll.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "TenSV"))
        item = self.QTableShowAll.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Phai"))
        item = self.QTableShowAll.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "NgaySinh"))
        item = self.QTableShowAll.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "NoiSinh"))
        item = self.QTableShowAll.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "TenLop"))
        item = self.QTableShowAll.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Email"))
        self.tab.setTabText(self.tab.indexOf(self.ShowAll), _translate("MainWindow", "ShowAll"))
        self.QLineSDMaMH.setPlaceholderText(_translate("MainWindow", "Ma Mon Hoc"))
        item = self.QTableShowDiem.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "MaMH"))
        item = self.QTableShowDiem.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "MaSV"))
        item = self.QTableShowDiem.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "HoSV"))
        item = self.QTableShowDiem.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "TenSV"))
        item = self.QTableShowDiem.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "TenMH"))
        item = self.QTableShowDiem.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Diem"))
        self.QButtonSDSearch.setText(_translate("MainWindow", "Search"))
        self.QButtonSDClear.setText(_translate("MainWindow", "Clear"))
        self.label_26.setText(_translate("MainWindow", "Ma Mon Hoc"))
        self.tab.setTabText(self.tab.indexOf(self.ShowDiem), _translate("MainWindow", "ShowDiem"))
        self.QButtonBack.setText(_translate("MainWindow", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
