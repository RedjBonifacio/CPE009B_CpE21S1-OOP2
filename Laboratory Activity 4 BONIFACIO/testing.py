import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "PyQt Line Edit"
        self.x = 200  # or left
        self.y = 200  # or top
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('Oopfa1lbonifacio_lab8'))

        # Create textbox
        self.textbox = QLineEdit(self)

        self.textbox.move(20, 20)
        self.textbox.resize(255, 20)

        # Create label
        self.textboxlbl = QLabel("Hello World!", self)

        self.textboxlbl.move(self.width // 2 - self.textboxlbl.width() // 2, 25)  # Center the label

        # Create another label
        self.pycharm_label = QLabel("This program is written in PyCharm", self)

        self.pycharm_label.move(self.width // 3 - self.pycharm_label.width() // 2, self.textboxlbl.y() + self.textboxlbl.height() + 10)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


