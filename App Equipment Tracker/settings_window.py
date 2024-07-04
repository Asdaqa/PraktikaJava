# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_window.ui'
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
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableView, QWidget)
import res_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1280, 720)
        Dialog.setMaximumSize(QSize(1280, 720))
        Dialog.setStyleSheet(u"border: 1px solid rgba(0, 0, 0, 0);\n"
"border-radius: 7px;")
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 50, 255, 52))
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

        self.labelMain = QLabel(Dialog)
        self.labelMain.setObjectName(u"labelMain")
        self.labelMain.setGeometry(QRect(475, 90, 411, 31))
        self.labelMain.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.lineEquipment = QLineEdit(Dialog)
        self.lineEquipment.setObjectName(u"lineEquipment")
        self.lineEquipment.setGeometry(QRect(71, 160, 250, 40))
        self.lineEquipment.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"font-size: 20px;\n"
"padding-left: 10px;\n"
"color: rgb(130, 130, 130);")
        self.lineStatus = QLineEdit(Dialog)
        self.lineStatus.setObjectName(u"lineStatus")
        self.lineStatus.setGeometry(QRect(367, 160, 250, 40))
        self.lineStatus.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"font-size: 20px;\n"
"padding-left: 10px;\n"
"color: rgb(130, 130, 130);")
        self.lineCustomers = QLineEdit(Dialog)
        self.lineCustomers.setObjectName(u"lineCustomers")
        self.lineCustomers.setGeometry(QRect(663, 160, 250, 40))
        self.lineCustomers.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"font-size: 20px;\n"
"padding-left: 10px;\n"
"color: rgb(130, 130, 130);")
        self.lineResponsible = QLineEdit(Dialog)
        self.lineResponsible.setObjectName(u"lineResponsible")
        self.lineResponsible.setGeometry(QRect(959, 160, 250, 40))
        self.lineResponsible.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"font-size: 20px;\n"
"padding-left: 10px;\n"
"color: rgb(130, 130, 130);")
        self.pushSearch = QPushButton(Dialog)
        self.pushSearch.setObjectName(u"pushSearch")
        self.pushSearch.setGeometry(QRect(367, 235, 250, 40))
        self.pushSearch.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(663, 235, 250, 40))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"font-size: 16px;\n"
"color: rgb(255, 255, 255);\n"
"background-color:  rgb(192, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  rgba(192, 0, 0, 95);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:  rgba(192, 0, 0, 85);\n"
"}\n"
"")
        self.tableView = QTableView(Dialog)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 310, 1251, 391))
        self.tableView.setStyleSheet(u"QTableView {\n"
"background-color: rgb(250, 250, 250);\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"}\n"
"\n"
"QTableView::section {\n"
"background-color: (53,53, 53);\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 14pt;\n"
"}\n"
"\n"
"QTableView::item {\n"
"border-style: none;\n"
"border-bottom: rgba(0, 0, 0, 50);\n"
"}")
        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 290, 1281, 5))
        self.line.setStyleSheet(u"\n"
"background-color: rgb(0, 0, 0);")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.labelLogo.setText("")
        self.labelLogoText.setText(QCoreApplication.translate("Dialog", u"Equipment Tracker", None))
        self.labelMain.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u0434\u0430\u0439\u0442\u0435 \u0444\u0438\u043b\u044c\u0442\u0440\u044b \u0434\u043b\u044f \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.lineEquipment.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.lineStatus.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.lineCustomers.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u043a\u0430\u0437\u0447\u0438\u043a\u0438", None))
        self.lineResponsible.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0435 \u043b\u0438\u0446\u0430", None))
        self.pushSearch.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
    # retranslateUi

