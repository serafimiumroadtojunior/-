# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uimain.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTableView,
    QWidget)
import res-icon-qrc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(502, 423)
        icon = QIcon()
        icon.addFile(u":/icon/icons/home_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QLineEdit{\n"
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
"    font-size: 26px;\n"
"    background-color: rgb(62, 75, 75);\n"
"    border:none;\n"
"} \n"
"\n"
"QWidget{\n"
"    background-color: rgb(22, 54, 56);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgba(116, 63, 240,80);\n"
"    font-family: Comic Sans MS;\n"
"    font-size: 16px;\n"
"    border: 1px solid rgba(247,247,247,80);\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"    height:50px\n"
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
" "
                        "   border-radius: 10px;\n"
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
"	border: none;"
                        "\n"
"	color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QHBoxLayout{\n"
"    background-color: rgb(62, 75, 75);\n"
"    border-radius: 10px;\n"
"    border: none;\n"
"} ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 481, 401))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 10, 191, 31))
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 120, 151, 41))
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/add_circle_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(22, 22))
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(160, 120, 161, 41))
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/delete_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(22, 22))
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(320, 120, 151, 41))
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/edit_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QSize(22, 22))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 50, 141, 21))
        self.label_2.setStyleSheet(u"QLabel{\n"
"    border-radius: 10px;\n"
"    font-family: Comic Sans MS;\n"
"    color:white;\n"
"    font-size: 14px;\n"
"    background-color: rgb(62, 75, 75);\n"
"    border:none;\n"
"} ")
        self.tableView = QTableView(self.frame)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 170, 461, 221))
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 10, 31, 31))
        self.label_3.setMaximumSize(QSize(1116, 16777215))
        self.label_3.setPixmap(QPixmap(u":/icon/icons/handshake_FILL0_wght400_GRAD0_opsz24.svg"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0456\u0432\u0440\u043e\u0431\u0456\u0442\u043d\u0438\u043a\u0438!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0456\u0432\u0440\u043e\u0431\u0456\u0442\u043d\u0438\u043a\u0438!", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add Information", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Delete Information", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Edit Information", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"*With PostgreSQL*", None))
        self.label_3.setText("")
    # retranslateUi

