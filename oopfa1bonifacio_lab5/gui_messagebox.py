import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Button Click Example'
        self.left = 100
        self.top = 100
        self.width = 300
        self.height = 200
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        button = QPushButton('Click me', self)
        button.setToolTip('Example Button')
        button.move(100,70)
        button.clicked.connect(self.on_click)
        
        self.show()
    
    @pyqtSlot()
    def on_click(self):
        QMessageBox.information(self, 'Message', 'Button was clicked!', QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

    