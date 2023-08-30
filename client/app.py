import sys
from PySide6.QtWidgets import QApplication,QMainWindow
from design.app import Ui_MainWindow
from client import Client

class Application(QMainWindow):
    def __init__(self):
        super(Application, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.update_combobox_learntype()

    def update_combobox_learntype(self):
        combobox = self.ui.comboBox_learntype
        combobox.clear()
        client = Client()
        client.connect()
        data = client.send_and_recv_request_on_server('Select learntype from learntype;')
        for item in data:
            combobox.addItem(item[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec())