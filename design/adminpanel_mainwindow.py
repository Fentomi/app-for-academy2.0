# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adminpanel_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_adminpanel(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 300)
        MainWindow.setStyleSheet(u"background-color: rgb(32,37,43);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 381, 281))
        self.label.setStyleSheet(u"background-color: rgba(14,15,20, 0.75);\n"
"border: 1px solid gray;")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(-20, 150, 271, 21))
        self.label_6.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"margin: 0 auto;\n"
"font-size: 14px;")
        self.pushButton_add = QPushButton(self.centralwidget)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setGeometry(QRect(60, 250, 75, 24))
        self.pushButton_add.setStyleSheet(u"background-color: rgba(43,48,55, 0.8);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color: white;")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(-20, 180, 271, 21))
        self.label_7.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"margin: 0 auto;\n"
"font-size: 14px;")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(-20, 120, 271, 21))
        self.label_5.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"margin: 0 auto;\n"
"font-size: 14px;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(-10, 20, 411, 31))
        self.label_2.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"margin: 0 auto;\n"
"font-size: 20px;")
        self.lineedit_learntype = QLineEdit(self.centralwidget)
        self.lineedit_learntype.setObjectName(u"lineedit_learntype")
        self.lineedit_learntype.setGeometry(QRect(220, 60, 151, 21))
        self.lineedit_learntype.setStyleSheet(u"background-color: rgba(43,48,55, 0.8);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color: white;")
        self.lineedit_learnprice_year = QLineEdit(self.centralwidget)
        self.lineedit_learnprice_year.setObjectName(u"lineedit_learnprice_year")
        self.lineedit_learnprice_year.setGeometry(QRect(220, 180, 151, 21))
        self.lineedit_learnprice_year.setStyleSheet(u"background-color: rgba(43,48,55, 0.8);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color: white;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 60, 261, 21))
        self.label_3.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"margin: 0 auto;\n"
"font-size: 14px;")
        self.pushButton_delete = QPushButton(self.centralwidget)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setGeometry(QRect(260, 250, 75, 24))
        self.pushButton_delete.setStyleSheet(u"background-color: rgba(43,48,55, 0.8);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color: white;")
        self.lineedit_learntime = QLineEdit(self.centralwidget)
        self.lineedit_learntime.setObjectName(u"lineedit_learntime")
        self.lineedit_learntime.setGeometry(QRect(220, 90, 151, 21))
        self.lineedit_learntime.setStyleSheet(u"background-color: rgba(43,48,55, 0.8);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color: white;")
        self.pushButton_change = QPushButton(self.centralwidget)
        self.pushButton_change.setObjectName(u"pushButton_change")
        self.pushButton_change.setGeometry(QRect(160, 250, 75, 24))
        self.pushButton_change.setStyleSheet(u"background-color: rgba(43,48,55, 0.8);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color: white;")
        self.lineedit_learnprice_month = QLineEdit(self.centralwidget)
        self.lineedit_learnprice_month.setObjectName(u"lineedit_learnprice_month")
        self.lineedit_learnprice_month.setGeometry(QRect(220, 120, 151, 21))
        self.lineedit_learnprice_month.setStyleSheet(u"background-color: rgba(43,48,55, 0.8);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color: white;")
        self.lineedit_learntime_sem = QLineEdit(self.centralwidget)
        self.lineedit_learntime_sem.setObjectName(u"lineedit_learntime_sem")
        self.lineedit_learntime_sem.setGeometry(QRect(220, 150, 151, 21))
        self.lineedit_learntime_sem.setStyleSheet(u"background-color: rgba(43,48,55, 0.8);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color: white;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 90, 261, 21))
        self.label_4.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"margin: 0 auto;\n"
"font-size: 14px;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f(\u0437\u0430 \u0441\u0435\u043c.):", None))
        self.pushButton_add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f (\u0437\u0430 \u0433\u043e\u0434):", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f(\u0437\u0430 \u043c\u0435\u0441.):", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c, \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c, \u0443\u0434\u0430\u043b\u0438\u0442\u044c \u0444\u043e\u0440\u043c\u0443", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0440\u043c\u0430 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f:", None))
        self.pushButton_delete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton_change.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u043e\u043a \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f (\u043c\u0435\u0441):", None))
    # retranslateUi

