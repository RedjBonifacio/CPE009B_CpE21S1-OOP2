import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import csv

class AccountRegistration(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Account Registration')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.username = QLineEdit(placeholderText="Username")
        self.password = QLineEdit(placeholderText="Password", echoMode=QLineEdit.Password)
        self.email = QLineEdit(placeholderText="Email")

        register_button = QPushButton('Register')
        register_button.clicked.connect(self.register)

        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(self.email)
        layout.addWidget(register_button)

    def register(self):
        username = self.username.text().strip()
        password = self.password.text().strip()
        email = self.email.text().strip()

        if not all([username, password, email]):
            QMessageBox.warning(self, 'Error', 'All fields must be filled!')
            return

        try:
            with open('accounts.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([username, password, email])
            QMessageBox.information(self, 'Success', 'Registration successful!')
            self.username.clear()
            self.password.clear()
            self.email.clear()
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Registration failed: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AccountRegistration()
    ex.show()
    sys.exit(app.exec_())

    