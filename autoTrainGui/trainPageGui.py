import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import cv2

def select_directory():
    directory = filedialog.askdirectory()
    directory_label.config(text="Directory selected: " + directory)

def take_picture():
    # Open the camera and capture a picture
    camera = cv2.VideoCapture(0)
    _, image = camera.read()
    camera.release()

    # Save the picture as "photo.jpg"
    cv2.imwrite("photo.jpg", image)

    messagebox.showinfo("Success", "Picture taken and saved as photo.jpg")

def select_options():
    selected_options = left_box.curselection()
    selected_values = [left_box.get(index) for index in selected_options]
    messagebox.showinfo("Selected Options", f"Selected options: {', '.join(selected_values)}")

def additional_button():
    messagebox.showinfo("Additional Button", "This is an additional button!")

def perform_action():
    # Perform the desired action
    messagebox.showinfo("Action", "Performing the action...")


def move_right():
    selected_indices = left_box.curselection()
    for index in reversed(selected_indices):
        item = left_box.get(index)
        right_box.insert(tk.END, item)
        left_box.delete(index)


def move_left():
    selected_indices = right_box.curselection()
    for index in reversed(selected_indices):
        item = right_box.get(index)
        left_box.insert(tk.END, item)
        right_box.delete(index)

# Create the main window
window = tk.Tk()
window.title("GUI Example")
window.geometry("700x500")
window.config(bg="white")

# Create the input text field and label
input_field = tk.Entry(window)
input_field.grid(row=0, column=1, padx=10, pady=10,sticky="W")
label = tk.Label(window, text="Input MLFB:", bg="white")
label.grid(row=0, column=0, padx=10, pady=10,sticky="E")

# Create the button to select a directory
directory_button = tk.Button(window, text="Select Directory", command=select_directory)
directory_button.grid(row=1, column=0, padx=30, pady=10, sticky="W")
directory_label = tk.Label(window, text="Directory selected:", bg="white")
directory_label.grid(row=1, column=0,columnspan=2, padx=150, pady=10, sticky="W")

# Create the button to take a picture
picture_button = tk.Button(window, text="Take Picture", command=take_picture)
picture_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

frame = tk.Frame(window)
frame.grid(row=3, column=0, rowspan=2, columnspan=2, padx=10, pady=(0, 10), sticky="W")

left_frame = tk.LabelFrame(frame, text="Left Box")
left_frame.pack(side=tk.LEFT, padx=10)

left_box = tk.Listbox(left_frame, selectmode=tk.MULTIPLE)
left_box.pack()

right_frame = tk.LabelFrame(frame, text="Right Box")
right_frame.pack(side=tk.RIGHT, padx=10)

right_box = tk.Listbox(right_frame, selectmode=tk.MULTIPLE)
right_box.pack()

button_frame = tk.Frame(window)
button_frame.grid(row=7, column=0, columnspan=2, padx=10, pady=(0, 10))

right_button = tk.Button(button_frame, text=">", command=move_right)
right_button.grid(row=0, column=0, padx=5)

left_button = tk.Button(button_frame, text="<", command=move_left)
left_button.grid(row=0, column=1, padx=5)


options = ["Option 1", "Option 2", "Option 3", "Option 4"]
for option in options:
    left_box.insert(tk.END, option)

# Create the button for selecting options
select_options_button = tk.Button(window, text="Select Options", command=select_options)
select_options_button.grid(row=3, column=1, padx=10, pady=(0, 10), sticky="W")

# Create an additional button in row 4
additional_butn = tk.Button(window, text="Additional Button", command=additional_button)
additional_butn.grid(row=4, column=1, padx=10, pady=(0, 10), sticky="W")

# Create the button in row 5 column 0
button_row5_col0 = tk.Button(window, text="Button in row 5 column 0", bg="light blue", fg="white")
button_row5_col0.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

# Create the button to perform an action
perform_action_button = tk.Button(window, text="Perform Action", command=perform_action, bg="green", fg="white")
perform_action_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

# Configure grid column and row weights
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(8, weight=1)

# Start the main loop
window.mainloop()
