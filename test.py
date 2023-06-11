import sys
from PyQt6.QtWidgets import QHBoxLayout ,QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton
from PyQt6.QtCore import Qt


from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMouseEvent


from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMouseEvent, QPainter, QColor, QBrush
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton


class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self.setStyleSheet(
            """
            QWidget {
                background-color: rgba(250, 250, 250, 200);
                border: 1px solid rgba(255, 255, 255, 30);
                border-radius: 10px;
            }
            QLineEdit {
                background-color: rgba(200, 200, 200, 200);
                qproperty-alignment: AlignCenter; /* Align text to center */
                padding: 5px;
                font-size: 14px; /* Adjust font size */
                font-weight: bold; /* Apply bold font style */
                border-radius: 5px;
                color: #333333; /* Set font color */
            }
            QPushButton {
                background-color: rgba(255, 255, 255, 150);
                padding: 5px;
                border: 1px solid rgba(0, 0, 0, 0);
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 200);
            }
            """
        )

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        self.text_input = QLineEdit(self)
        layout.addWidget(self.text_input)

        button_layout = QHBoxLayout()
        apply_button = QPushButton("Apply", self)
        apply_button.clicked.connect(self.apply_and_close)
        button_layout.addWidget(apply_button)

        close_button = QPushButton("Close", self)
        close_button.clicked.connect(self.close)
        button_layout.addWidget(close_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_dragging = True
            self.mouse_press_pos = event.globalPosition()
            self.window_pos = self.pos()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.is_dragging:
            global_pos = event.globalPosition()
            moved = global_pos - self.mouse_press_pos
            self.move(self.window_pos + moved)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_dragging = False

    def apply_and_close(self):
        input_text = self.text_input.text()
        print("Input Text:", input_text)
        self.close()




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 400, 300)

        self.button = QPushButton("Open Second Window", self)
        self.button.setGeometry(150, 120, 150, 30)
        self.button.clicked.connect(self.open_second_window)

    def open_second_window(self):
        self.second_window = SecondWindow()
        self.second_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
