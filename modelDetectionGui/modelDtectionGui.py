import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image
import cv2

def pass_button_click():
    print("PASS")

def fail_button_click():
    print("FAIL")

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

        video_label.img_tk = img_tk  # Keep a reference to avoid garbage collection
        video_label.configure(image=img_tk)

    # Repeat the update every 10 milliseconds
    video_label.after(5, update_frame)
    # video_label2.after(5, update_frame)

root = tk.Tk()
root.title("MLFB Number Verification")

# Get the available camera devices
available_cameras = []
for i in range(10):
    cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
    if cap.isOpened():
        available_cameras.append(i)
        cap.release()

# Create a combo box to select the camera
camera_combobox = tk.Spinbox(root, values=available_cameras)
camera_combobox.pack(pady=10)

# Create a button to start the selected camera
start_button = tk.Button(root, text="Start", command=select_camera)
start_button.pack(pady=10)

# Create a label and entry textbox
mlfb_label = tk.Label(root, text="MLFB NUMBER", anchor="nw")
mlfb_label.pack(side="top", padx=10, pady=10)

mlfb_entry = tk.Entry(root)
mlfb_entry.pack(side="top", padx=10, pady=10)

# Create a frame to show camera feed
camera_frame = tk.Frame(root, width=640, height=480, bg="black")
camera_frame.pack(side="left", padx=10, pady=10)

video_label = tk.Label(camera_frame)
video_label.pack()

# Create pass and fail buttons
button_frame = tk.Frame(root)
button_frame.pack(side="left", padx=10, pady=10)

button_font = font.Font(weight="bold")

pass_button = tk.Button(button_frame, text="PASS", fg="white", bg="green", width=5, height=10, font=button_font,
                        command=pass_button_click)
pass_button.pack(side="top", pady=10)

fail_button = tk.Button(button_frame, text="FAIL", fg="white", bg="red", width=5, height=10, font=button_font,
                        command=fail_button_click)
fail_button.pack(side="top", pady=10)

# Create a frame to show logs
log_frame = tk.Frame(root, width=200, bg="white")
log_frame.pack(side="right", fill="y", padx=10, pady=10)

# Configure weight to make log frame expand vertically
root.rowconfigure(1, weight=1)

# Run the GUI
root.mainloop()
