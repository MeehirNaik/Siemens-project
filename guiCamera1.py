import tkinter as tk
import cv2
from PIL import ImageTk, Image

def select_camera():
    global cap
    selected_camera = int(camera_combobox.get())
    cap = cv2.VideoCapture(selected_camera)
    update_frame()

def update_frame():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (640, 480))

        processed_frame = process_frame(frame)

        img = Image.fromarray(frame)
        img_tk = ImageTk.PhotoImage(image=img)

        video_label.img_tk = img_tk  # Keep a reference to avoid garbage collection
        video_label.configure(image=img_tk)

        processed_img = Image.fromarray(processed_frame)
        processed_img_tk = ImageTk.PhotoImage(image=processed_img)

        processed_label.img_tk = processed_img_tk
        processed_label.configure(image=processed_img_tk)

    # Repeat the update every 10 milliseconds
    video_label.after(10, update_frame)

def process_frame(frame):
    # Add your image processing code here
    # For example, you can convert the image to grayscale
    processed_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    return processed_frame

# Create the main window
window = tk.Tk()
window.title("Camera Selection")

# Get the available camera devices
available_cameras = []
for i in range(10):
    cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
    if cap.isOpened():
        available_cameras.append(i)
        cap.release()

# Create a combo box to select the camera
camera_combobox = tk.Spinbox(window, values=available_cameras)
camera_combobox.pack(pady=10)

# Create a button to start the selected camera
start_button = tk.Button(window, text="Start", command=select_camera)
start_button.pack(pady=10)

# Create a label to display the video
video_label = tk.Label(window)
video_label.pack()

# Create a label to display the processed image
processed_label = tk.Label(window)
processed_label.pack()

# Start the GUI event loop
window.mainloop()

# Release the camera and destroy the window when done
if 'cap' in globals():
    cap.release()
cv2.destroyAllWindows()
