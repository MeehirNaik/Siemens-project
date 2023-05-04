import tkinter as tk
import tkinter.messagebox as mbox
import os

# define GUI elements
class SerialNumberGUI:
    def __init__(self, master):
        self.master = master
        master.title("Serial Number")
        
        # set background color and font
        master.configure(bg="#f2f2f2")
        self.label_font = ("Arial", 14)
        self.entry_font = ("Arial", 12)
        self.button_font = ("Arial", 12, "bold")
        
        # create label and entry box for serial number input
        self.label = tk.Label(master, text="Enter Serial Number:", bg="#f2f2f2", font=self.label_font)
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(master, font=self.entry_font)
        self.entry.pack(padx=20, pady=5)
        
        # create submit button to save serial number
        self.submit_button = tk.Button(master, text="Submit", bg="#0077b6", fg="#ffffff", font=self.button_font, command=self.submit)
        self.submit_button.pack(pady=20)
        
        # check if serial number already exists
        if os.path.isfile("serial_number.txt"):
            self.change_serial_number()
        
    # method to save serial number
    def submit(self):
        serial_number = self.entry.get()
        with open("serial_number.txt", "w") as f:
            f.write(serial_number)
        mbox.showinfo("Success", "Serial number saved successfully!")
        self.master.destroy() # destroy the current window
        
    # method to change serial number if it already exists
    def change_serial_number(self):
        self.master.withdraw() # hide the main window
        new_window = tk.Toplevel(self.master) # create new window for changing serial number
        new_gui = ChangeSerialNumberGUI(new_window, self.master) # pass the main window as a parameter to the new GUI

# define GUI elements for changing serial number
class ChangeSerialNumberGUI:
    def __init__(self, master, main_window):
        self.master = master
        self.main_window = main_window
        master.title("Change Serial Number")
        
        # set background color and font
        master.configure(bg="#f2f2f2")
        self.label_font = ("Arial", 14)
        self.entry_font = ("Arial", 12)
        self.button_font = ("Arial", 12, "bold")
        
        # create label and entry box for new serial number input
        self.label = tk.Label(master, text="Enter New Serial Number:", bg="#f2f2f2", font=self.label_font)
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(master, font=self.entry_font)
        self.entry.pack(padx=20, pady=5)
        
        # create submit button to save new serial number
        self.submit_button = tk.Button(master, text="Submit", bg="#0077b6", fg="#ffffff", font=self.button_font, command=self.submit)
        self.submit_button.pack(pady=20)
        
        # bind the window close event to a method that shows the main window again
        master.protocol("WM_DELETE_WINDOW", self.show_main_window)
        
    # method to save new serial number
    def submit(self):
        serial_number = self.entry.get()
        with open("serial_number.txt", "w") as f:
            f.write(serial_number)
        mbox.showinfo("Success", "Serial number saved successfully!")
        self.show_main_window()

    # method to show the main window again and close the current window
    def show_main_window(self):
        self.master.destroy() # destroy the current window
        self.main_window.deiconify() # show the main window again
        self.main_window.destroy()

#run the gui

root = tk.Tk()
gui = SerialNumberGUI(root)
root.mainloop()