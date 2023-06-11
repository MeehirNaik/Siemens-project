import sys
import cv2
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication,QFileDialog, QMainWindow, QLabel, QComboBox, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QLabel
from PyQt6 import uic
from PyQt6 import QtGui
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
import numpy as np

class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self,camera_dir):
        super().__init__()
        self._run_flag = True
        self.camera_dir = camera_dir
        
    def run(self):
        # capture from web cam
        cap = cv2.VideoCapture(self.camera_dir)
        # max_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # max_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        while self._run_flag:
            ret, cv_img = cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)
        # shut down capture system
        cap.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.disply_width = 960
        self.display_height = 540
        self.directory = None
        self.camera_flag = False

        uic.loadUi("mainwindow.ui",self)

        self.photo_capt_butn: QPushButton = self.pushButton
        # self.theme_butn: QPushButton = self.pushButton_3
        self.location_butn: QPushButton = self.pushButton_5
        self.camera_select_butn: QPushButton = self.pushButton_6
        self.lineEdit: QLineEdit = self.lineEdit
        self.camera_lineEdit: QLineEdit = self.lineEdit_2
        self.label: QLabel = self.label
        self.comboBox: QLineEdit = self.comboBox

        self.location_butn.clicked.connect(self.open_directory_dialog)
        self.photo_capt_butn.clicked.connect(self.capture_frame)
        self.camera_select_butn.clicked.connect(self.switch_camera)
        
    def switch_camera(self):
        if self.lineEdit.text().strip():  # Check if the text box is not empty
            print("Text box is not empty")
        else:
            print("Text box is empty")
            return
        if self.camera_flag == True:
            self.thread.stop()
            print("Thread Stopped")
        # create the video capture thread
        self.camera_dir = self.camera_lineEdit.text()
        if self.camera_dir.isdigit():
            self.camera_dir = int(self.camera_dir)
            self.camera_select_butn.setText('camera: Cam')
        else:
            self.camera_select_butn.setText('camera: IP')
        self.thread = VideoThread(self.camera_dir)
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        # start the thread
        self.thread.start()
        self.camera_flag = True

    def open_directory_dialog(self):
        self.directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if self.directory:
            self.location_butn.setText(self.directory)
    
    def capture_frame(self):
        if self.directory is None:
            return
        
        if self.lineEdit.text().strip():  # Check if the text box is not empty
            print("Text box is not empty")
        else:
            print("Text box is empty")
            return
        
        if self.camera_lineEdit.text().strip():  # Check if the text box is not empty
            print("Text box is not empty")
        else:
            print("Text box is empty")
            return
        

        if self.camera_flag == True:
            # Generate a unique filename for the captured frame
            filename = self.directory + "/" + self.lineEdit.text() + self.comboBox.currentText()

            cv2.imwrite(filename, self.cv_img)

            print("Frame captured and saved at:", filename)

    def closeEvent(self, event):
        if self.camera_flag == True:
            self.thread.stop()
        event.accept()

    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        self.cv_img = cv_img
        qt_img = self.convert_cv_qt(cv_img)
        self.label.setPixmap(qt_img)
    
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.AspectRatioMode.KeepAspectRatio)
        return QPixmap.fromImage(p)

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())