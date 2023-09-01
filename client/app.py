import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget
from design.app import Ui_MainWindow
from design.adminpanel_mainwindow import Ui_adminpanel
from client import Client

class Adminpanel(QMainWindow):
    def __init__(self):
        super(Adminpanel, self).__init__()
        self.ui = Ui_adminpanel()
        self.ui.setupUi(self)

        self.ui.pushButton_delete.clicked.connect(self.adminpanel_delete_value)
        self.ui.pushButton_add.clicked.connect(self.adminpanel_add_value)
        self.ui.pushButton_change.clicked.connect(self.adminpanel_change_value)

    def adminpanel_add_value(self):
        try:
            learntype = self.ui.lineedit_learntype.text()
            learntime = self.ui.lineedit_learntime.text()
            learnprice_month = self.ui.lineedit_learnprice_month.text()
            learnprice_sem = self.ui.lineedit_learntime_sem.text()
            learnprice_year = self.ui.lineedit_learnprice_year.text()

            self.ui.lineedit_learntype.clear()
            self.ui.lineedit_learntime.clear()
            self.ui.lineedit_learnprice_month.clear()
            self.ui.lineedit_learntime_sem.clear()
            self.ui.lineedit_learnprice_year.clear()

            client = Client()
            client.connect()
            data = client.send_and_recv_request_on_server(f'select * from learntype;')
            client.close()

            client = Client()
            client.connect()
            client.send_and_recv_request_on_server(f'insert into learntype values ({len(data)+1},\'{learntype}\',{learntime},{learnprice_month},{learnprice_sem},{learnprice_year});')
            client.close()
        except:
            error = QtWidgets.QDialog()
            error.show()
    def adminpanel_delete_value(self):
        try:
            learntype = self.ui.lineedit_learntype.text()

            self.ui.lineedit_learntype.clear()
            self.ui.lineedit_learntime.clear()
            self.ui.lineedit_learnprice_month.clear()
            self.ui.lineedit_learntime_sem.clear()
            self.ui.lineedit_learnprice_year.clear()

            client = Client()
            client.connect()
            client.send_and_recv_request_on_server(f"delete from learntype where learntype='{learntype}'")
            client.close()

        except:
            error = QtWidgets.QDialog()
            error.show()

    def adminpanel_change_value(self):
        learntype = self.ui.lineedit_learntype.text()
        learntime = self.ui.lineedit_learntime.text()
        learnprice_month = self.ui.lineedit_learnprice_month.text()
        learnprice_sem = self.ui.lineedit_learntime_sem.text()
        learnprice_year = self.ui.lineedit_learnprice_year.text()

        self.ui.lineedit_learntype.clear()
        self.ui.lineedit_learntime.clear()
        self.ui.lineedit_learnprice_month.clear()
        self.ui.lineedit_learntime_sem.clear()
        self.ui.lineedit_learnprice_year.clear()

class Application(QMainWindow):
    def __init__(self):
        super(Application, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        client = Client()
        client.connect()
        data = client.send_and_recv_request_on_server('select * from learntype')
        client.close()

        self.update_combobox_learntype()
        self.fill_tablewidget(self.ui.tableWidget_before, data)
        self.ui.pushButton_apply.clicked.connect(self.apply_button_search)
        self.ui.pushButton_clear.clicked.connect(self.clear_button_search)
        self.ui.pushButton_adminpanel.clicked.connect(self.create_adminpanel)

    def create_adminpanel(self):
        self.adminpanel = Adminpanel()
        self.adminpanel.show()
    def update_combobox_learntype(self):
        combobox = self.ui.comboBox_learntype
        combobox.clear()
        client = Client()
        client.connect()
        data = client.send_and_recv_request_on_server('Select learntype from learntype;')
        client.close()
        for item in data:
            combobox.addItem(item[0])
    def fill_tablewidget(self, QTableWidget, data):
        QTableWidget.setRowCount(len(data))
        for row in range(len(data)):
            QTableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[row][1])))
            QTableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data[row][2])))
            QTableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[row][3])))
            QTableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data[row][4])))
            QTableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(data[row][5])))
    def clear_tablewidget(self, QTableWidget):
        QTableWidget.clearContents()
        QTableWidget.setRowCount(0)
    def apply_button_search(self):
        combobox = self.ui.comboBox_learntype.currentText()
        skidka = self.ui.lineedit_skidka.text()
        self.ui.lineedit_skidka.clear()

        client = Client()
        client.connect()
        data = client.send_and_recv_request_on_server(f"select * from learntype where learntype='{combobox}'")
        client.close()

        if skidka == '':
            self.fill_tablewidget(self.ui.tableWidget_before, data)
        else:
            self.fill_tablewidget(self.ui.tableWidget_before, data)
            self.fill_tablewidget(self.ui.tableWidget_after, self.change_data_with_skidka(data, skidka))
    def clear_button_search(self):
        client = Client()
        client.connect()
        data = client.send_and_recv_request_on_server('select * from learntype')
        client.close()

        self.fill_tablewidget(self.ui.tableWidget_before, data)
        self.clear_tablewidget(self.ui.tableWidget_after)
    def change_data_with_skidka(self, tuple_data, skidka=0):
        change_data = []
        float_skidka = float(f'0.{skidka}')
        for i in range(len(tuple_data)):
            list_data = list(tuple_data[i])
            for j in range(len(tuple_data[i])):
                if type(tuple_data[i][j]) is int and j != 2:
                    if skidka == 0:
                        list_data[j] = int(tuple_data[i][j])
                    else:
                        list_data[j] = int(tuple_data[i][j] - (tuple_data[i][j] * float_skidka))
            change_data.append(tuple(list_data))
        return change_data


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec())