# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeTeacher.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1915, 937)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(510, 210, 971, 711))
        self.widget.setObjectName("widget")
        self.QButtonMH = QtWidgets.QPushButton(self.widget)
        self.QButtonMH.setGeometry(QtCore.QRect(330, 290, 270, 45))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.QButtonMH.setFont(font)
        self.QButtonMH.setObjectName("QButtonMH")
        self.QButtonSV = QtWidgets.QPushButton(self.widget)
        self.QButtonSV.setGeometry(QtCore.QRect(330, 220, 270, 45))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.QButtonSV.setFont(font)
        self.QButtonSV.setObjectName("QButtonSV")
        self.NAMEGV = QtWidgets.QLabel(self.widget)
        self.NAMEGV.setGeometry(QtCore.QRect(480, 110, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.NAMEGV.setFont(font)
        self.NAMEGV.setObjectName("NAMEGV")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(300, 110, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.QButtonCH = QtWidgets.QPushButton(self.widget)
        self.QButtonCH.setGeometry(QtCore.QRect(330, 360, 270, 45))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.QButtonCH.setFont(font)
        self.QButtonCH.setObjectName("QButtonCH")
        self.QButtonLogout = QtWidgets.QPushButton(self.widget)
        self.QButtonLogout.setGeometry(QtCore.QRect(330, 430, 270, 45))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.QButtonLogout.setFont(font)
        self.QButtonLogout.setObjectName("QButtonLogout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.QButtonMH.setText(_translate("MainWindow", "Thêm Môn Học"))
        self.QButtonSV.setText(_translate("MainWindow", "Thêm SV"))
        self.NAMEGV.setText(_translate("MainWindow", "GIAO VIEN"))
        self.label.setText(_translate("MainWindow", "Welcome"))
        self.QButtonCH.setText(_translate("MainWindow", "Thêm Câu Hỏi"))
        self.QButtonLogout.setText(_translate("MainWindow", "LOG OUT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
