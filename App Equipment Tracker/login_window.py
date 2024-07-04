# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)
import res_rc

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(1280, 720)
        LoginWindow.setStyleSheet(u"border: 1px solid rgba(0, 0, 0, 0);\n"
"border-radius: 7px;")
        self.ButtonRegister = QPushButton(LoginWindow)
        self.ButtonRegister.setObjectName(u"ButtonRegister")
        self.ButtonRegister.setGeometry(QRect(440, 590, 400, 40))
        self.ButtonRegister.setMinimumSize(QSize(400, 40))
        self.ButtonRegister.setStyleSheet(u"QPushButton {\n"
"font-size: 16px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(0, 0, 0, 95);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(0, 0, 0, 85);\n"
"}\n"
"")
        self.labelInfo3 = QLabel(LoginWindow)
        self.labelInfo3.setObjectName(u"labelInfo3")
        self.labelInfo3.setGeometry(QRect(540, 550, 211, 21))
        self.labelInfo3.setMinimumSize(QSize(1, 0))
        self.labelInfo3.setStyleSheet(u"font-size: 16px;\n"
"color: rgb(130, 130, 130);")
        self.frame = QFrame(LoginWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(440, 140, 400, 361))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.labelMain = QLabel(self.frame)
        self.labelMain.setObjectName(u"labelMain")
        self.labelMain.setGeometry(QRect(70, 0, 251, 41))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.labelMain.setFont(font)
        self.labelSecond = QLabel(self.frame)
        self.labelSecond.setObjectName(u"labelSecond")
        self.labelSecond.setGeometry(QRect(90, 40, 221, 31))
        font1 = QFont()
        font1.setPointSize(16)
        self.labelSecond.setFont(font1)
        self.EnterLogin = QLineEdit(self.frame)
        self.EnterLogin.setObjectName(u"EnterLogin")
        self.EnterLogin.setGeometry(QRect(0, 130, 400, 40))
        self.EnterLogin.setMinimumSize(QSize(400, 40))
        self.EnterLogin.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"font-size: 20px;\n"
"padding-left: 10px;\n"
"color: rgb(130, 130, 130);")
        self.EnterLogin.setMaxLength(32767)
        self.EnterLogin.setFrame(True)
        self.EnterPassword = QLineEdit(self.frame)
        self.EnterPassword.setObjectName(u"EnterPassword")
        self.EnterPassword.setGeometry(QRect(0, 180, 400, 40))
        self.EnterPassword.setMinimumSize(QSize(400, 40))
        self.EnterPassword.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"font-size: 20px;\n"
"padding-left: 10px;\n"
"color: rgb(130, 130, 130);")
        self.EnterPassword.setMaxLength(32767)
        self.ButtonCome = QPushButton(self.frame)
        self.ButtonCome.setObjectName(u"ButtonCome")
        self.ButtonCome.setGeometry(QRect(0, 240, 400, 40))
        self.ButtonCome.setMinimumSize(QSize(400, 40))
        self.ButtonCome.setStyleSheet(u"QPushButton {\n"
"font-size: 16px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(0, 0, 0, 95);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(0, 0, 0, 85);\n"
"}\n"
"")
        self.labelinfo = QLabel(self.frame)
        self.labelinfo.setObjectName(u"labelinfo")
        self.labelinfo.setGeometry(QRect(20, 290, 361, 40))
        self.labelinfo.setMinimumSize(QSize(0, 40))
        self.labelinfo.setStyleSheet(u"font-size: 16px;\n"
"color: rgb(130, 130, 130);")
        self.labelinfo2 = QLabel(self.frame)
        self.labelinfo2.setObjectName(u"labelinfo2")
        self.labelinfo2.setGeometry(QRect(140, 330, 121, 21))
        self.labelinfo2.setStyleSheet(u"font-size: 16px;\n"
"color: rgb(130, 130, 130);")
        self.line = QFrame(LoginWindow)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 110, 1281, 5))
        self.line.setStyleSheet(u"\n"
"background-color: rgb(0, 0, 0);")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.layoutWidget = QWidget(LoginWindow)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 20, 255, 52))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelLogo = QLabel(self.layoutWidget)
        self.labelLogo.setObjectName(u"labelLogo")
        self.labelLogo.setPixmap(QPixmap(u":/icons/logo/logopen72.svg"))

        self.horizontalLayout.addWidget(self.labelLogo)

        self.labelLogoText = QLabel(self.layoutWidget)
        self.labelLogoText.setObjectName(u"labelLogoText")
        self.labelLogoText.setStyleSheet(u"font-size: 20px;\n"
"\n"
"font: 700 16pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.labelLogoText)


        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Dialog", None))
        self.ButtonRegister.setText(QCoreApplication.translate("LoginWindow", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.labelInfo3.setText(QCoreApplication.translate("LoginWindow", u"\u2014 \u0412\u0430\u0441 \u0435\u0449\u0435 \u043d\u0435\u0442\u0443 \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0435? ", None))
        self.labelMain.setText(QCoreApplication.translate("LoginWindow", u"\u0412\u0445\u043e\u0434 \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0443", None))
        self.labelSecond.setText(QCoreApplication.translate("LoginWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u0432\u043e\u0438 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.EnterLogin.setInputMask("")
        self.EnterLogin.setText("")
        self.EnterLogin.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.EnterPassword.setInputMask("")
        self.EnterPassword.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.ButtonCome.setText(QCoreApplication.translate("LoginWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.labelinfo.setText(QCoreApplication.translate("LoginWindow", u"\u041f\u0435\u0440\u0435\u0434 \u0432\u0445\u043e\u0434\u043e\u043c \u0443\u0431\u0435\u0434\u0438\u0442\u0435\u0441\u044c \u0432 \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e\u0441\u0442\u0438 \u043d\u0430\u0431\u043e\u0440\u0430", None))
        self.labelinfo2.setText(QCoreApplication.translate("LoginWindow", u"\u0412\u0430\u0448\u0438\u0445 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.labelLogo.setText("")
        self.labelLogoText.setText(QCoreApplication.translate("LoginWindow", u"Equipment Tracker", None))
    # retranslateUi

