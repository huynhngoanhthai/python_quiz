import sys
from werkzeug.security import generate_password_hash, check_password_hash
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QLineEdit,  QTableWidgetItem
from PyQt5 import QtWidgets
import mysql.connector as sql
# import file code func
from messageBox import MBox
from database import myDB
from sendMail import sendMail
from radomPassword import get_random_string
# import file designer
import view.Login as Login
import view.SendEmail as HomeSendEmail
import view.HomeQuestion as HomeQuestion
import view.HomeTeacher as HomeTeacher
import view.HomeStudent as HomeStudent
import view.TakeTest as TakeTest
import view.Student as Student
import view.Subjects as Subjects


def showLogin():
    global ui
    ui = Login.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()

    ui.login.clicked.connect(loginUser)
    ui.password.returnPressed.connect(loginUser)
    ui.seePassword.clicked.connect(checkPassword)
    ui.QButtonForgotPassword.clicked.connect(showSendMail)


def loginUser():
    try:
        cur = myDB.cursor()
        getUname = ui.uname.text().strip()  # GT
        getPassword = ui.password.text()

        if(getUname[0:2] == "GT"):
            cur.execute(
                "SELECT * FROM dmgv WHERE MaGV=%s AND Password=%s", (getUname, getPassword))
            result = cur.fetchall()
            if(result == []):
                return MBox(0, 'ERROR', "uname or password wrong", 16)
            return showHomeTeacher(result)

        cur.execute("SELECT * FROM dmsv WHERE MaSV=%s", (getUname,))
        result = cur.fetchall()
        if not result:
            return MBox(0, 'ERROR', "uname or password wrong", 16)
        if not check_password_hash(result[0][1], getPassword):
            return MBox(0, 'ERROR', "uname or password wrong", 16)
        else:
            showHomeStudent(result)
    except sql.Error as e:
        MBox(0, "Error", str(e), 32)


def showSendMail():
    global ui
    ui = HomeSendEmail.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    try:
        cur = myDB.cursor()
        cur.execute("SELECT Email FROM dmsv ")
        result = cur.fetchall()
        ui.Email = []
        for row in result:
            ui.Email.append(row[0])
    except sql.Error as e:
        MBox(0, "Error", str(e), 16)
    # Send an Email
    ui.QButtonSend.clicked.connect(sendEmailForgotPassword)
    ui.QButtonClear.clicked.connect(clearContentsSendMail)
    ui.QLineEmail.returnPressed.connect(sendEmailForgotPassword)
    ui.QButtonBack.clicked.connect(showLogin)


def clearContentsSendMail():
    ui.QLineEmail.clear()


def sendEmailForgotPassword():
    try:
        cur = myDB.cursor()
        Email = ui.QLineEmail.text().strip()
        if not isCheckedEmpty(Email):
            return MBox(0, "Error", "Not empty", 16)
        if not Email in ui.Email:
            return MBox(0, "Error", "not find", 16)
        if not "@" in Email:
            return MBox(0, "Error", "not @", 16)
        passwordRandom = get_random_string(8)
        cur.execute("UPDATE dmsv SET Password=%s where email = %s",
                    (generate_password_hash(passwordRandom), Email))
        myDB.commit()
        sendMail(Email, "Forgot Password",
                 "Your Password is {}".format(passwordRandom))
        clearContentsSendMail()
        # sleep(2)
        showLogin()
    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


def checkPassword():
    if ui.seePassword.isChecked():
        ui.password.setEchoMode(QLineEdit.Normal)
    else:
        ui.password.setEchoMode(QLineEdit.Password)


def showHomeTeacher(info):
    global ui
    ui = HomeTeacher.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    # default name for GV
    ui.NAMEGV.setText(info[0][3])
    ui.QButtonCH.clicked.connect(showHomeQuestion)
    ui.QButtonSV.clicked.connect(showStudent)
    ui.QButtonMH.clicked.connect(showSubjects)
    ui.QButtonLogout.clicked.connect(showLogin)


def showSubjects():
    global ui
    ui = Subjects.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    # default
    ui.tab.setCurrentWidget(ui.Add)
    ui.QButtonBack.clicked.connect(showHomeTeacherHandler)
    # event clicked for button in add
    ui.QButtonAClear.clicked.connect(clearContentsAddSubjects)
    ui.QButtonAAdd.clicked.connect(addSubject)
    # event clicked for button in Update
    ui.QButtonUClear.clicked.connect(clearContentsUpdateSubjects)
    ui.QLineUMaMH.returnPressed.connect(suggestUpdateSubjects)
    ui.QButtonUUpdate.clicked.connect(updateSubject)
    # event clicked for button in DELETE
    ui.QButtonDClear.clicked.connect(clearContentsDeleteSubjects)
    ui.QLineDMaMH.returnPressed.connect(suggestDeleteSubjects)
    ui.QLineDTenMH.returnPressed.connect(suggestDeleteSubjects)
    ui.QButtonDDelete.clicked.connect(deleteSubject)


# Add subject


def clearContentsAddSubjects():
    ui.QLineAMaMH.clear()
    ui.QLineATenMH.clear()
    ui.QBoxASoTiet.setValue(0)


def addSubject():
    try:
        cur = myDB.cursor()
        MaMH = ui.QLineAMaMH.text().strip()
        TenMH = ui.QLineATenMH.text().strip()
        SoTiet = ui.QBoxASoTiet.text()
        if isCheckedEmpty(MaMH, TenMH, SoTiet) == False:
            return MBox(0, "Error", "Not empty", 32)

        query = "INSERT INTO dmmh (MaMH,TenMH,SoTiet) VALUES (%s,%s, %s) "
        cur.execute(query, (MaMH, TenMH, SoTiet))
        myDB.commit()
        MBox(0, "Successfully", "Successfully", 32)
        clearContentsAddSubjects()
    except sql.Error as e:
        MBox(0, "Error", str(e), 16)

# update


def clearContentsUpdateSubjects():
    ui.QLineUMaMH.clear()
    ui.QLineUTenMH.clear()
    ui.QBoxUSoTiet.setValue(0)
    ui.QLineUMaMH.setEnabled(True)


def suggestUpdateSubjects():
    try:
        cur = myDB.cursor()
        MaMH = ui.QLineUMaMH.text().strip()
        query = "SELECT * FROM dmmh WHERE MaMH LIKE '%{}%' ".format(
            MaMH)
        cur.execute(query)
        result = cur.fetchall()
        if len(result) == 0:
            return MBox(0, "Error", "not found", 16)
        if len(result) == 1 or result[0][0] == MaMH:
            ui.QLineUMaMH.setText(result[0][0])
            ui.QLineUTenMH.setText(result[0][1])
            ui.QBoxUSoTiet.setValue(result[0][2])
            ui.QLineUMaMH.setDisabled(True)

        ui.QTableUpdate.clearContents()
        ui.QTableUpdate.setColumnCount(3)
        ui.QTableUpdate.setRowCount(10)
        columns = 0
        for row in result:
            ui.QTableUpdate.setItem(columns, 0, QTableWidgetItem(row[0]))
            ui.QTableUpdate.setItem(columns, 1, QTableWidgetItem(row[1]))
            ui.QTableUpdate.setItem(columns, 2, QTableWidgetItem(str(row[2])))

            columns += 1
    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


def updateSubject():
    try:
        if ui.QLineUMaMH.isEnabled() == True:
            return MBox(0, "Error", "You need block ", 16)
        cur = myDB.cursor()
        MaMH = ui.QLineUMaMH.text().strip()
        TenMH = ui.QLineUTenMH.text().strip()
        SoTiet = ui.QBoxUSoTiet.text()
        if isCheckedEmpty(MaMH, TenMH, SoTiet) == False:
            return MBox(0, "Error", "not empty", 16)

        query = ""
        cur.execute(query, (TenMH, SoTiet, MaMH))
        myDB.commit()
        clearContentsUpdateSubjects()
        MBox(0, "Successfully", "Successfully", 32)
    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


# Delete
def clearContentsDeleteSubjects():
    ui.QLineDMaMH.clear()
    ui.QLineDTenMH.clear()

    ui.QLineDMaMH.setEnabled(True)
    ui.QLineDTenMH.setEnabled(True)
    ui.QTableDelete.clearContents()


def suggestDeleteSubjects():
    try:
        query = ""
        cur = myDB.cursor()
        MaMH = ui.QLineDMaMH.text().strip()
        TenMH = ui.QLineDTenMH.text().strip()
        if MaMH == "":
            query = "SELECT * FROM dmmh WHERE  TenMH LIKE '%{}%';".format(
                TenMH)
        elif TenMH == '':
            query = "SELECT * FROM dmmh WHERE MaMH LIKE '%{}%';".format(MaMH)
        else:
            query = "SELECT * FROM dmmh WHERE  TenMH LIKE '%{}%' AND MaMH LIKE '%{}%';".format(
                TenMH, MaMH)

        cur.execute(query)
        result = cur.fetchall()
        if len(result) == 0:
            return MBox(0, "Error", "not found", 16)
        if len(result) == 1 or result[0][0] == MaMH:
            ui.QLineDMaMH.setText(result[0][0])
            ui.QLineDTenMH.setText(result[0][1])
            ui.QLineDMaMH.setDisabled(True)
            ui.QLineDTenMH.setDisabled(True)
        ui.QTableDelete.clearContents()
        ui.QTableDelete.setColumnCount(3)
        ui.QTableDelete.setRowCount(10)
        columns = 0
        for row in result:
            ui.QTableDelete.setItem(columns, 0, QTableWidgetItem(row[0]))
            ui.QTableDelete.setItem(columns, 1, QTableWidgetItem(row[1]))
            ui.QTableDelete.setItem(columns, 2, QTableWidgetItem(str(row[2])))
            columns += 1

    except sql.Error as e:
        MBox(0, "Error", str(e), 16)

    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


def deleteSubject():
    try:
        if ui.QLineDMaMH.isEnabled() or ui.QLineDTenMH.isEnabled():
            return MBox(0, "Error", "you need block", 16)
        cur = myDB.cursor()
        MaMH = ui.QLineDMaMH.text().strip()
        TenMH = ui.QLineDTenMH.text().strip()

        query = "DELETE FROM dmmh WHERE MaMH = %s AND TenMH = %s"
        cur.execute(query, (MaMH, TenMH))
        myDB.commit()
        clearContentsDeleteSubjects()
        MBox(0, "Successfully", "Successfully", 32)
    except sql.Error as e:
        MBox(0, "Error", str(e), 16)

# show Student


def showHomeTeacherHandler():
    return showHomeTeacher([('', '', '', 'GIAO VIEN')])


def showStudent():
    global ui
    ui = Student.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    # default
    ui.QButtonBack.clicked.connect(showHomeTeacherHandler)

    # event clicked for button in add
    ui.tab.setCurrentWidget(ui.Add)
    ui.QButtonAClear.clicked.connect(clearContentsAddStudent)
    ui.QButtonAAddStudent.clicked.connect(addStudent)
    ui.QLineALop.returnPressed.connect(addStudent)
    # event clicked for button in update
    ui.QLineUMaSV.returnPressed.connect(suggestUpdateStudent)
    ui.QButtonUClear.clicked.connect(clearContentsUpdateStudent)
    ui.QButtonUUpdate.clicked.connect(updateStudent)
    # event clicked for button in DELETE
    ui.QButtonDClear.clicked.connect(clearContentsDeleteStudent)
    ui.QLineDMaSV.returnPressed.connect(suggestDeleteStudent)
    ui.QLineDTenSV.returnPressed.connect(suggestDeleteStudent)

    ui.QButtonDDelete.clicked.connect(deleteStudent)
    # event clicked for button in Show All

    ui.QButtonSAClear.clicked.connect(clearContentsShowAllStudent)
    ui.QButtonShowAll.clicked.connect(showAllStudent)
    ui.QLineSATenLop.returnPressed.connect(showAllStudent)
    # event clicked for button in Show diem
    ui.QButtonSDClear.clicked.connect(clearContentsShowDiemStudent)
    ui.QButtonSDSearch.clicked.connect(showDiemStudent)
    ui.QLineSDMaMH.returnPressed.connect(showDiemStudent)

# add student


def clearContentsAddStudent():
    ui.QLineAMaSV.clear()
    ui.QLineAHoSV.clear()
    ui.QDateANS.setDate(date_changed("04/11/2001"))
    ui.QLineATenSV.clear()
    ui.QLineADC.clear()
    ui.QLineALop.clear()
    ui.QLineAEmail.clear()


def addStudent():
    try:
        MaSV = ui.QLineAMaSV.text()

        HoSV = ui.QLineAHoSV.text()

        TenSV = ui.QLineATenSV.text()

        Phai = ''
        if ui.OpNAM.isChecked():
            Phai = "NAM"
        elif ui.OpNU.isChecked():
            Phai = "NU"
        else:
            return MBox(0, "Error", "you need choose Phai", 16)

        NgaySinh = ui.QDateANS.text()
        NoiSinh = ui.QLineADC.text()

        Lop = ui.QLineALop.text()
        Email = ui.QLineAEmail.text().strip()
        if not "@" in Email:
            return MBox(0, "Error", "not @", 16)
        checked = isCheckedEmpty(
            MaSV, HoSV, TenSV, NgaySinh, NoiSinh, Lop, Email)
        if not checked:
            return MBox(0, "Error", "not empty", 16)
        password = generate_password_hash(MaSV)

        cur = myDB.cursor()
        cur.execute(
            "INSERT INTO dmsv (MaSV,Password,HoSV,TenSV,Phai,NgaySinh,NoiSinh,TenLop,Email) VALUES (%s,%s, %s,%s,%s, %s,%s,%s,%s) ",
            (MaSV, password, HoSV, TenSV, Phai, NgaySinh, NoiSinh, Lop, Email))
        myDB.commit()
        MBox(0, "Successfully", "Successfully", 32)
        clearContentsAddStudent()
    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


# update student
def clearContentsUpdateStudent():
    ui.QLineUMaSV.clear()
    ui.QLineUHoSV.clear()
    ui.QLineUTenSV.clear()
    ui.OpUPhai.setCurrentIndex(0)
    ui.QDateUNgaySinh.setDate(date_changed("04/11/2001"))
    ui.QLineUNoiSinh.clear()
    ui.QLineULop.clear()
    ui.QLineUEmail.clear()

    ui.QLineUMaSV.setDisabled(False)
    ui.QTableUpdate.clearContents()


def date_changed(day):
    newDay = day.split('/')
    return QDate(int(newDay[2]), int(newDay[1]), int(newDay[0]))


def suggestUpdateStudent():
    try:
        cur = myDB.cursor()
        MaSV = ui.QLineUMaSV.text().strip()
        query = "SELECT * FROM dmsv WHERE MaSV LIKE '%{}%' LIMIT 10;".format(
            MaSV)
        cur.execute(query)
        result = cur.fetchall()
        if len(result) == 0:
            return MBox(0, "Error", "not found", 16)
        if len(result) == 1 or result[0][0] == MaSV:
            ui.QLineUMaSV.setText(result[0][0])
            ui.QLineUHoSV.setText(result[0][2])
            ui.QLineUTenSV.setText(result[0][3])
            if result[0][4] == 'NAM':
                ui.OpUPhai.setCurrentIndex(0)
            else:
                ui.OpUPhai.setCurrentIndex(1)
            ui.QDateUNgaySinh.setDate(date_changed(result[0][5]))
            ui.QLineUNoiSinh.setText(result[0][6])
            ui.QLineULop.setText(result[0][7])
            ui.QLineUEmail.setText(result[0][8])
            ui.QLineUMaSV.setDisabled(True)

        ui.QTableUpdate.clearContents()
        ui.QTableUpdate.setColumnCount(8)
        ui.QTableUpdate.setRowCount(10)
        columns = 0
        for row in result:
            ui.QTableUpdate.setItem(columns, 0, QTableWidgetItem(row[0]))
            ui.QTableUpdate.setItem(columns, 1, QTableWidgetItem(row[2]))
            ui.QTableUpdate.setItem(columns, 2, QTableWidgetItem(row[3]))
            ui.QTableUpdate.setItem(columns, 3, QTableWidgetItem(row[4]))
            ui.QTableUpdate.setItem(columns, 4, QTableWidgetItem(row[5]))
            ui.QTableUpdate.setItem(columns, 5, QTableWidgetItem(row[6]))
            ui.QTableUpdate.setItem(columns, 6, QTableWidgetItem(row[7]))
            ui.QTableUpdate.setItem(columns, 7, QTableWidgetItem(row[8]))
            columns += 1
    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


def isCheckedEmpty(*argv):
    #  argv is a tuple
    for item in argv:
        if item == '' or item == '0':
            return False
    return True


def updateStudent():
    try:
        cur = myDB.cursor()
        MaSV = ui.QLineUMaSV.text().strip()
        HoSV = ui.QLineUHoSV.text().strip()
        TenSV = ui.QLineUTenSV.text().strip()
        Phai = ui.OpUPhai.currentText()
        NgaySinh = ui.QDateUNgaySinh.text().strip()
        NoiSinh = ui.QLineUNoiSinh.text().strip()
        TenLop = ui.QLineULop.text().strip()
        Email = ui.QLineUEmail.text().strip()
        if not "@" in Email:
            return MBox(0, "Error", "not @", 16)
        checked = isCheckedEmpty(
            MaSV, HoSV, TenSV, Phai, NgaySinh, NoiSinh, TenLop, Email)
        if not checked:
            return MBox(0, "Error", "not empty", 16)

        query = "UPDATE dmsv SET HoSV=%s,TenSV=%s,Phai=%s,NgaySinh=%s,NoiSinh=%s,TenLop=%s,Email=%s WHERE MaSV=%s"

        cur.execute(query, (HoSV, TenSV, Phai,
                    NgaySinh, NoiSinh, TenLop, Email, MaSV))
        myDB.commit()
        clearContentsUpdateStudent()
        MBox(0, "Successfully", "Successfully", 32)

    except sql.Error as e:
        MBox(0, "Error", str(e), 16)

# delete


def clearContentsDeleteStudent():
    ui.QLineDMaSV.clear()
    ui.QLineDTenSV.clear()

    ui.QTableDelete.clearContents()
    ui.QLineDMaSV.setEnabled(True)
    ui.QLineDTenSV.setEnabled(True)


def suggestDeleteStudent():
    try:
        query = ""
        cur = myDB.cursor()
        MaSV = ui.QLineDMaSV.text().strip()
        TenSV = ui.QLineDTenSV.text().strip()
        if MaSV == '':
            query = "SELECT * FROM dmsv WHERE TenSV LIKE '%{}%' LIMIT 10".format(
                TenSV)
        if TenSV == '':
            query = "SELECT * FROM dmsv WHERE MaSV LIKE '%{}%' LIMIT 10".format(
                MaSV)
        else:
            query = "SELECT * FROM dmsv WHERE MaSV LIKE '%{}%' AND TenSV LIKE '%{}%' LIMIT 10".format(
                MaSV, TenSV)
        cur.execute(query)
        result = cur.fetchall()
        if len(result) == 0:
            return MBox(0, "Error", "not found", 16)
        if len(result) == 1 or result[0][0] == MaSV:
            ui.QLineDMaSV.setText(result[0][0])
            ui.QLineDTenSV.setText(result[0][3])
            ui.QLineDMaSV.setDisabled(True)
            ui.QLineDTenSV.setDisabled(True)
        ui.QTableDelete.clearContents()
        ui.QTableDelete.setColumnCount(8)
        ui.QTableDelete.setRowCount(10)
        columns = 0
        for row in result:
            ui.QTableDelete.setItem(columns, 0, QTableWidgetItem(row[0]))
            ui.QTableDelete.setItem(columns, 1, QTableWidgetItem(row[2]))
            ui.QTableDelete.setItem(columns, 2, QTableWidgetItem(row[3]))
            ui.QTableDelete.setItem(columns, 3, QTableWidgetItem(row[4]))
            ui.QTableDelete.setItem(columns, 4, QTableWidgetItem(row[5]))
            ui.QTableDelete.setItem(columns, 5, QTableWidgetItem(row[6]))
            ui.QTableDelete.setItem(columns, 6, QTableWidgetItem(row[7]))
            ui.QTableDelete.setItem(columns, 7, QTableWidgetItem(row[8]))

            columns += 1

    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


def deleteStudent():
    try:
        if ui.QLineDMaSV.isEnabled() and ui.QLineDMaSV.isEnabled():
            return MBox(0, "Error", "You need block ", 16)
        cur = myDB.cursor()
        MaSV = ui.QLineDMaSV.text().strip()
        TenSV = ui.QLineDTenSV.text().strip()
        cur.execute(
            "DELETE FROM dmsv WHERE MaSV = %s AND TenSV = %s", (MaSV, TenSV))
        myDB.commit()
        MBox(0, "Successfully", "Successfully", 32)
        clearContentsDeleteStudent()

    except sql.Error as e:
        MBox(0, "Error", str(e), 16)

# Show All


def clearContentsShowAllStudent():
    ui.QLineSATenLop.clear()
    ui.QTableDelete.clearContents()


def showAllStudent():
    try:
        cur = myDB.cursor()
        TenLop = ui.QLineSATenLop.text().strip()
        query = "SELECT * FROM dmsv WHERE TenLop LIKE '%{}%'".format(TenLop)
        cur.execute(query)
        result = cur.fetchall()
        ui.QTableShowAll.clearContents()
        ui.QTableShowAll.setColumnCount(8)
        ui.QTableShowAll.setRowCount(len(result))
        columns = 0
        for row in result:
            ui.QTableShowAll.setItem(columns, 0, QTableWidgetItem(row[0]))
            ui.QTableShowAll.setItem(columns, 1, QTableWidgetItem(row[2]))
            ui.QTableShowAll.setItem(columns, 2, QTableWidgetItem(row[3]))
            ui.QTableShowAll.setItem(columns, 3, QTableWidgetItem(row[4]))
            ui.QTableShowAll.setItem(columns, 4, QTableWidgetItem(row[5]))
            ui.QTableShowAll.setItem(columns, 5, QTableWidgetItem(row[6]))
            ui.QTableShowAll.setItem(columns, 6, QTableWidgetItem(row[7]))
            ui.QTableShowAll.setItem(columns, 7, QTableWidgetItem(row[8]))
            columns += 1

    except sql.Error as e:
        MBox(0, "Error", str(e), 16)

# show diem


def clearContentsShowDiemStudent():
    ui.QTableShowDiem.clearContents()
    ui.QLineSDMaMH.clear()


def showDiemStudent():
    try:
        cur = myDB.cursor()
        MaMH = ui.QLineSDMaMH.text().strip()
        query = "SELECT dmmh.MaMH,dmsv.MaSV,HoSV,TenSV,TenMH,Diem FROM dmkq INNER JOIN dmsv on dmsv.MaSV = dmkq.MaSV INNER JOIN dmmh on  dmkq.MaMH =dmmh.MaMH WHERE  dmkq.MaMH LIKE '%{}%';".format(
            MaMH)
        cur.execute(query)
        result = cur.fetchall()
        ui.QTableShowDiem.clearContents()
        ui.QTableShowDiem.setColumnCount(6)
        ui.QTableShowDiem.setRowCount(len(result))
        columns = 0
        for row in result:
            ui.QTableShowDiem.setItem(columns, 0, QTableWidgetItem(row[0]))
            ui.QTableShowDiem.setItem(columns, 1, QTableWidgetItem(row[1]))
            ui.QTableShowDiem.setItem(columns, 2, QTableWidgetItem(row[2]))
            ui.QTableShowDiem.setItem(columns, 3, QTableWidgetItem(row[3]))
            ui.QTableShowDiem.setItem(columns, 4, QTableWidgetItem(row[4]))
            ui.QTableShowDiem.setItem(
                columns, 5, QTableWidgetItem(str(row[5])))
            columns += 1

    except sql.Error as e:
        MBox(0, "Error", str(e), 16)

# HomeQuestion


def showHomeQuestion():
    global ui
    ui = HomeQuestion.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    # default here add
    ui.tab.setCurrentWidget(ui.Add)
    ui.ButtonBacked.clicked.connect(showHomeTeacherHandler)
    # default ID is
    cur = myDB.cursor()
    try:
        cur.execute("SELECT max(MaCH) FROM dmch")
        result = cur.fetchall()[0][0]+1
    except:
        result = 1
    ui.IDAddQuestion.setText(str(result))
    try:
        cur.execute("SELECT MaMH,TenMH FROM dmmh")
        result = cur.fetchall()
        temp = []
        for item in result:
            ui.QComboxAMaMH.addItem(item[0] + "-" + item[1])
            ui.QComboxUMaMH.addItem(item[0] + "-" + item[1])
            temp.append(item[0])
        ui.MaMH = temp
    except sql.Error as e:
        return MBox(0, "Error", str(e), 32)
    # event clicked for button in add
    ui.AddQuestion.clicked.connect(addQuestion)
    ui.ClearQuestion.clicked.connect(clearContentsAddQuestion)
    # event clicked for button in Update
    ui.ClearUpdate.clicked.connect(clearContentsUpdateQuestion)
    ui.QLineUIDCauHoi.returnPressed.connect(suggestUpdateQuestion)
    ui.UpdateQuestion.clicked.connect(updateQuestion)
    # event clicked for button in Delete
    ui.ClearDelete.clicked.connect(clearContentsDeleteQuestion)
    ui.QLineDIDCauHoi.returnPressed.connect(suggestDeleteQuestion)
    ui.QLineDCauHoi.returnPressed.connect(suggestDeleteQuestion)
    ui.DeleteQuestion.clicked.connect(deleteQuestion)
    # event clicked for button in Show All list student
    ui.ButtonSAClear.clicked.connect(clearContentsShowAllQuestion)
    ui.QLineSAMaCH.returnPressed.connect(suggestShowAllQuestion)
    ui.QLineSACauHoi.returnPressed.connect(suggestShowAllQuestion)

# Add


def answerFilter(option):
    if option == 'A':
        return ui.QLineAOPA.text().strip()
    if option == 'B':
        return ui.QLineAOPB.text().strip()
    if option == 'C':
        return ui.QLineAOPC.text().strip()
    else:
        return ui.QLineAOPD.text().strip()


def addQuestion():
    try:
        cur = myDB.cursor()
        IDQuestion = ui.IDAddQuestion.text().strip()
        Question = ui.QLineAQuestion.text().strip()

        OPA = ui.QLineAOPA.text().strip()

        OPB = ui.QLineAOPB.text().strip()

        OPC = ui.QLineAOPC.text().strip()

        OPD = ui.QLineAOPD.text().strip()

        tempAnswer = ui.QComboBoxAAnswer.currentText()

        Answer = answerFilter(tempAnswer)

        MaMH = ui.QComboxAMaMH.currentText().split("-")
        checked = isCheckedEmpty(IDQuestion, Question,
                                 OPA, OPB, OPC, OPD, Answer, MaMH[0])
        if not checked:
            return MBox(0, "Error", "not empty", 16)

        query = "INSERT INTO dmch (MaCH, CauHoi, CauA,CauB,CauC,CauD,DapAn,MaMH) VALUES (%s, %s,%s,%s, %s,%s,%s, %s)"
        cur.execute(query, (IDQuestion, Question,
                    OPA, OPB, OPC, OPD, Answer, MaMH[0]))
        MBox(0, "Successfully", "Successfully", 32)
        myDB.commit()
        showHomeQuestion()
    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


def clearContentsAddQuestion():
    ui.QLineAQuestion.clear()
    ui.QLineAOPA.clear()
    ui.QLineAOPB.clear()
    ui.QLineAOPC.clear()
    ui.QLineAOPD.clear()
    ui.QLineAMaMH.clear()
    ui.QComBoxAAnswer.setCurrentIndex(0)

# Update


def clearContentsUpdateQuestion():
    ui.QLineUIDCauHoi.clear()
    ui.QLineUQuestion.clear()
    ui.QLineUOPA.clear()
    ui.QLineUOPB.clear()
    ui.QLineUOPC.clear()
    ui.QLineUOPD.clear()
    ui.QLineUIDCauHoi.setDisabled(False)
    ui.QTableUpdate.clearContents()


def printAnswerFiltered(answer):
    if answer == ui.QLineUOPA.text():
        return 0
    if answer == ui.QLineUOPB.text():
        return 1
    if answer == ui.QLineUOPC.text():
        return 2
    else:
        return 3


def suggestUpdateQuestion():
    try:
        cur = myDB.cursor()
        IDQuestion = ui.QLineUIDCauHoi.text().strip()
        query = "SELECT * FROM dmch WHERE MaCH LIKE '%{}%' LIMIT 10;".format(
            IDQuestion)
        cur.execute(query)
        result = cur.fetchall()
        if len(result) == 0:
            return MBox(0, "Error", "not found", 16)
        if len(result) == 1 or str(result[0][0]) == IDQuestion:
            ui.QLineUIDCauHoi.setText(str(result[0][0]))
            ui.QLineUQuestion.setText(result[0][1])
            ui.QLineUOPA.setText(result[0][2])
            ui.QLineUOPB.setText(result[0][3])
            ui.QLineUOPC.setText(result[0][4])
            ui.QLineUOPD.setText(result[0][5])
            ui.QComboxUAnswer.setCurrentIndex(
                printAnswerFiltered(result[0][6]))
            ui.QComboxUMaMH.setCurrentIndex(ui.MaMH.index(result[0][7]))
            ui.QLineUIDCauHoi.setDisabled(True)
        ui.QTableUpdate.clearContents()
        ui.QTableUpdate.setColumnCount(8)
        ui.QTableUpdate.setRowCount(10)
        columns = 0
        for row in result:
            ui.QTableUpdate.setItem(columns, 0, QTableWidgetItem(str(row[0])))
            ui.QTableUpdate.setItem(columns, 1, QTableWidgetItem(row[1]))
            ui.QTableUpdate.setItem(columns, 2, QTableWidgetItem(row[2]))
            ui.QTableUpdate.setItem(columns, 3, QTableWidgetItem(row[3]))
            ui.QTableUpdate.setItem(columns, 4, QTableWidgetItem(row[4]))
            ui.QTableUpdate.setItem(columns, 5, QTableWidgetItem(row[5]))
            ui.QTableUpdate.setItem(columns, 6, QTableWidgetItem(row[6]))
            ui.QTableUpdate.setItem(columns, 7, QTableWidgetItem(row[7]))
            columns += 1

    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


def answerFilterForUpdate(option):
    if option == 'A':
        return ui.QLineUOPA.text().strip()
    if option == 'B':
        return ui.QLineUOPB.text().strip()
    if option == 'C':
        return ui.QLineUOPC.text().strip()
    else:
        return ui.QLineUOPD.text().strip()


def updateQuestion():
    try:
        cur = myDB.cursor()
        IDQuestion = ui.QLineUIDCauHoi.text().strip()
        if ui.QLineUIDCauHoi.isEnabled():
            return MBox(0, "Error", "you need block", 16)
        Question = ui.QLineUQuestion.text().strip()

        OPA = ui.QLineUOPA.text().strip()

        OPB = ui.QLineUOPB.text().strip()

        OPC = ui.QLineUOPC.text().strip()

        OPD = ui.QLineUOPD.text().strip()

        tempAnswer = ui.QComboxUAnswer.currentText()

        Answer = answerFilterForUpdate(tempAnswer)

        MaMH = ui.QComboxUMaMH.currentText().split("-")[0]

        checked = isCheckedEmpty(IDQuestion, Question,
                                 OPA, OPB, OPC, OPD, Answer, MaMH)
        if not checked:
            return MBox(0, "Error", "not empty", 16)

        query = "UPDATE dmch SET CauHoi=%s,CauA=%s,CauB=%s,CauC=%s,CauD=%s,DapAn=%s,MaMH=%s WHERE MaCH=%s"
        cur.execute(query, (Question,
                    OPA, OPB, OPC, OPD, Answer, MaMH, IDQuestion))
        MBox(0, "Successfully", "Successfully", 32)
        myDB.commit()
        clearContentsUpdateQuestion()

    except sql.Error as e:
        MBox(0, "Error", str(e), 16)

# delete


def clearContentsDeleteQuestion():
    ui.QLineDCauHoi.clear()
    ui.QLineDIDCauHoi.clear()
    ui.QLineDCauHoi.setDisabled(False)
    ui.QLineDIDCauHoi.setDisabled(False)
    ui.QTableDelete.clearContents()


def suggestDeleteQuestion():
    try:
        cur = myDB.cursor()
        IDQuestion = ui.QLineDIDCauHoi.text().strip()
        CauHoi = ui.QLineDCauHoi.text().strip()
        query = "SELECT * FROM dmch WHERE MaCH LIKE '%{0}%' AND CauHoi LIKE '%{1}%' LIMIT 15;".format(
                IDQuestion, CauHoi)
        cur.execute(query)
        result = cur.fetchall()
        if len(result) == 0:
            return MBox(0, "Error", "not found", 16)
        if len(result) == 1 or str(result[0][0]) == IDQuestion:
            ui.QLineDIDCauHoi.setText(str(result[0][0]))
            ui.QLineDCauHoi.setText(result[0][1])
            ui.QLineDIDCauHoi.setDisabled(True)
            ui.QLineDCauHoi.setDisabled(True)
        ui.QTableDelete.clearContents()
        ui.QTableDelete.setColumnCount(8)
        ui.QTableDelete.setRowCount(15)
        columns = 0
        for row in result:
            ui.QTableDelete.setItem(columns, 0, QTableWidgetItem(str(row[0])))
            ui.QTableDelete.setItem(columns, 1, QTableWidgetItem(row[1]))
            ui.QTableDelete.setItem(columns, 2, QTableWidgetItem(row[2]))
            ui.QTableDelete.setItem(columns, 3, QTableWidgetItem(row[3]))
            ui.QTableDelete.setItem(columns, 4, QTableWidgetItem(row[4]))
            ui.QTableDelete.setItem(columns, 5, QTableWidgetItem(row[5]))
            ui.QTableDelete.setItem(columns, 6, QTableWidgetItem(row[6]))
            ui.QTableDelete.setItem(columns, 7, QTableWidgetItem(row[7]))
            columns += 1

    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


def deleteQuestion():
    try:
        cur = myDB.cursor()
        IDQuestion = ui.QLineDIDCauHoi.text().strip()
        CauHoi = ui.QLineDCauHoi.text().strip()
        if ui.QLineDIDCauHoi.isEnabled() == True or ui.QLineDIDCauHoi.isEnabled() == True:
            return MBox(0, "Error", "You need block ", 16)

        cur.execute(
            "DELETE FROM dmch WHERE MaCH = %s AND CauHoi = %s", (IDQuestion, CauHoi))
        myDB.commit()
        MBox(0, "Successfully", "Successfully", 32)
        clearContentsDeleteQuestion()
    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


# ShowAll
def clearContentsShowAllQuestion():
    ui.QLineSACauHoi.clear()
    ui.QLineSAMaCH.clear()
    ui.QTableShowAll.clearContents()


def suggestShowAllQuestion():
    try:
        cur = myDB.cursor()
        MaCH = ui.QLineSAMaCH.text().strip()
        CauHoi = ui.QLineSACauHoi.text().strip()
        query = ""
        if MaCH == '':
            query = "SELECT * FROM dmch WHERE CauHoi LIKE '%{}%'".format(
                CauHoi)
        if CauHoi == '':
            query = "SELECT * FROM dmch WHERE MaCH LIKE '%{}%'".format(
                MaCH)
        else:
            query = "SELECT * FROM dmch WHERE MaCH LIKE '%{}%' AND CauHoi LIKE '%{}%'".format(
                MaCH, CauHoi)

        cur.execute(query)
        result = cur.fetchall()
        columns = 0
        ui.QTableShowAll.clearContents()
        ui.QTableShowAll.setColumnCount(8)
        ui.QTableShowAll.setRowCount(len(result))
        for row in result:
            ui.QTableShowAll.setItem(columns, 0, QTableWidgetItem(str(row[0])))
            ui.QTableShowAll.setItem(columns, 1, QTableWidgetItem(row[1]))
            ui.QTableShowAll.setItem(columns, 2, QTableWidgetItem(row[2]))
            ui.QTableShowAll.setItem(columns, 3, QTableWidgetItem(row[3]))
            ui.QTableShowAll.setItem(columns, 4, QTableWidgetItem(row[4]))
            ui.QTableShowAll.setItem(columns, 5, QTableWidgetItem(row[5]))
            ui.QTableShowAll.setItem(columns, 6, QTableWidgetItem(row[6]))
            ui.QTableShowAll.setItem(columns, 7, QTableWidgetItem(row[7]))
            columns += 1

    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


# -------------------------Student------------------------


def showHomeStudent(info):
    global ui
    # info1 ĐỂ GIỮ LẠI DỮ LIỆU XỬ LÍ DƯỚI CÁC HÀM DƯỚI
    global infoStudent
    infoStudent = info
    ui = HomeStudent.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    # default tab1
    ui.student.setCurrentWidget(ui.studentprofile)
    # info Student Login
    ui.showmasv.setText(infoStudent[0][0])
    ui.showhosv.setText(infoStudent[0][2])
    ui.showtensv.setText(infoStudent[0][3])
    ui.showphai.setText(infoStudent[0][4])
    ui.showngaysinh.setText(infoStudent[0][5])
    ui.shownoisinh.setText(infoStudent[0][6])
    ui.showtenlop.setText(infoStudent[0][7])
    ui.showpassword.setText(infoStudent[0][8])
    # event clicked for button in THI
    ui.inputmamh.returnPressed.connect(callBackShowTakeTest)
    ui.buttonvaothi.clicked.connect(callBackShowTakeTest)
    # Back TO LOGIN_USER
    ui.backToLogin.clicked.connect(showLogin)

    # event clicked for button in updatePassword
    ui.QButtonUPClear.clicked.connect(clearContentsUpdatePassword)
    ui.QButtonUPUpdatePassword.clicked.connect(updatePassword)
    ui.QLineUPNewPassword_2.returnPressed.connect(updatePassword)


def clearContentsUpdatePassword():
    ui.QLineUPOldPassword.clear()
    ui.QLineUPNewPassword.clear()
    ui.QLineUPNewPassword_2.clear()


def updatePassword():
    try:
        cur = myDB.cursor()
        olbPassword = ui.QLineUPOldPassword.text()
        if not check_password_hash(infoStudent[0][1], olbPassword):
            return MBox(0, "Error", "password wrong", 16)
        newPassword = ui.QLineUPNewPassword.text()
        newPassword_2 = ui.QLineUPNewPassword_2.text()
        checked = isCheckedEmpty(olbPassword, newPassword, newPassword_2)
        if not checked:
            return MBox(0, "Error", "not empty", 16)
        if newPassword != newPassword_2:
            return MBox(0, "Error", "password wrong", 16)
        cur.execute("UPDATE dmsv SET Password=%s WHERE MaSV=%s",
                    (generate_password_hash(newPassword), infoStudent[0][0]))
        clearContentsUpdatePassword()
        myDB.commit()
        MBox(0, "Suggestfully", "Suggestfully update password", 32)
    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


def checkStudentExamined(MaSV, MaMH):
    try:
        cur = myDB.cursor()
        cur.execute(
            "SELECT MaSV,MaMH FROM dmkq WHERE MaSV = %s AND MaMH = %s", (MaSV, MaMH))
        result = cur.fetchall()
        if not result:
            return True
        else:
            return False
    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


def callBackShowTakeTest():
    MaMH = ui.inputmamh.text()
    if not isCheckedEmpty(MaMH):
        return MBox(0, "Error", "Not empty", 32)
    cur = myDB.cursor()
    query = "SELECT * FROM dmch WHERE MaMH = %s "
    cur.execute(query, (MaMH,))
    result = cur.fetchall()
    if len(result) < 10:
        return MBox(0, "Error", "Không đủ số lượng câu hỏi hoặc không tồn tại mã môn", 16)
    if not checkStudentExamined(infoStudent[0][0], MaMH):
        return MBox(0, "Error", "Sinh Viên Đã thi môn này rồi", 16)
    showTakeTest(MaMH, result)


def showTakeTest(MaMH, result):
    global ui
    ui = TakeTest.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.tabWidget.setCurrentWidget(ui.tab)
    ui.result = result
    ui.DSDapAnDB = []
    for item in result:
        ui.DSDapAnDB.append(item[6])
    ui.DSDapAnSV = []
    # ID_cau hoi
    ui.id_question.setText(str(result[0][0]))
    ui.id_question2.setText(str(result[1][0]))
    ui.id_question3.setText(str(result[2][0]))
    ui.id_question4.setText(str(result[3][0]))
    ui.id_question5.setText(str(result[4][0]))
    ui.id_question6.setText(str(result[5][0]))
    ui.id_question7.setText(str(result[6][0]))
    ui.id_question8.setText(str(result[7][0]))
    ui.id_question9.setText(str(result[8][0]))
    ui.id_question10.setText(str(result[9][0]))

    # cau hoi
    ui.question.setText(result[0][1])
    ui.question_2.setText(result[1][1])
    ui.question_3.setText(result[2][1])
    ui.question_4.setText(result[3][1])
    ui.question_5.setText(result[4][1])
    ui.question_6.setText(result[5][1])
    ui.question_7.setText(result[6][1])
    ui.question_8.setText(result[7][1])
    ui.question_9.setText(result[8][1])
    ui.question_10.setText(result[9][1])

    # cau tra loi
    A = "A. "
    B = "B. "
    C = "C. "
    D = "D. "
    ui.A.setText(A + result[0][2])
    ui.B.setText(B + result[0][3])
    ui.C.setText(C + result[0][4])
    ui.D.setText(D + result[0][5])
    # 2
    ui.A_2.setText(A + result[1][2])
    ui.B_2.setText(B + result[1][3])
    ui.C_2.setText(C + result[1][4])
    ui.D_2.setText(D + result[1][5])

    ui.A_3.setText(A + result[2][2])
    ui.B_3.setText(B + result[2][3])
    ui.C_3.setText(C + result[2][4])
    ui.D_3.setText(D + result[2][5])

    ui.A_4.setText(A + result[3][2])
    ui.B_4.setText(B + result[3][3])
    ui.C_4.setText(C + result[3][4])
    ui.D_4.setText(D + result[3][5])

    ui.A_5.setText(A + result[4][2])
    ui.B_5.setText(B + result[4][3])
    ui.C_5.setText(C + result[4][4])
    ui.D_5.setText(D + result[4][5])

    ui.A_6.setText(A + result[5][2])
    ui.B_6.setText(B + result[5][3])
    ui.C_6.setText(C + result[5][4])
    ui.D_6.setText(D + result[5][5])

    ui.A_7.setText(A + result[6][2])
    ui.B_7.setText(B + result[6][3])
    ui.C_7.setText(C + result[6][4])
    ui.D_7.setText(D + result[6][5])

    ui.A_8.setText(A + result[7][2])
    ui.B_8.setText(B + result[7][3])
    ui.C_8.setText(C + result[7][4])
    ui.D_8.setText(D + result[7][5])

    ui.A_9.setText(A + result[8][2])
    ui.B_9.setText(B + result[8][3])
    ui.C_9.setText(C + result[8][4])
    ui.D_9.setText(D + result[8][5])

    ui.A_10.setText(A + result[9][2])
    ui.B_10.setText(B + result[9][3])
    ui.C_10.setText(C + result[9][4])
    ui.D_10.setText(D + result[9][5])

    # CÁC NÚT ĐÁP ÁN CỦA CÁC CÂU HỎI
    # CÂU 1
    ui.A.toggled.connect(onClicked)
    ui.B.toggled.connect(onClicked)
    ui.C.toggled.connect(onClicked)
    ui.D.toggled.connect(onClicked)
    # 2
    ui.A_2.toggled.connect(onClicked)
    ui.B_2.toggled.connect(onClicked)
    ui.C_2.toggled.connect(onClicked)
    ui.D_2.toggled.connect(onClicked)
    # 3
    ui.A_3.toggled.connect(onClicked)
    ui.B_3.toggled.connect(onClicked)
    ui.C_3.toggled.connect(onClicked)
    ui.D_3.toggled.connect(onClicked)
    # 4
    ui.A_4.toggled.connect(onClicked)
    ui.B_4.toggled.connect(onClicked)
    ui.C_4.toggled.connect(onClicked)
    ui.D_4.toggled.connect(onClicked)
    # 5
    ui.A_5.toggled.connect(onClicked)
    ui.B_5.toggled.connect(onClicked)
    ui.C_5.toggled.connect(onClicked)
    ui.D_5.toggled.connect(onClicked)
    # 6
    ui.A_6.toggled.connect(onClicked)
    ui.B_6.toggled.connect(onClicked)
    ui.C_6.toggled.connect(onClicked)
    ui.D_6.toggled.connect(onClicked)
    # 7
    ui.A_7.toggled.connect(onClicked)
    ui.B_7.toggled.connect(onClicked)
    ui.C_7.toggled.connect(onClicked)
    ui.D_7.toggled.connect(onClicked)
    # 8
    ui.A_8.toggled.connect(onClicked)
    ui.B_8.toggled.connect(onClicked)
    ui.C_8.toggled.connect(onClicked)
    ui.D_8.toggled.connect(onClicked)
    # 9
    ui.A_9.toggled.connect(onClicked)
    ui.B_9.toggled.connect(onClicked)
    ui.C_9.toggled.connect(onClicked)
    ui.D_9.toggled.connect(onClicked)
    # 10
    ui.A_10.toggled.connect(onClicked)
    ui.B_10.toggled.connect(onClicked)
    ui.C_10.toggled.connect(onClicked)
    ui.D_10.toggled.connect(onClicked)
    ui.finish.clicked.connect(ketQuaThi)


def onClicked():
    if ui.A.isChecked():
        ui.DSDapAnSV.append(ui.A.text()[3::])
    elif ui.B.isChecked():
        ui.DSDapAnSV.append(ui.B.text()[3::])
    elif ui.C.isChecked():
        ui.DSDapAnSV.append(ui.C.text()[3::])
    elif ui.D.isChecked():
        ui.DSDapAnSV.append(ui.D.text()[3::])

    if ui.A_2.isChecked():
        ui.DSDapAnSV.append(ui.A_2.text()[3::])
    elif ui.B_2.isChecked():
        ui.DSDapAnSV.append(ui.B_2.text()[3::])
    elif ui.C_2.isChecked():
        ui.DSDapAnSV.append(ui.C_2.text()[3::])
    elif ui.D_2.isChecked():
        ui.DSDapAnSV.append(ui.D_2.text()[3::])

    # câu 3
    if ui.A_3.isChecked():
        ui.DSDapAnSV.append(ui.A_3.text()[3::])
    elif ui.B_3.isChecked():
        ui.DSDapAnSV.append(ui.B_3.text()[3::])
    elif ui.C_3.isChecked():
        ui.DSDapAnSV.append(ui.C_3.text()[3::])
    elif ui.D_3.isChecked():
        ui.DSDapAnSV.append(ui.D_3.text()[3::])

    # câu 4
    if ui.A_4.isChecked():
        ui.DSDapAnSV.append(ui.A_4.text()[3::])
    elif ui.B_4.isChecked():
        ui.DSDapAnSV.append(ui.B_4.text()[3::])
    elif ui.C_4.isChecked():
        ui.DSDapAnSV.append(ui.C_4.text()[3::])
    elif ui.D_4.isChecked():
        ui.DSDapAnSV.append(ui.D_4.text()[3::])

    # câu 5
    if ui.A_5.isChecked():
        ui.DSDapAnSV.append(ui.A_5.text()[3::])
    elif ui.B_5.isChecked():
        ui.DSDapAnSV.append(ui.B_5.text()[3::])
    elif ui.C_5.isChecked():
        ui.DSDapAnSV.append(ui.C_5.text()[3::])
    elif ui.D_5.isChecked():
        ui.DSDapAnSV.append(ui.D_5.text()[3::])

    # câu 6
    if ui.A_6.isChecked():
        ui.DSDapAnSV.append(ui.A_6.text()[3::])
    elif ui.B_6.isChecked():
        ui.DSDapAnSV.append(ui.B_6.text()[3::])
    elif ui.C_6.isChecked():
        ui.DSDapAnSV.append(ui.C_6.text()[3::])
    elif ui.D_6.isChecked():
        ui.DSDapAnSV.append(ui.D_6.text()[3::])

    # câu 7
    if ui.A_7.isChecked():
        ui.DSDapAnSV.append(ui.A_7.text()[3::])
    elif ui.B_7.isChecked():
        ui.DSDapAnSV.append(ui.B_7.text()[3::])
    elif ui.C_7.isChecked():
        ui.DSDapAnSV.append(ui.C_7.text()[3::])
    elif ui.D_7.isChecked():
        ui.DSDapAnSV.append(ui.D_7.text()[3::])

    # câu 8
    if ui.A_8.isChecked():
        ui.DSDapAnSV.append(ui.A_8.text()[3::])
    elif ui.B_8.isChecked():
        ui.DSDapAnSV.append(ui.B_8.text()[3::])
    elif ui.C_8.isChecked():
        ui.DSDapAnSV.append(ui.C_8.text()[3::])
    elif ui.D_8.isChecked():
        ui.DSDapAnSV.append(ui.D_8.text()[3::])

    # câu 9
    if ui.A_9.isChecked():
        ui.DSDapAnSV.append(ui.A_9.text()[3::])
    elif ui.B_9.isChecked():
        ui.DSDapAnSV.append(ui.B_9.text()[3::])
    elif ui.C_9.isChecked():
        ui.DSDapAnSV.append(ui.C_9.text()[3::])
    elif ui.D_9.isChecked():
        ui.DSDapAnSV.append(ui.D_9.text()[3::])

    # câu 10
    if ui.A_10.isChecked():
        ui.DSDapAnSV.append(ui.A_10.text()[3::])
    elif ui.B_10.isChecked():
        ui.DSDapAnSV.append(ui.B_10.text()[3::])
    elif ui.C_10.isChecked():
        ui.DSDapAnSV.append(ui.C_10.text()[3::])
    elif ui.D_10.isChecked():
        ui.DSDapAnSV.append(ui.D_10.text()[3::])


def ketQuaThi():
    try:
        diem = 0
        for i in range(0, len(ui.DSDapAnSV)):
            if ui.DSDapAnDB[i] == ui.DSDapAnSV[i]:
                diem += 1
        print(diem)

        cur = myDB.cursor()
        cur.execute("INSERT INTO dmkq (MaSV,MaMH,diem) VALUES (%s,%s, %s);",
                    (infoStudent[0][0], ui.result[0][7], diem))
        myDB.commit()
        MBox(0, "Successfully", "Bạn thi được {} ".format(diem), 32)

        showHomeStudent(infoStudent)
    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


if __name__ == "__main__":
    ui = ''
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    showLogin()
    # showHomeTeacher(123)
    # showStudent()
    # showSubjects()
    # showTakeTest()
    # showHomeStudent()
    # showHomeQuestion()
    sys.exit(app.exec())
