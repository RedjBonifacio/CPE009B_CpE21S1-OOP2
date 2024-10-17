from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon

class RegistrationApp(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Account Registration"
        self.width = 400
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, self.width, self.height)
        self.setWindowIcon(QIcon('Oopfa1lbonifacio_lab8'))
        self.center()

        label_x = 20
        input_x = 140
        y_offset = 30
        y_pos = 30

        self.program_title = QLabel("Register for an Account", self)
        self.program_title.setGeometry(self.width // 4, y_pos, 200, 30)
        y_pos += y_offset

        self.first_name_label = QLabel("First Name:", self)
        self.first_name_label.setGeometry(label_x, y_pos, 100, 30)
        self.first_name_input = QLineEdit(self)
        self.first_name_input.setGeometry(input_x, y_pos, 200, 30)
        y_pos += y_offset

        self.last_name_label = QLabel("Last Name:", self)
        self.last_name_label.setGeometry(label_x, y_pos, 100, 30)
        self.last_name_input = QLineEdit(self)
        self.last_name_input.setGeometry(input_x, y_pos, 200, 30)
        y_pos += y_offset

        self.username_label = QLabel("Username:", self)
        self.username_label.setGeometry(label_x, y_pos, 100, 30)
        self.username_input = QLineEdit(self)
        self.username_input.setGeometry(input_x, y_pos, 200, 30)
        y_pos += y_offset

        self.password_label = QLabel("Password:", self)
        self.password_label.setGeometry(label_x, y_pos, 100, 30)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setGeometry(input_x, y_pos, 200, 30)
        y_pos += y_offset

        self.email_label = QLabel("Email Address:", self)
        self.email_label.setGeometry(label_x, y_pos, 100, 30)
        self.email_input = QLineEdit(self)
        self.email_input.setGeometry(input_x, y_pos, 200, 30)
        y_pos += y_offset

        self.contact_label = QLabel("Contact Number:", self)
        self.contact_label.setGeometry(label_x, y_pos, 100, 30)
        self.contact_input = QLineEdit(self)
        self.contact_input.setGeometry(input_x, y_pos, 200, 30)
        y_pos += y_offset

        button_y = y_pos + 40
        self.submit_button = QPushButton('Submit', self)
        self.submit_button.setGeometry(label_x, button_y, 100, 40)

        self.clear_button = QPushButton('Clear', self)
        self.clear_button.setGeometry(input_x, button_y, 100, 40)

        self.submit_button.clicked.connect(self.submit_form)
        self.clear_button.clicked.connect(self.clear_form)

        self.show()

    def submit_form(self):
        print("Form submitted!")

    def clear_form(self):
        self.first_name_input.clear()
        self.last_name_input.clear()
        self.username_input.clear()
        self.password_input.clear()
        self.email_input.clear()
        self.contact_input.clear()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


