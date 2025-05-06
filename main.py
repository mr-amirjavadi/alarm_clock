from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys, os
import webbrowser
import random
import string
from datetime import datetime
import pytz
import csv

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(636, 515)
        MainWindow.setMinimumSize(QtCore.QSize(636, 515))
        MainWindow.setMaximumSize(QtCore.QSize(636, 515))
        MainWindow.setSizeIncrement(QtCore.QSize(636, 515))
        MainWindow.setBaseSize(QtCore.QSize(636, 515))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
                                         "    font: 9pt \"MS Shell Dlg 2\";\n"
                                         "background-color : rgb(170, 170, 255)\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, 0, 637, 471))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_6 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 6, 7, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 6, 3, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 6, 6, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 6, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 8, 14, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 6, 4, 1, 1)
        self.checkBox_1 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_1.setObjectName("checkBox_1")
        self.gridLayout.addWidget(self.checkBox_1, 6, 2, 1, 1)
        self.checkBox_0 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_0.setObjectName("checkBox_0")
        self.gridLayout.addWidget(self.checkBox_0, 6, 1, 1, 1)

        self.lcdNumber = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber.setStyleSheet("QLCDNumber {\n"
                                     "background-color : rgb(255, 255, 255)\n"
                                     "}")
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout.addWidget(self.lcdNumber, 2, 3, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 6, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 2, 1, 1)
        self.textEdit_todo = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_todo.setStyleSheet("QTextEdit {\n"
                                         "background-color : rgb(255, 255, 255)\n"
                                         "}")
        self.textEdit_todo.setObjectName("textEdit_todo")
        self.gridLayout.addWidget(self.textEdit_todo, 9, 1, 1, 7)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 1, 1, 7)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 10, 1, 1, 7)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 7, 1, 1, 7)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 7)
        self.pushButton_save = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_save.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_save.setFont(font)
        self.pushButton_save.setStyleSheet("QPushButton {\n"
                                           "background-color : rgb(255, 255, 255)\n"
                                           "}")
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout.addWidget(self.pushButton_save, 11, 5, 1, 2)
        self.pushButton_reset = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_reset.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_reset.setFont(font)
        self.pushButton_reset.setStyleSheet("QPushButton {\n"
                                            "background-color : rgb(255, 255, 255)\n"
                                            "}")
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.gridLayout.addWidget(self.pushButton_reset, 11, 2, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 8, 3, 1, 3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 0, 0, 14, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 1, 1, 1, 7)
        self.timeEdit_settime = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        self.timeEdit_settime.setStyleSheet("QTimeEdit {\n"
                                            "background-color : rgb(255, 255, 255)\n"
                                            "}")
        self.timeEdit_settime.setObjectName("timeEdit_settime")
        iran_tz = pytz.timezone('Asia/Tehran')
        iran_time = datetime.now(iran_tz)
        self.timeEdit_settime.setTime(QTime(iran_time.hour, iran_time.minute))
        self.gridLayout.addWidget(self.timeEdit_settime, 4, 3, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 636, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.timer = QTimer()
        self.timer.timeout.connect(self.lcd_number)
        self.timer.start(1000)
        self.lcd_number()
        self.pushButton_save.clicked.connect(self.save_alarm)
        self.pushButton_reset.clicked.connect(self.reset_form)
    def save_alarm(self):
        # گرفتن زمان از timeEdit
        alarm_time = self.timeEdit_settime.time().toString("HH:mm")

        # گرفتن متن از QTextEdit
        todo_text = self.textEdit_todo.toPlainText()

        # گرفتن روزهای انتخاب شده از چک‌باکس‌ها
        days = []
        for i in range(7):
            checkbox = getattr(self, f'checkBox_{i}')
            if checkbox.isChecked():
                days.append(checkbox.text())

        # ساختن یک رشته برای روزها
        days_str = ', '.join(days)

        # ذخیره در فایل CSV
        with open("alarms.csv", "a", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["==="])  # جداکننده بین رکوردها
            writer.writerow(["Time", alarm_time])
            writer.writerow(["Days", days_str])
            writer.writerow(["Text", todo_text])

        # فلگ فعال شدن آلارم
        self.alarm_enabled = True

        QMessageBox.information(None, "Saved", "Alarm has been saved!")

    def reset_form(self):
        # 1. پاک کردن متن یادداشت
        self.textEdit_todo.clear()

        # 2. ریست کردن زمان به ساعت فعلی ایران
        iran_tz = pytz.timezone('Asia/Tehran')
        iran_time = datetime.now(iran_tz)
        self.timeEdit_settime.setTime(QTime(iran_time.hour, iran_time.minute))

        # 3. برداشتن تیک همه چک‌باکس‌ها
        for i in range(7):
            checkbox = getattr(self, f'checkBox_{i}')
            checkbox.setChecked(False)

        # 4. غیرفعال‌کردن آلارم
        if hasattr(self, 'alarm_enabled'):
            del self.alarm_enabled
        if hasattr(self, 'alarm_triggered'):
            del self.alarm_triggered

        # 5. پیام اطلاع
        QMessageBox.information(None, "Reset", "فرم به حالت اولیه بازگشت.")

    def lcd_number(self):
        # نمایش ساعت ایران
        iran_tz = pytz.timezone('Asia/Tehran')
        iran_time = datetime.now(iran_tz)
        f_time = iran_time.strftime("%H:%M:%S")
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.display(f_time)

        #  فقط اگه آلارم فعال شده بود
        if not hasattr(self, 'alarm_enabled') or not self.alarm_enabled:
            return

        # زمان تنظیم‌شده توسط کاربر
        alarm_time = self.timeEdit_settime.time().toString("HH:mm")
        current_time = iran_time.strftime("%H:%M")

        # متن هشدار
        alarm_text = self.textEdit_todo.toPlainText().strip()
        if not alarm_text:
            alarm_text = "⏰ وقتشه بیدار شی!"

        # اجرا فقط یک‌بار
        if current_time == alarm_time and not hasattr(self, 'alarm_triggered'):
            self.alarm_triggered = True
            QMessageBox.critical(None, "⏰ WAKE UP!", alarm_text)

        # ریست‌کردن برای تکرار در آینده
        if current_time != alarm_time and hasattr(self, 'alarm_triggered'):
            del self.alarm_triggered
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox_6.setText(_translate("MainWindow", "Friday"))
        self.checkBox_2.setText(_translate("MainWindow", "Monday"))
        self.checkBox_5.setText(_translate("MainWindow", "Thursday"))
        self.checkBox_4.setText(_translate("MainWindow", "Wednesday"))
        self.checkBox_3.setText(_translate("MainWindow", "Tuesday"))
        self.checkBox_1.setText(_translate("MainWindow", "Sunday"))
        self.checkBox_0.setText(_translate("MainWindow", "Saturday"))
        self.label.setText(_translate("MainWindow", "Alarm clock"))
        self.pushButton_save.setText(_translate("MainWindow", "Save"))
        self.pushButton_reset.setText(_translate("MainWindow", "Reset"))
        self.label_2.setText(_translate("MainWindow", "What are you going to do?"))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
