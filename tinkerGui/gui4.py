import tkinter as tk
import cv2
from PIL import ImageTk, Image

def process_input():
    operator = operator_entry.get()
    # Process the input here
    print("Operator:", operator)

def minimize_window():
    window.iconify()

def maximize_window():
    window.state('zoomed')

def toggle_fullscreen():
    if window.attributes('-fullscreen'):
        window.attributes('-fullscreen', False)
    else:
        window.attributes('-fullscreen', True)

def close_window():
    window.destroy()

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
    video_label.after(10, update_frame)

# Create the main window
window = tk.Tk()

# Set the window title
window.title("The Title of Test")

# Configure the window to full screen
window.attributes("-fullscreen", True)

# Create a frame to hold the content
frame = tk.Frame(window)
frame.pack(pady=50)

# Create a label for the heading
heading_label = tk.Label(frame, text="The Title of Test", font=("Arial", 24, "bold"), bg="blue", fg="white")
heading_label.grid(row=0, column=0, columnspan=2, sticky='w', padx=10, pady=(10, 20))

# Create a label for the operator number
operator_label = tk.Label(frame, text="Operator Number:")
operator_label.grid(row=0, column=3, sticky='e', padx=10, pady=10)

# Create an entry for the operator number
operator_entry = tk.Entry(frame, font=("Arial", 14))
operator_entry.grid(row=0, column=4, sticky='w', padx=10, pady=10)

# Create a button to process the input
process_button = tk.Button(frame, text="Process", command=process_input)
process_button.grid(row=0, column=5, columnspan=2, pady=20)

# Create the buttons for minimize, maximize, fullscreen, and close
minimize_button = tk.Button(window, text="_", command=minimize_window)
minimize_button.place(x=10, y=10, width=30, height=30)

maximize_button = tk.Button(window, text="[]", command=maximize_window)
maximize_button.place(x=50, y=10, width=30, height=30)

fullscreen_button = tk.Button(window, text="⤢", command=toggle_fullscreen)
fullscreen_button.place(x=90, y=10, width=30, height=30)

close_button = tk.Button(window, text="X", command=close_window)
close_button.place(x=130, y=10, width=30, height=30)

# Set column weights to position elements
window.grid_columnconfigure(0, weight=1)  # Title box on left
window.grid_columnconfigure(1, weight=1)  # Buttons on right

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

# Start the GUI event loop
window.mainloop()

# Release the camera and destroy the window when done
if 'cap' in globals():
    cap.release()
cv2.destroyAllWindows()
