# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adminpanel.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        Form.setStyleSheet(u"background-color: rgb(32,37,43);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 381, 281))
        self.label.setStyleSheet(u"background-color: rgba(14,15,20, 0.75);\n"
"border: 1px solid gray;")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(-10, 10, 411, 31))
        self.label_2.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"margin: 0 auto;\n"
"font-size: 20px;")
        self.pushButton_add = QPushButton(Form)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setGeometry(QRect(60, 240, 75, 24))
        self.pushButton_add.setStyleSheet(u"background-color: rgba(43,48,55, 0.8);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color: white;")
        self.pushButton_change = QPushButton(Form)
        self.pushButton_change.setObjectName(u"pushButton_change")
        self.pushButton_change.setGeometry(QRect(160, 240, 75, 24))
        self.pushButton_change.setStyleSheet(u"background-color: rgba(43,48,55, 0.8);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color: white;")
        self.pushButton_delete = QPushButton(Form)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setGeometry(QRect(260, 240, 75, 24))
        self.pushButton_delete.setStyleSheet(u"background-color: rgba(43,48,55, 0.8);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color: white;")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 50, 261, 21))
        self.label_3.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"margin: 0 auto;\n"
"font-size: 14px;")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 80, 261, 21))
        self.label_4.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"margin: 0 auto;\n"
"font-size: 14px;")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(-20, 110, 271, 21))
        self.label_5.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"margin: 0 auto;\n"
"font-size: 14px;")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(-20, 140, 271, 21))
        self.label_6.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"margin: 0 auto;\n"
"font-size: 14px;")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(-20, 170, 271, 21))
        self.label_7.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"margin: 0 auto;\n"
"font-size: 14px;")
        self.lineedit_learntype = QLineEdit(Form)
        self.lineedit_learntype.setObjectName(u"lineedit_learntype")
        self.lineedit_learntype.setGeometry(QRect(220, 50, 151, 21))
        self.lineedit_learntype.setStyleSheet(u"background-color: rgba(43,48,55, 0.8);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color: white;")
        self.lineedit_learntime = QLineEdit(Form)
        self.lineedit_learntime.setObjectName(u"lineedit_learntime")
        self.lineedit_learntime.setGeometry(QRect(220, 80, 151, 21))
        self.lineedit_learntime.setStyleSheet(u"background-color: rgba(43,48,55, 0.8);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color: white;")
        self.lineedit_learnprice_month = QLineEdit(Form)
        self.lineedit_learnprice_month.setObjectName(u"lineedit_learnprice_month")
        self.lineedit_learnprice_month.setGeometry(QRect(220, 110, 151, 21))
        self.lineedit_learnprice_month.setStyleSheet(u"background-color: rgba(43,48,55, 0.8);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color: white;")
        self.lineedit_learntime_sem = QLineEdit(Form)
        self.lineedit_learntime_sem.setObjectName(u"lineedit_learntime_sem")
        self.lineedit_learntime_sem.setGeometry(QRect(220, 140, 151, 21))
        self.lineedit_learntime_sem.setStyleSheet(u"background-color: rgba(43,48,55, 0.8);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color: white;")
        self.lineedit_learnprice_year = QLineEdit(Form)
        self.lineedit_learnprice_year.setObjectName(u"lineedit_learnprice_year")
        self.lineedit_learnprice_year.setGeometry(QRect(220, 170, 151, 21))
        self.lineedit_learnprice_year.setStyleSheet(u"background-color: rgba(43,48,55, 0.8);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color: white;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c, \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c, \u0443\u0434\u0430\u043b\u0438\u0442\u044c \u0444\u043e\u0440\u043c\u0443", None))
        self.pushButton_add.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_change.setText(QCoreApplication.translate("Form", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.pushButton_delete.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0424\u043e\u0440\u043c\u0430 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0421\u0440\u043e\u043a \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f (\u043c\u0435\u0441):", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f(\u0437\u0430 \u043c\u0435\u0441.):", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f(\u0437\u0430 \u0441\u0435\u043c.):", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f (\u0437\u0430 \u0433\u043e\u0434):", None))
    # retranslateUi

