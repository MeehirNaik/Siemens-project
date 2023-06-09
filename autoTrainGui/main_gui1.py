from tkinter import Tk, Label, Entry, Button
from photoCapture import run_camera_app

# List of strings for validation
valid_strings = ['apple', 'banana', 'cherry']

def navigate_to_home():
    input_text = text_input.get().lower()
    if input_text in valid_strings:
        home_page()

def home_page():

    def first_page():
        # Clear the home page
        home_label.pack_forget()
        back_button.pack_forget()

        # Create the first page
        text_input.pack()
        submit_button.pack()

    def camera_window():
        run_camera_app()

    # Clear the first page
    text_input.delete(0, 'end')
    text_input.pack_forget()
    submit_button.pack_forget()

    # Create the home page
    home_label = Label(window, text="Welcome to the Home Page!")
    home_label.pack()

    camera_button = Button(window, text="Open Camera", command=camera_window)
    camera_button.pack()

    back_button = Button(window, text="Go Back", command=first_page)
    back_button.pack()

    



# Create the main window
window = Tk()
window.title("Page Navigation")
window.geometry("500x500")

# Create the text box
text_input = Entry(window)
text_input.pack()

# Create the button
submit_button = Button(window, text="Submit", command=navigate_to_home)
submit_button.pack()

# Run the application
window.mainloop()
