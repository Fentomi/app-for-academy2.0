import sys
from PySide6.QtWidgets import QApplication,QMainWindow
from design.app import Ui_MainWindow

class Application(QMainWindow):
    def __init__(self):
        super(Application, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec())