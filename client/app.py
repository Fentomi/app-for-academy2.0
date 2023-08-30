import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget
from design.app import Ui_MainWindow
from client import Client

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

    def apply_button_search(self):
        combobox = self.ui.comboBox_learntype.currentText()
        skidka = self.ui.lineedit_skidka.text()
        self.ui.lineedit_skidka.clear()

        client = Client()
        client.connect()
        data = client.send_and_recv_request_on_server(f"select * from learntype where learntype='{combobox}'")
        client.close()

        self.fill_tablewidget(self.ui.tableWidget_before, data)
    def clear_button_search(self):
        client = Client()
        client.connect()
        data = client.send_and_recv_request_on_server('select * from learntype')
        client.close()

        self.fill_tablewidget(self.ui.tableWidget_before, data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec())