import tkinter as tk
import cv2
from PIL import Image, ImageTk
from tkinter import messagebox, simpledialog

# Constants
VIDEO_WIDTH = 640
VIDEO_HEIGHT = 480
SERIAL_NUMBER_LENGTH = 5

class WebcamGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Webcam GUI")

        # Create video frame
        self.video_frame = tk.Frame(self.root)
        self.video_frame.pack()

        # Create capture frame
        self.capture_frame = tk.Frame(self.root)
        self.capture_frame.pack()

        # Create video label
        self.video_label = tk.Label(self.video_frame)
        self.video_label.pack()

        # Create capture button
        self.capture_button = tk.Button(self.capture_frame, text="Capture Image", command=self.capture_image)
        self.capture_button.pack()

        # Open webcam
        self.video_capture = cv2.VideoCapture(0)
        self.paused = False
        self.update_video()

    def update_video(self):
        if not self.paused:
            ret, frame = self.video_capture.read()

            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (VIDEO_WIDTH, VIDEO_HEIGHT))

                # Convert frame to ImageTk format
                image = Image.fromarray(frame)
                image_tk = ImageTk.PhotoImage(image)

                # Update video label
                self.video_label.configure(image=image_tk)
                self.video_label.image = image_tk

        # Schedule next update
        self.video_label.after(10, self.update_video)

    def capture_image(self):
        # Pause the video feed
        self.paused = True

        # Prompt for serial number
        serial_number = simpledialog.askstring("Capture Image", "Enter Serial Number:")
        if serial_number is None:
            # Resume video feed
            self.paused = False
            return

        # Check serial number length
        if len(serial_number) != SERIAL_NUMBER_LENGTH:
            messagebox.showerror("Error", "Invalid serial number length!")
            # Resume video feed
            self.paused = False
            return

        # Save image with serial number as the filename
        ret, frame = self.video_capture.read()
        if ret:
            cv2.imwrite(f"{serial_number}.jpg", frame)
            messagebox.showinfo("Success", "Image captured and saved successfully!")

        # Resume video feed
        self.paused = False


# Create the main window
root = tk.Tk()

# Create the GUI
webcam_gui = WebcamGUI(root)

# Start the main loop
root.mainloop()
