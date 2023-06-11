import sys
from PyQt6 import QtCore

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QWidget, QLineEdit, QPushButton, QTextEdit,QVBoxLayout
from PyQt6.QtGui import QIcon
from PyQt6 import uic


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("mainwindow.ui",self)

        self.pushButton: QPushButton = self.pushButton
        self.pushButton_3: QPushButton = self.pushButton_3
        self.pushButton_5: QPushButton = self.pushButton_5
        self.pushButton_6: QPushButton = self.pushButton_6
        self.lineEdit: QLineEdit = self.lineEdit
        self.label: QLabel = self.label
        self.comboBox: QLineEdit = self.comboBox


        self.pushButton_5.clicked.connect(self.sayHello)

    #     self.setWindowTitle('hello World')
    #     self.setWindowIcon(QIcon(r"C:\Users\naikm\Downloads\virology_lab_test_coronavirus_covid_detection_laboratory_icon_134541.ico"))
    #     self.resize(500, 400) #width, height

    #     layout = QVBoxLayout()
    #     self.setLayout(layout)

    #     # Widgets
    #     self.inputField = QLineEdit()
    #     self.button = QPushButton('&Say Hello',clicked = self.sayHello)
    #     # self.button.clicked.connect(self.sayHello)
        
    #     self.output =QTextEdit()

    #     layout.addWidget(self.inputField)
    #     layout.addWidget(self.button)
    #     layout.addWidget(self.output)

    def sayHello(self):
        self.lineEdit.setText("meehir")

app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MyApp()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event
# loop has stopped.
