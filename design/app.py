# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1130, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(32,37,43);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 431, 171))
        self.label.setStyleSheet(u"background-color: rgba(14,15,20, 0.75);\n"
"border: 1px solid gray;")
        self.pushButton_apply = QPushButton(self.centralwidget)
        self.pushButton_apply.setObjectName(u"pushButton_apply")
        self.pushButton_apply.setGeometry(QRect(70, 160, 75, 24))
        self.pushButton_apply.setStyleSheet(u"background-color: rgba(43,48,55, 0.8);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color: white;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 40, 141, 31))
        self.label_2.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"margin: 0 auto;\n"
"font-size: 20px;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 90, 261, 21))
        self.label_3.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"margin: 0 auto;\n"
"font-size: 14px;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 120, 261, 21))
        self.label_4.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"margin: 0 auto;\n"
"font-size: 14px;")
        self.lineedit_skidka = QLineEdit(self.centralwidget)
        self.lineedit_skidka.setObjectName(u"lineedit_skidka")
        self.lineedit_skidka.setGeometry(QRect(260, 120, 151, 21))
        self.lineedit_skidka.setStyleSheet(u"background-color: rgba(43,48,55, 0.8);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color: white;")
        self.pushButton_clear = QPushButton(self.centralwidget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setGeometry(QRect(160, 160, 75, 24))
        self.pushButton_clear.setStyleSheet(u"background-color: rgba(43,48,55, 0.8);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color: white;")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 220, 531, 351))
        self.label_5.setStyleSheet(u"background-color: rgba(14,15,20, 0.75);\n"
"border: 1px solid gray;")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(580, 220, 531, 351))
        self.label_6.setStyleSheet(u"background-color: rgba(14,15,20, 0.75);\n"
"border: 1px solid gray;")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(-10, 220, 301, 31))
        self.label_7.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"margin: 0 auto;\n"
"font-size: 20px;")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(550, 220, 141, 31))
        self.label_8.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"margin: 0 auto;\n"
"font-size: 20px;")
        self.pushButton_adminpanel = QPushButton(self.centralwidget)
        self.pushButton_adminpanel.setObjectName(u"pushButton_adminpanel")
        self.pushButton_adminpanel.setGeometry(QRect(20, 0, 75, 24))
        self.pushButton_adminpanel.setStyleSheet(u"background-color: rgba(43,48,55, 0.8);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color: white;")
        self.comboBox_learntype = QComboBox(self.centralwidget)
        self.comboBox_learntype.setObjectName(u"comboBox_learntype")
        self.comboBox_learntype.setGeometry(QRect(260, 90, 151, 22))
        self.comboBox_learntype.setStyleSheet(u"background-color: rgba(43,48,55, 0.8);\n"
"border: 1px solid gray;\n"
"color: white;")
        self.tableWidget_before = QTableWidget(self.centralwidget)
        if (self.tableWidget_before.columnCount() < 5):
            self.tableWidget_before.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_before.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_before.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_before.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_before.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_before.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_before.setObjectName(u"tableWidget_before")
        self.tableWidget_before.setGeometry(QRect(30, 260, 511, 301))
        self.tableWidget_before.setMinimumSize(QSize(391, 0))
        self.tableWidget_before.setStyleSheet(u"")
        self.tableWidget_before.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_before.horizontalHeader().setMinimumSectionSize(32)
        self.tableWidget_before.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_after = QTableWidget(self.centralwidget)
        if (self.tableWidget_after.columnCount() < 5):
            self.tableWidget_after.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_after.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_after.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_after.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_after.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_after.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.tableWidget_after.setObjectName(u"tableWidget_after")
        self.tableWidget_after.setGeometry(QRect(590, 260, 511, 301))
        self.tableWidget_after.setMinimumSize(QSize(391, 0))
        self.tableWidget_after.setStyleSheet(u"")
        self.tableWidget_after.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_after.horizontalHeader().setMinimumSectionSize(32)
        self.tableWidget_after.verticalHeader().setCascadingSectionResizes(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FentomiApp", None))
        self.label.setText("")
        self.pushButton_apply.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u043e\u0440\u043c\u0443 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0440\u0430\u0437\u043c\u0435\u0440 \u0441\u043a\u0438\u0434\u043a\u0438(%):", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0441\u043a\u0438\u0434\u043a\u0438:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0435:", None))
        self.pushButton_adminpanel.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u043c\u0438\u043d\u043a\u0430", None))
        ___qtablewidgetitem = self.tableWidget_before.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f", None));
        ___qtablewidgetitem1 = self.tableWidget_before.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u043e\u043a", None));
        ___qtablewidgetitem2 = self.tableWidget_before.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u0438\u043c. \u0432 \u043c\u0435\u0441.", None));
        ___qtablewidgetitem3 = self.tableWidget_before.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u0438\u043c. \u0432 \u0441\u0435\u043c.", None));
        ___qtablewidgetitem4 = self.tableWidget_before.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u0438\u043c. \u0432 \u0433\u043e\u0434.", None));
        ___qtablewidgetitem5 = self.tableWidget_after.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f", None));
        ___qtablewidgetitem6 = self.tableWidget_after.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u043e\u043a", None));
        ___qtablewidgetitem7 = self.tableWidget_after.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u0438\u043c. \u0432 \u043c\u0435\u0441.", None));
        ___qtablewidgetitem8 = self.tableWidget_after.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u0438\u043c. \u0432 \u0441\u0435\u043c.", None));
        ___qtablewidgetitem9 = self.tableWidget_after.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u0438\u043c. \u0432 \u0433\u043e\u0434.", None));
    # retranslateUi

