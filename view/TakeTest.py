# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TakeTest.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1908, 877)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(300, 140, 1271, 711))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.D = QtWidgets.QRadioButton(self.tab)
        self.D.setGeometry(QtCore.QRect(330, 440, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.D.setFont(font)
        self.D.setObjectName("D")
        self.C = QtWidgets.QRadioButton(self.tab)
        self.C.setGeometry(QtCore.QRect(330, 370, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.C.setFont(font)
        self.C.setObjectName("C")
        self.A = QtWidgets.QRadioButton(self.tab)
        self.A.setGeometry(QtCore.QRect(330, 230, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.A.setFont(font)
        self.A.setObjectName("A")
        self.question = QtWidgets.QLabel(self.tab)
        self.question.setGeometry(QtCore.QRect(230, 100, 761, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.question.setFont(font)
        self.question.setWordWrap(True)
        self.question.setObjectName("question")
        self.B = QtWidgets.QRadioButton(self.tab)
        self.B.setGeometry(QtCore.QRect(330, 300, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B.setFont(font)
        self.B.setObjectName("B")
        self.id_question = QtWidgets.QLabel(self.tab)
        self.id_question.setGeometry(QtCore.QRect(180, 110, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.id_question.setFont(font)
        self.id_question.setObjectName("id_question")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.B_2 = QtWidgets.QRadioButton(self.tab_2)
        self.B_2.setGeometry(QtCore.QRect(330, 300, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_2.setFont(font)
        self.B_2.setObjectName("B_2")
        self.C_2 = QtWidgets.QRadioButton(self.tab_2)
        self.C_2.setGeometry(QtCore.QRect(330, 370, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.C_2.setFont(font)
        self.C_2.setObjectName("C_2")
        self.D_2 = QtWidgets.QRadioButton(self.tab_2)
        self.D_2.setGeometry(QtCore.QRect(330, 440, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.D_2.setFont(font)
        self.D_2.setObjectName("D_2")
        self.question_2 = QtWidgets.QLabel(self.tab_2)
        self.question_2.setGeometry(QtCore.QRect(230, 100, 761, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.question_2.setFont(font)
        self.question_2.setWordWrap(True)
        self.question_2.setObjectName("question_2")
        self.A_2 = QtWidgets.QRadioButton(self.tab_2)
        self.A_2.setGeometry(QtCore.QRect(330, 230, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.A_2.setFont(font)
        self.A_2.setObjectName("A_2")
        self.id_question2 = QtWidgets.QLabel(self.tab_2)
        self.id_question2.setGeometry(QtCore.QRect(180, 110, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.id_question2.setFont(font)
        self.id_question2.setObjectName("id_question2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.C_3 = QtWidgets.QRadioButton(self.tab_3)
        self.C_3.setGeometry(QtCore.QRect(330, 370, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.C_3.setFont(font)
        self.C_3.setObjectName("C_3")
        self.question_3 = QtWidgets.QLabel(self.tab_3)
        self.question_3.setGeometry(QtCore.QRect(230, 100, 761, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.question_3.setFont(font)
        self.question_3.setWordWrap(True)
        self.question_3.setObjectName("question_3")
        self.B_3 = QtWidgets.QRadioButton(self.tab_3)
        self.B_3.setGeometry(QtCore.QRect(330, 300, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_3.setFont(font)
        self.B_3.setObjectName("B_3")
        self.A_3 = QtWidgets.QRadioButton(self.tab_3)
        self.A_3.setGeometry(QtCore.QRect(330, 230, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.A_3.setFont(font)
        self.A_3.setObjectName("A_3")
        self.D_3 = QtWidgets.QRadioButton(self.tab_3)
        self.D_3.setGeometry(QtCore.QRect(330, 440, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.D_3.setFont(font)
        self.D_3.setObjectName("D_3")
        self.id_question3 = QtWidgets.QLabel(self.tab_3)
        self.id_question3.setGeometry(QtCore.QRect(180, 120, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.id_question3.setFont(font)
        self.id_question3.setObjectName("id_question3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.id_question4 = QtWidgets.QLabel(self.tab_4)
        self.id_question4.setGeometry(QtCore.QRect(180, 110, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.id_question4.setFont(font)
        self.id_question4.setObjectName("id_question4")
        self.A_4 = QtWidgets.QRadioButton(self.tab_4)
        self.A_4.setGeometry(QtCore.QRect(330, 230, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.A_4.setFont(font)
        self.A_4.setObjectName("A_4")
        self.D_4 = QtWidgets.QRadioButton(self.tab_4)
        self.D_4.setGeometry(QtCore.QRect(330, 440, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.D_4.setFont(font)
        self.D_4.setObjectName("D_4")
        self.B_4 = QtWidgets.QRadioButton(self.tab_4)
        self.B_4.setGeometry(QtCore.QRect(330, 300, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_4.setFont(font)
        self.B_4.setObjectName("B_4")
        self.C_4 = QtWidgets.QRadioButton(self.tab_4)
        self.C_4.setGeometry(QtCore.QRect(330, 370, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.C_4.setFont(font)
        self.C_4.setObjectName("C_4")
        self.question_4 = QtWidgets.QLabel(self.tab_4)
        self.question_4.setGeometry(QtCore.QRect(230, 100, 761, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.question_4.setFont(font)
        self.question_4.setWordWrap(True)
        self.question_4.setObjectName("question_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.id_question5 = QtWidgets.QLabel(self.tab_5)
        self.id_question5.setGeometry(QtCore.QRect(180, 110, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.id_question5.setFont(font)
        self.id_question5.setObjectName("id_question5")
        self.A_5 = QtWidgets.QRadioButton(self.tab_5)
        self.A_5.setGeometry(QtCore.QRect(330, 230, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.A_5.setFont(font)
        self.A_5.setObjectName("A_5")
        self.D_5 = QtWidgets.QRadioButton(self.tab_5)
        self.D_5.setGeometry(QtCore.QRect(330, 440, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.D_5.setFont(font)
        self.D_5.setObjectName("D_5")
        self.B_5 = QtWidgets.QRadioButton(self.tab_5)
        self.B_5.setGeometry(QtCore.QRect(330, 300, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_5.setFont(font)
        self.B_5.setObjectName("B_5")
        self.C_5 = QtWidgets.QRadioButton(self.tab_5)
        self.C_5.setGeometry(QtCore.QRect(330, 370, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.C_5.setFont(font)
        self.C_5.setObjectName("C_5")
        self.question_5 = QtWidgets.QLabel(self.tab_5)
        self.question_5.setGeometry(QtCore.QRect(230, 100, 761, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.question_5.setFont(font)
        self.question_5.setWordWrap(True)
        self.question_5.setObjectName("question_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.id_question6 = QtWidgets.QLabel(self.tab_6)
        self.id_question6.setGeometry(QtCore.QRect(180, 110, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.id_question6.setFont(font)
        self.id_question6.setObjectName("id_question6")
        self.A_6 = QtWidgets.QRadioButton(self.tab_6)
        self.A_6.setGeometry(QtCore.QRect(330, 230, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.A_6.setFont(font)
        self.A_6.setObjectName("A_6")
        self.D_6 = QtWidgets.QRadioButton(self.tab_6)
        self.D_6.setGeometry(QtCore.QRect(330, 440, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.D_6.setFont(font)
        self.D_6.setObjectName("D_6")
        self.B_6 = QtWidgets.QRadioButton(self.tab_6)
        self.B_6.setGeometry(QtCore.QRect(330, 300, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_6.setFont(font)
        self.B_6.setObjectName("B_6")
        self.C_6 = QtWidgets.QRadioButton(self.tab_6)
        self.C_6.setGeometry(QtCore.QRect(330, 370, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.C_6.setFont(font)
        self.C_6.setObjectName("C_6")
        self.question_6 = QtWidgets.QLabel(self.tab_6)
        self.question_6.setGeometry(QtCore.QRect(230, 100, 761, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.question_6.setFont(font)
        self.question_6.setWordWrap(True)
        self.question_6.setObjectName("question_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.id_question7 = QtWidgets.QLabel(self.tab_7)
        self.id_question7.setGeometry(QtCore.QRect(180, 110, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.id_question7.setFont(font)
        self.id_question7.setObjectName("id_question7")
        self.A_7 = QtWidgets.QRadioButton(self.tab_7)
        self.A_7.setGeometry(QtCore.QRect(330, 230, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.A_7.setFont(font)
        self.A_7.setObjectName("A_7")
        self.D_7 = QtWidgets.QRadioButton(self.tab_7)
        self.D_7.setGeometry(QtCore.QRect(330, 440, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.D_7.setFont(font)
        self.D_7.setObjectName("D_7")
        self.B_7 = QtWidgets.QRadioButton(self.tab_7)
        self.B_7.setGeometry(QtCore.QRect(330, 300, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_7.setFont(font)
        self.B_7.setObjectName("B_7")
        self.C_7 = QtWidgets.QRadioButton(self.tab_7)
        self.C_7.setGeometry(QtCore.QRect(330, 370, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.C_7.setFont(font)
        self.C_7.setObjectName("C_7")
        self.question_7 = QtWidgets.QLabel(self.tab_7)
        self.question_7.setGeometry(QtCore.QRect(230, 100, 761, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.question_7.setFont(font)
        self.question_7.setWordWrap(True)
        self.question_7.setObjectName("question_7")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.id_question8 = QtWidgets.QLabel(self.tab_8)
        self.id_question8.setGeometry(QtCore.QRect(180, 110, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.id_question8.setFont(font)
        self.id_question8.setObjectName("id_question8")
        self.A_8 = QtWidgets.QRadioButton(self.tab_8)
        self.A_8.setGeometry(QtCore.QRect(330, 230, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.A_8.setFont(font)
        self.A_8.setObjectName("A_8")
        self.D_8 = QtWidgets.QRadioButton(self.tab_8)
        self.D_8.setGeometry(QtCore.QRect(330, 440, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.D_8.setFont(font)
        self.D_8.setObjectName("D_8")
        self.B_8 = QtWidgets.QRadioButton(self.tab_8)
        self.B_8.setGeometry(QtCore.QRect(330, 300, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_8.setFont(font)
        self.B_8.setObjectName("B_8")
        self.C_8 = QtWidgets.QRadioButton(self.tab_8)
        self.C_8.setGeometry(QtCore.QRect(330, 370, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.C_8.setFont(font)
        self.C_8.setObjectName("C_8")
        self.question_8 = QtWidgets.QLabel(self.tab_8)
        self.question_8.setGeometry(QtCore.QRect(230, 100, 751, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.question_8.setFont(font)
        self.question_8.setWordWrap(True)
        self.question_8.setObjectName("question_8")
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.id_question9 = QtWidgets.QLabel(self.tab_9)
        self.id_question9.setGeometry(QtCore.QRect(180, 110, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.id_question9.setFont(font)
        self.id_question9.setObjectName("id_question9")
        self.A_9 = QtWidgets.QRadioButton(self.tab_9)
        self.A_9.setGeometry(QtCore.QRect(330, 230, 661, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.A_9.setFont(font)
        self.A_9.setObjectName("A_9")
        self.D_9 = QtWidgets.QRadioButton(self.tab_9)
        self.D_9.setGeometry(QtCore.QRect(330, 440, 661, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.D_9.setFont(font)
        self.D_9.setObjectName("D_9")
        self.B_9 = QtWidgets.QRadioButton(self.tab_9)
        self.B_9.setGeometry(QtCore.QRect(330, 300, 661, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_9.setFont(font)
        self.B_9.setObjectName("B_9")
        self.C_9 = QtWidgets.QRadioButton(self.tab_9)
        self.C_9.setGeometry(QtCore.QRect(330, 370, 661, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.C_9.setFont(font)
        self.C_9.setObjectName("C_9")
        self.question_9 = QtWidgets.QLabel(self.tab_9)
        self.question_9.setGeometry(QtCore.QRect(230, 100, 761, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.question_9.setFont(font)
        self.question_9.setWordWrap(True)
        self.question_9.setObjectName("question_9")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.question_10 = QtWidgets.QLabel(self.tab_10)
        self.question_10.setGeometry(QtCore.QRect(230, 90, 851, 111))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.question_10.setFont(font)
        self.question_10.setWordWrap(True)
        self.question_10.setObjectName("question_10")
        self.A_10 = QtWidgets.QRadioButton(self.tab_10)
        self.A_10.setGeometry(QtCore.QRect(330, 230, 601, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.A_10.setFont(font)
        self.A_10.setObjectName("A_10")
        self.D_10 = QtWidgets.QRadioButton(self.tab_10)
        self.D_10.setGeometry(QtCore.QRect(330, 440, 601, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.D_10.setFont(font)
        self.D_10.setObjectName("D_10")
        self.B_10 = QtWidgets.QRadioButton(self.tab_10)
        self.B_10.setGeometry(QtCore.QRect(330, 300, 601, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_10.setFont(font)
        self.B_10.setObjectName("B_10")
        self.C_10 = QtWidgets.QRadioButton(self.tab_10)
        self.C_10.setGeometry(QtCore.QRect(330, 370, 601, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.C_10.setFont(font)
        self.C_10.setObjectName("C_10")
        self.finish = QtWidgets.QPushButton(self.tab_10)
        self.finish.setGeometry(QtCore.QRect(900, 570, 291, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.finish.setFont(font)
        self.finish.setObjectName("finish")
        self.id_question10 = QtWidgets.QLabel(self.tab_10)
        self.id_question10.setGeometry(QtCore.QRect(180, 110, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.id_question10.setFont(font)
        self.id_question10.setObjectName("id_question10")
        self.tabWidget.addTab(self.tab_10, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1908, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.D.setText(_translate("MainWindow", "D. xyz"))
        self.C.setText(_translate("MainWindow", "C. dca"))
        self.A.setText(_translate("MainWindow", "A. bcd"))
        self.question.setText(_translate("MainWindow", "Ai là abc?"))
        self.B.setText(_translate("MainWindow", "B. aab"))
        self.id_question.setText(_translate("MainWindow", "ID câu hỏi"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Câu 1"))
        self.B_2.setText(_translate("MainWindow", "B. qyt"))
        self.C_2.setText(_translate("MainWindow", "C. ajs"))
        self.D_2.setText(_translate("MainWindow", "D. znx"))
        self.question_2.setText(_translate("MainWindow", "Cái gì là ijk?"))
        self.A_2.setText(_translate("MainWindow", "A. mno"))
        self.id_question2.setText(_translate("MainWindow", "ID câu hỏi"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Câu 2"))
        self.C_3.setText(_translate("MainWindow", "C. dca"))
        self.question_3.setText(_translate("MainWindow", "Ai là 123456?"))
        self.B_3.setText(_translate("MainWindow", "B. aab"))
        self.A_3.setText(_translate("MainWindow", "A. bcd"))
        self.D_3.setText(_translate("MainWindow", "D. xyz"))
        self.id_question3.setText(_translate("MainWindow", "ID câu hỏi"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Câu 3"))
        self.id_question4.setText(_translate("MainWindow", "ID câu hỏi"))
        self.A_4.setText(_translate("MainWindow", "A. bcd"))
        self.D_4.setText(_translate("MainWindow", "D. xyz"))
        self.B_4.setText(_translate("MainWindow", "B. aab"))
        self.C_4.setText(_translate("MainWindow", "C. dca"))
        self.question_4.setText(_translate("MainWindow", "123?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Câu 4"))
        self.id_question5.setText(_translate("MainWindow", "ID câu hỏi"))
        self.A_5.setText(_translate("MainWindow", "A. bcd"))
        self.D_5.setText(_translate("MainWindow", "D. xyz"))
        self.B_5.setText(_translate("MainWindow", "B. aab"))
        self.C_5.setText(_translate("MainWindow", "C. dca"))
        self.question_5.setText(_translate("MainWindow", "456?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Câu 5"))
        self.id_question6.setText(_translate("MainWindow", "ID câu hỏi"))
        self.A_6.setText(_translate("MainWindow", "A. bcd"))
        self.D_6.setText(_translate("MainWindow", "D. xyz"))
        self.B_6.setText(_translate("MainWindow", "B. aab"))
        self.C_6.setText(_translate("MainWindow", "C. dca"))
        self.question_6.setText(_translate("MainWindow", "A?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Câu 6"))
        self.id_question7.setText(_translate("MainWindow", "ID câu hỏi"))
        self.A_7.setText(_translate("MainWindow", "A. bcd"))
        self.D_7.setText(_translate("MainWindow", "D. xyz"))
        self.B_7.setText(_translate("MainWindow", "B. aab"))
        self.C_7.setText(_translate("MainWindow", "C. dca"))
        self.question_7.setText(_translate("MainWindow", "AAAAA?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Câu 7"))
        self.id_question8.setText(_translate("MainWindow", "ID câu hỏi"))
        self.A_8.setText(_translate("MainWindow", "A. bcd"))
        self.D_8.setText(_translate("MainWindow", "D. xyz"))
        self.B_8.setText(_translate("MainWindow", "B. aab"))
        self.C_8.setText(_translate("MainWindow", "C. dca"))
        self.question_8.setText(_translate("MainWindow", "A?????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "Câu 8"))
        self.id_question9.setText(_translate("MainWindow", "ID câu hỏi"))
        self.A_9.setText(_translate("MainWindow", "A. bcd"))
        self.D_9.setText(_translate("MainWindow", "D. xyz"))
        self.B_9.setText(_translate("MainWindow", "B. aab"))
        self.C_9.setText(_translate("MainWindow", "C. dca"))
        self.question_9.setText(_translate("MainWindow", "ABACAS?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("MainWindow", "Câu 9"))
        self.question_10.setText(_translate("MainWindow", "Câu 10: 6?"))
        self.A_10.setText(_translate("MainWindow", "A. bcd"))
        self.D_10.setText(_translate("MainWindow", "D. xyz"))
        self.B_10.setText(_translate("MainWindow", "B. aab"))
        self.C_10.setText(_translate("MainWindow", "C. dca"))
        self.finish.setText(_translate("MainWindow", "Kết Thúc Bài Thi"))
        self.id_question10.setText(_translate("MainWindow", "ID câu hỏi"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("MainWindow", "Câu 10"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
