# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registration_window.ui'
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

class Ui_registration_window(object):
    def setupUi(self, registration_window):
        if not registration_window.objectName():
            registration_window.setObjectName(u"registration_window")
        registration_window.resize(1280, 720)
        registration_window.setMinimumSize(QSize(0, 720))
        registration_window.setMaximumSize(QSize(1280, 720))
        registration_window.setStyleSheet(u"border: 1px solid rgba(0, 0, 0, 0);\n"
"border-radius: 7px;")
        self.frame = QFrame(registration_window)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(410, 160, 400, 361))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.labelMain = QLabel(self.frame)
        self.labelMain.setObjectName(u"labelMain")
        self.labelMain.setGeometry(QRect(100, 0, 211, 41))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.labelMain.setFont(font)
        self.labelMain.setStyleSheet(u"")
        self.labelSecond = QLabel(self.frame)
        self.labelSecond.setObjectName(u"labelSecond")
        self.labelSecond.setGeometry(QRect(50, 40, 311, 31))
        font1 = QFont()
        font1.setPointSize(16)
        self.labelSecond.setFont(font1)
        self.EnterRegistrationLogin = QLineEdit(self.frame)
        self.EnterRegistrationLogin.setObjectName(u"EnterRegistrationLogin")
        self.EnterRegistrationLogin.setGeometry(QRect(0, 130, 400, 40))
        self.EnterRegistrationLogin.setMinimumSize(QSize(400, 40))
        self.EnterRegistrationLogin.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"font-size: 20px;\n"
"padding-left: 10px;\n"
"color: rgb(130, 130, 130);")
        self.EnterRegistrationLogin.setMaxLength(32767)
        self.EnterRegistrationLogin.setFrame(True)
        self.EnterRegistrationPassword = QLineEdit(self.frame)
        self.EnterRegistrationPassword.setObjectName(u"EnterRegistrationPassword")
        self.EnterRegistrationPassword.setGeometry(QRect(0, 180, 400, 40))
        self.EnterRegistrationPassword.setMinimumSize(QSize(400, 40))
        self.EnterRegistrationPassword.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"font-size: 20px;\n"
"padding-left: 10px;\n"
"color: rgb(130, 130, 130);")
        self.EnterRegistrationPassword.setMaxLength(32767)
        self.ButtonRegistration = QPushButton(self.frame)
        self.ButtonRegistration.setObjectName(u"ButtonRegistration")
        self.ButtonRegistration.setGeometry(QRect(0, 240, 400, 40))
        self.ButtonRegistration.setMinimumSize(QSize(400, 40))
        self.ButtonRegistration.setStyleSheet(u"QPushButton {\n"
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
        self.labelinfo2.setGeometry(QRect(80, 330, 241, 21))
        self.labelinfo2.setStyleSheet(u"font-size: 16px;\n"
"color: rgb(130, 130, 130);")
        self.line = QFrame(registration_window)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 628, 1281, 5))
        self.line.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_3 = QLabel(registration_window)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 650, 51, 50))
        self.label_3.setPixmap(QPixmap(u":/icons/logo/faq.svg"))
        self.label_4 = QLabel(registration_window)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 650, 63, 50))
        self.label_4.setStyleSheet(u"font: 20pt \"Segoe UI\";")
        self.label_5 = QLabel(registration_window)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(1105, 660, 131, 31))
        self.label_5.setStyleSheet(u"font-size: 16px;\n"
"color: rgb(130, 130, 130);")
        self.layoutWidget = QWidget(registration_window)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 30, 255, 52))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.labelLogo = QLabel(self.layoutWidget)
        self.labelLogo.setObjectName(u"labelLogo")
        self.labelLogo.setPixmap(QPixmap(u":/icons/logo/logopen72.svg"))

        self.horizontalLayout_3.addWidget(self.labelLogo)

        self.labelLogoText = QLabel(self.layoutWidget)
        self.labelLogoText.setObjectName(u"labelLogoText")
        self.labelLogoText.setStyleSheet(u"font-size: 20px;\n"
"\n"
"font: 700 16pt \"Segoe UI\";")

        self.horizontalLayout_3.addWidget(self.labelLogoText)


        self.retranslateUi(registration_window)

        QMetaObject.connectSlotsByName(registration_window)
    # setupUi

    def retranslateUi(self, registration_window):
        registration_window.setWindowTitle(QCoreApplication.translate("registration_window", u"Dialog", None))
        self.labelMain.setText(QCoreApplication.translate("registration_window", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.labelSecond.setText(QCoreApplication.translate("registration_window", u"\u041f\u0440\u0438\u0434\u0443\u043c\u0430\u0439\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0434\u043b\u044f \u0432\u0445\u043e\u0434\u0430", None))
        self.EnterRegistrationLogin.setInputMask("")
        self.EnterRegistrationLogin.setText("")
        self.EnterRegistrationLogin.setPlaceholderText(QCoreApplication.translate("registration_window", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.EnterRegistrationPassword.setInputMask("")
        self.EnterRegistrationPassword.setPlaceholderText(QCoreApplication.translate("registration_window", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.ButtonRegistration.setText(QCoreApplication.translate("registration_window", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.labelinfo.setText(QCoreApplication.translate("registration_window", u"\u041f\u0435\u0440\u0435\u0434 \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u0435\u043c \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438 \u0443\u0431\u0435\u0434\u0438\u0442\u0435\u0441\u044c, \u0447\u0442\u043e", None))
        self.labelinfo2.setText(QCoreApplication.translate("registration_window", u"\u0432\u044b \u0437\u0430\u043f\u043e\u043c\u043d\u0438\u043b\u0438 \u0434\u0430\u043d\u043d\u044b\u0435 \u0434\u043b\u044f \u0432\u0445\u043e\u0434\u0430", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("registration_window", u"FAQ", None))
        self.label_5.setText(QCoreApplication.translate("registration_window", u"\u00a9 2024 \u201cMirage\u201d", None))
        self.labelLogo.setText("")
        self.labelLogoText.setText(QCoreApplication.translate("registration_window", u"Equipment Tracker", None))
    # retranslateUi


