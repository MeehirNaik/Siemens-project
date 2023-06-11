import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Directory Selection")
        self.setGeometry(100, 100, 300, 200)

        self.button = QPushButton("Select Directory", self)
        self.button.setGeometry(50, 50, 200, 30)
        self.button.clicked.connect(self.open_directory_dialog)

    def open_directory_dialog(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            self.button.setText(directory)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
