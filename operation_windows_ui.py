# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'operation-windows.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(371, 401)
        Dialog.setStyleSheet(u"QLineEdit{\n"
"    border: 1px solid rgba(255, 246, 246,80);\n"
"    border-radius: 10px;\n"
"    font-family: Comic Sans MS;\n"
"    font-size: 16px;\n"
"    color: white;\n"
"    background-color: rgb(62, 75, 75)\n"
"}\n"
"\n"
"QLabel{\n"
"    border-radius: 10px;\n"
"    font-family: Comic Sans MS;\n"
"    color:white;\n"
"    font-size: 16px;\n"
"    background-color: rgb(62, 75, 75);\n"
"    border:none;\n"
"} \n"
"\n"
"QWidget{\n"
"    background-color: rgb(22, 54, 56);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgba(116, 63, 240,90);\n"
"    font-family: Comic Sans MS;\n"
"    font-size: 16px;\n"
"    border: 1px solid rgba(247,247,247,80);\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    opacity: 0.2;\n"
"    transition: all 0.5s;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgba(116, 63, 240,90);\n"
"	border: 1px solid rgba(247,247,247,80);\n"
"}\n"
"\n"
"QFrame{\n"
"    background-color: rgb(62, 75, 75);\n"
"    border-radius: 10"
                        "px;\n"
"    border: none;\n"
"} \n"
"\n"
"QComboBox{\n"
"    font-family: Comic Sans MS;\n"
"    font-size: 16px;\n"
"    background-color:rgb(86, 83, 90);\n"
"    border-radius: 10px;\n"
"    border:1px solid rgb(113, 111, 117);\n"
"	color:white;\n"
"}\n"
"\n"
"QPlainTextEdit{\n"
"	border: 1px solid rgba(247,247,247,80);\n"
"    border-radius: 10px;\n"
"    font-family: Comic Sans MS;\n"
"    font-size: 14px;\n"
"    color: white;\n"
"    background-color:rgb(86, 83, 90)\n"
"}\n"
"QTableView {\n"
"background-color: rgb(62, 75, 75);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-bottom-right-radius: 7px; \n"
"border-bottom-left-radius: 7px; \n"
"color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"background-color: rgb(53, 53, 53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 16pt;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgba(255,255,255,50);\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	border: none;\n"
"	color: rgb(255"
                        ", 255, 255);\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 351, 381))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 10, 81, 41))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(18, 65, 61, 31))
        self.label_2.setStyleSheet(u"QLabel{\n"
"    border-radius: 10px;\n"
"    font-family: Comic Sans MS;\n"
"    color:white;\n"
"    font-size: 20px;\n"
"    background-color: rgb(62, 75, 75);\n"
"    border:none;\n"
"} ")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(18, 115, 81, 31))
        self.label_3.setStyleSheet(u"QLabel{\n"
"    border-radius: 10px;\n"
"    font-family: Comic Sans MS;\n"
"    color:white;\n"
"    font-size: 20px;\n"
"    background-color: rgb(62, 75, 75);\n"
"    border:none;\n"
"} \n"
"")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(18, 159, 41, 31))
        self.label_4.setStyleSheet(u"QLabel{\n"
"    border-radius: 10px;\n"
"    font-family: Comic Sans MS;\n"
"    color:white;\n"
"    font-size: 20px;\n"
"    background-color: rgb(62, 75, 75);\n"
"    border:none;\n"
"} ")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(18, 210, 61, 31))
        self.label_5.setStyleSheet(u"QLabel{\n"
"    border-radius: 10px;\n"
"    font-family: Comic Sans MS;\n"
"    color:white;\n"
"    font-size: 20px;\n"
"    background-color: rgb(62, 75, 75);\n"
"    border:none;\n"
"} ")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 260, 81, 31))
        self.label_6.setStyleSheet(u"QLabel{\n"
"    border-radius: 10px;\n"
"    font-family: Comic Sans MS;\n"
"    color:white;\n"
"    font-size: 20px;\n"
"    background-color: rgb(62, 75, 75);\n"
"    border:none;\n"
"} \n"
"")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 315, 41, 31))
        self.label_7.setStyleSheet(u"QLabel{\n"
"    border-radius: 10px;\n"
"    font-family: Comic Sans MS;\n"
"    color:white;\n"
"    font-size: 20px;\n"
"    background-color: rgb(62, 75, 75);\n"
"    border:none;\n"
"} ")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 70, 261, 22))
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(110, 120, 231, 22))
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(60, 170, 281, 22))
        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(80, 220, 261, 22))
        self.lineEdit_5 = QLineEdit(self.frame)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(60, 320, 281, 22))
        self.lineEdit_6 = QLineEdit(self.frame)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(110, 270, 231, 22))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"window-operation", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"New info!", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"name:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"surname:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"age:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Phone:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"address:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Bio:", None))
    # retranslateUi

