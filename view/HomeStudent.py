# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeStudent.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1914, 940)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.student = QtWidgets.QTabWidget(self.centralwidget)
        self.student.setGeometry(QtCore.QRect(400, 120, 1141, 681))
        self.student.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.student.setObjectName("student")
        self.studentprofile = QtWidgets.QWidget()
        self.studentprofile.setObjectName("studentprofile")
        self.title = QtWidgets.QLabel(self.studentprofile)
        self.title.setGeometry(QtCore.QRect(470, 70, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.masv = QtWidgets.QLabel(self.studentprofile)
        self.masv.setGeometry(QtCore.QRect(200, 150, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.masv.setFont(font)
        self.masv.setObjectName("masv")
        self.hosv = QtWidgets.QLabel(self.studentprofile)
        self.hosv.setGeometry(QtCore.QRect(200, 200, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.hosv.setFont(font)
        self.hosv.setObjectName("hosv")
        self.tensv = QtWidgets.QLabel(self.studentprofile)
        self.tensv.setGeometry(QtCore.QRect(190, 250, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tensv.setFont(font)
        self.tensv.setObjectName("tensv")
        self.phai = QtWidgets.QLabel(self.studentprofile)
        self.phai.setGeometry(QtCore.QRect(200, 300, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.phai.setFont(font)
        self.phai.setObjectName("phai")
        self.ngaysinh = QtWidgets.QLabel(self.studentprofile)
        self.ngaysinh.setGeometry(QtCore.QRect(200, 350, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ngaysinh.setFont(font)
        self.ngaysinh.setObjectName("ngaysinh")
        self.noisinh = QtWidgets.QLabel(self.studentprofile)
        self.noisinh.setGeometry(QtCore.QRect(200, 400, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.noisinh.setFont(font)
        self.noisinh.setObjectName("noisinh")
        self.tenlop = QtWidgets.QLabel(self.studentprofile)
        self.tenlop.setGeometry(QtCore.QRect(200, 450, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tenlop.setFont(font)
        self.tenlop.setObjectName("tenlop")
        self.password = QtWidgets.QLabel(self.studentprofile)
        self.password.setGeometry(QtCore.QRect(220, 500, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.showmasv = QtWidgets.QTextBrowser(self.studentprofile)
        self.showmasv.setGeometry(QtCore.QRect(350, 150, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.showmasv.setFont(font)
        self.showmasv.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.showmasv.setObjectName("showmasv")
        self.showhosv = QtWidgets.QTextBrowser(self.studentprofile)
        self.showhosv.setGeometry(QtCore.QRect(350, 200, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.showhosv.setFont(font)
        self.showhosv.setObjectName("showhosv")
        self.showtensv = QtWidgets.QTextBrowser(self.studentprofile)
        self.showtensv.setGeometry(QtCore.QRect(350, 250, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.showtensv.setFont(font)
        self.showtensv.setObjectName("showtensv")
        self.showphai = QtWidgets.QTextBrowser(self.studentprofile)
        self.showphai.setGeometry(QtCore.QRect(350, 300, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.showphai.setFont(font)
        self.showphai.setObjectName("showphai")
        self.showngaysinh = QtWidgets.QTextBrowser(self.studentprofile)
        self.showngaysinh.setGeometry(QtCore.QRect(350, 350, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.showngaysinh.setFont(font)
        self.showngaysinh.setObjectName("showngaysinh")
        self.shownoisinh = QtWidgets.QTextBrowser(self.studentprofile)
        self.shownoisinh.setGeometry(QtCore.QRect(350, 400, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.shownoisinh.setFont(font)
        self.shownoisinh.setObjectName("shownoisinh")
        self.showtenlop = QtWidgets.QTextBrowser(self.studentprofile)
        self.showtenlop.setGeometry(QtCore.QRect(350, 450, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.showtenlop.setFont(font)
        self.showtenlop.setObjectName("showtenlop")
        self.showpassword = QtWidgets.QTextBrowser(self.studentprofile)
        self.showpassword.setGeometry(QtCore.QRect(350, 500, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.showpassword.setFont(font)
        self.showpassword.setObjectName("showpassword")
        self.student.addTab(self.studentprofile, "")
        self.taketest = QtWidgets.QWidget()
        self.taketest.setObjectName("taketest")
        self.title_2 = QtWidgets.QLabel(self.taketest)
        self.title_2.setGeometry(QtCore.QRect(440, 120, 311, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title_2.setFont(font)
        self.title_2.setObjectName("title_2")
        self.buttonvaothi = QtWidgets.QPushButton(self.taketest)
        self.buttonvaothi.setGeometry(QtCore.QRect(430, 350, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonvaothi.setFont(font)
        self.buttonvaothi.setObjectName("buttonvaothi")
        self.inputmamh = QtWidgets.QLineEdit(self.taketest)
        self.inputmamh.setGeometry(QtCore.QRect(320, 240, 521, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.inputmamh.setFont(font)
        self.inputmamh.setText("")
        self.inputmamh.setObjectName("inputmamh")
        self.student.addTab(self.taketest, "")
        self.UpdatePassword = QtWidgets.QWidget()
        self.UpdatePassword.setObjectName("UpdatePassword")
        self.QLineUPOldPassword = QtWidgets.QLineEdit(self.UpdatePassword)
        self.QLineUPOldPassword.setGeometry(QtCore.QRect(530, 160, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QLineUPOldPassword.setFont(font)
        self.QLineUPOldPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.QLineUPOldPassword.setObjectName("QLineUPOldPassword")
        self.QLineUPNewPassword = QtWidgets.QLineEdit(self.UpdatePassword)
        self.QLineUPNewPassword.setGeometry(QtCore.QRect(530, 220, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QLineUPNewPassword.setFont(font)
        self.QLineUPNewPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.QLineUPNewPassword.setObjectName("QLineUPNewPassword")
        self.QButtonUPUpdatePassword = QtWidgets.QPushButton(self.UpdatePassword)
        self.QButtonUPUpdatePassword.setGeometry(QtCore.QRect(570, 350, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QButtonUPUpdatePassword.setFont(font)
        self.QButtonUPUpdatePassword.setObjectName("QButtonUPUpdatePassword")
        self.QButtonUPClear = QtWidgets.QPushButton(self.UpdatePassword)
        self.QButtonUPClear.setGeometry(QtCore.QRect(710, 350, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QButtonUPClear.setFont(font)
        self.QButtonUPClear.setObjectName("QButtonUPClear")
        self.label = QtWidgets.QLabel(self.UpdatePassword)
        self.label.setGeometry(QtCore.QRect(350, 160, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.UpdatePassword)
        self.label_2.setGeometry(QtCore.QRect(340, 220, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.QLineUPNewPassword_2 = QtWidgets.QLineEdit(self.UpdatePassword)
        self.QLineUPNewPassword_2.setGeometry(QtCore.QRect(530, 280, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QLineUPNewPassword_2.setFont(font)
        self.QLineUPNewPassword_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.QLineUPNewPassword_2.setObjectName("QLineUPNewPassword_2")
        self.label_3 = QtWidgets.QLabel(self.UpdatePassword)
        self.label_3.setGeometry(QtCore.QRect(260, 280, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.student.addTab(self.UpdatePassword, "")
        self.backToLogin = QtWidgets.QPushButton(self.centralwidget)
        self.backToLogin.setGeometry(QtCore.QRect(1370, 830, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.backToLogin.setFont(font)
        self.backToLogin.setObjectName("backToLogin")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.student.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.student, self.showmasv)
        MainWindow.setTabOrder(self.showmasv, self.showhosv)
        MainWindow.setTabOrder(self.showhosv, self.showtensv)
        MainWindow.setTabOrder(self.showtensv, self.showphai)
        MainWindow.setTabOrder(self.showphai, self.showngaysinh)
        MainWindow.setTabOrder(self.showngaysinh, self.shownoisinh)
        MainWindow.setTabOrder(self.shownoisinh, self.showtenlop)
        MainWindow.setTabOrder(self.showtenlop, self.showpassword)
        MainWindow.setTabOrder(self.showpassword, self.buttonvaothi)
        MainWindow.setTabOrder(self.buttonvaothi, self.inputmamh)
        MainWindow.setTabOrder(self.inputmamh, self.QLineUPOldPassword)
        MainWindow.setTabOrder(self.QLineUPOldPassword, self.QLineUPNewPassword)
        MainWindow.setTabOrder(self.QLineUPNewPassword, self.QLineUPNewPassword_2)
        MainWindow.setTabOrder(self.QLineUPNewPassword_2, self.QButtonUPUpdatePassword)
        MainWindow.setTabOrder(self.QButtonUPUpdatePassword, self.QButtonUPClear)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Thông Tin Sinh Viên"))
        self.masv.setText(_translate("MainWindow", "Mã Sinh Viên:"))
        self.hosv.setText(_translate("MainWindow", "Họ Sinh Viên:"))
        self.tensv.setText(_translate("MainWindow", "Tên Sinh Viên:"))
        self.phai.setText(_translate("MainWindow", "Giới Tính:"))
        self.ngaysinh.setText(_translate("MainWindow", "Ngày Sinh:"))
        self.noisinh.setText(_translate("MainWindow", "Nơi Sinh:"))
        self.tenlop.setText(_translate("MainWindow", "Tên Lớp:"))
        self.password.setText(_translate("MainWindow", "Email:"))
        self.showmasv.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.showhosv.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.showtensv.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.showphai.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.showngaysinh.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.shownoisinh.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.showtenlop.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.showpassword.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.student.setTabText(self.student.indexOf(self.studentprofile), _translate("MainWindow", "Student\'s Profile"))
        self.title_2.setText(_translate("MainWindow", "Nhập Mã Môn Học"))
        self.buttonvaothi.setText(_translate("MainWindow", "Vào Thi"))
        self.student.setTabText(self.student.indexOf(self.taketest), _translate("MainWindow", "Take Test"))
        self.QButtonUPUpdatePassword.setText(_translate("MainWindow", "Update"))
        self.QButtonUPClear.setText(_translate("MainWindow", "Clear"))
        self.label.setText(_translate("MainWindow", "Old Password:"))
        self.label_2.setText(_translate("MainWindow", "New Password:"))
        self.label_3.setText(_translate("MainWindow", "Confirm New Password:"))
        self.student.setTabText(self.student.indexOf(self.UpdatePassword), _translate("MainWindow", "UpdatePassword"))
        self.backToLogin.setText(_translate("MainWindow", "BACK TO LOGIN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
