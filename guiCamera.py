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

        img = Image.fromarray(frame)
        img_tk = ImageTk.PhotoImage(image=img)

        video_label1.img_tk = img_tk  # Keep a reference to avoid garbage collection
        video_label1.configure(image=img_tk)

        # video_label2.img_tk = img_tk  # Keep a reference to avoid garbage collection
        # video_label2.configure(image=img_tk)

    # Repeat the update every 10 milliseconds
    video_label1.after(5, update_frame)
    # video_label2.after(5, update_frame)

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
video_label1 = tk.Label(window)
video_label1.pack()

# video_label2 = tk.Label(window)
# video_label2.pack()

# Start the GUI event loop
window.mainloop()

# Release the camera and destroy the window when done
if 'cap' in globals():
    cap.release()
cv2.destroyAllWindows()
