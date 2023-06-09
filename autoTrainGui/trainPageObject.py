import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from photoCapture import run_camera_app
import cv2


class GUIExample:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("GUI Example")
        self.window.geometry("500x500")
        self.window.config(bg="white")

        self.create_widgets()

    def create_widgets(self):
        self.create_input_field()
        self.create_directory_selection()
        self.create_picture_button()
        self.create_option_selection()
        self.create_additional_button()
        self.create_action_button()
        self.create_list_box_buttons()

    def create_input_field(self):
        self.input_field = tk.Entry(self.window)
        self.input_field.grid(row=0, column=0, padx=100, pady=10, sticky="W")
        self.label = tk.Label(self.window, text="Input MLFB:", bg="white")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

    def create_directory_selection(self):
        self.directory_button = tk.Button(self.window, text="Select Directory", command=self.select_directory)
        self.directory_button.grid(row=1, column=0, padx=30, pady=10, sticky="W")
        self.directory_label = tk.Label(self.window, text="Directory selected:", bg="white")
        self.directory_label.grid(row=1, column=0, columnspan=2, padx=150, pady=10, sticky="W")

    def create_picture_button(self):
        self.picture_button = tk.Button(self.window, text="Take Picture", command=self.take_picture)
        self.picture_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def create_option_selection(self):
        self.frame = tk.Frame(self.window)
        self.frame.grid(row=3, column=0, rowspan=2, columnspan=2, padx=10, pady=(0, 10), sticky="W")

        self.left_frame = tk.LabelFrame(self.frame, text="Left Box")
        self.left_frame.pack(side=tk.LEFT, padx=10)

        self.listbox_border_left = tk.Frame(self.left_frame, bd=1, relief="sunken", background="white")
        self.listbox_border_left.pack(padx=10, pady=10, fill=None, expand=False)

        self.listbox_left = tk.Listbox(self.listbox_border_left, width=20, height=10,
                            borderwidth=0, highlightthickness=0,selectmode=tk.MULTIPLE,
                            background=self.listbox_border_left.cget("background"),
        )
        self.vsb_left = tk.Scrollbar(self.listbox_border_left, orient="vertical", command=self.listbox_left.yview)
        self.listbox_left.configure(yscrollcommand=self.vsb_left)
        self.vsb_left.pack(side="right", fill="y")
        self.listbox_left.pack(padx=10, pady=10, fill="both", expand=True)

        self.right_frame = tk.LabelFrame(self.frame, text="Right Box")
        self.right_frame.pack(side=tk.RIGHT, padx=10)

        self.listbox_border_right = tk.Frame(self.right_frame, bd=1, relief="sunken", background="white")
        self.listbox_border_right.pack(padx=10, pady=10, fill=None, expand=False)

        self.listbox_right = tk.Listbox(self.listbox_border_right, width=20, height=10,
                            borderwidth=0, highlightthickness=0,selectmode=tk.MULTIPLE,
                            background=self.listbox_border_right.cget("background"),
        )
        self.vsb_right = tk.Scrollbar(self.listbox_border_right, orient="vertical", command=self.listbox_right.yview)
        self.listbox_right.configure(yscrollcommand=self.vsb_right)
        self.vsb_right.pack(side="right", fill="y")
        self.listbox_right.pack(padx=10, pady=10, fill="both", expand=True)


        # for i in range(100):
        #     self.listbox_left.insert("end", "Item #{}".format(i))
        
        options = ["Chips", "IC", "Resistors", "Capacitors","LED"]
        for option in options:
            self.listbox_left.insert(tk.END, option)

        self.sort_listboxes() # sort listbox data


        # self.left_frame = tk.LabelFrame(self.frame, text="Left Box")
        # self.left_frame.pack(side=tk.LEFT, padx=10)
        # self.left_box = tk.Listbox(self.left_frame, selectmode=tk.MULTIPLE)
        # self.left_box.pack()

        # self.right_frame = tk.LabelFrame(self.frame, text="Right Box")
        # self.right_frame.pack(side=tk.RIGHT, padx=10)
        # self.right_box = tk.Listbox(self.right_frame, selectmode=tk.MULTIPLE)
        # self.right_box.pack()

        # options = ["chips", "IC", "Resistors", "Capacitors","LED"]
        # for option in options:
        #     self.left_box.insert(tk.END, option)

        self.select_options_button = tk.Button(self.window, text="train new label model", command=self.select_options)
        self.select_options_button.grid(row=3, column=2, padx=10, pady=(0, 10), sticky="W")

    def create_additional_button(self):
        self.additional_butn = tk.Button(self.window, text="import label model", command=self.additional_button)
        self.additional_butn.grid(row=4, column=2, padx=10, pady=(0, 10), sticky="W")

    def create_action_button(self):

        self.apply_models_butn = tk.Button(self.window, text="apply selected models", bg="light blue", fg="white")
        self.apply_models_butn.grid(row=8, column=0, columnspan=1, padx=10, pady=10)

        self.button_row5_col0 = tk.Button(self.window, text="open labelImg", bg="light blue", fg="white")
        self.button_row5_col0.grid(row=8, column=1, columnspan=1, padx=10, pady=10)

        self.perform_action_button = tk.Button(
            self.window, text="train yolo model", command=self.perform_action, bg="green", fg="white"
        )
        self.perform_action_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

    def create_list_box_buttons(self):
        self.button_frame = tk.Frame(self.window)
        self.button_frame.grid(row=3, column=0, rowspan=2, columnspan=2, padx=10, pady=(0, 10))

        self.right_button = tk.Button(self.button_frame, text=">", command=self.move_right)
        self.right_button.grid(row=0, column=0, pady=5)

        self.left_button = tk.Button(self.button_frame, text="<", command=self.move_left)
        self.left_button.grid(row=1, column=0, pady=5)

    def select_directory(self):
        directory = filedialog.askdirectory()
        self.directory_label.config(text="Directory selected: " + directory)

    def take_picture(self):
        run_camera_app()

    def select_options(self):
        selected_options = self.listbox_left.curselection()
        selected_values = [self.listbox_left.get(index) for index in selected_options]
        messagebox.showinfo("Selected Options", f"Selected options: {', '.join(selected_values)}")

    def additional_button(self):
        messagebox.showinfo("Additional Button", "This is an additional button!")

    def perform_action(self):
        messagebox.showinfo("Action", "Performing the action...")

    def move_right(self):
        selected_indices = self.listbox_left.curselection()
        for index in reversed(selected_indices):
            item = self.listbox_left.get(index)
            self.listbox_right.insert(tk.END, item)
            self.listbox_left.delete(index)
        self.sort_listboxes()

    def move_left(self):
        selected_indices = self.listbox_right.curselection()
        for index in reversed(selected_indices):
            item = self.listbox_right.get(index)
            self.listbox_left.insert(tk.END, item)
            self.listbox_right.delete(index)
        self.sort_listboxes()
    
    def sort_listboxes(self):
        # Sort the items in the left and right listboxes
        left_items = sorted(self.listbox_left.get(0, tk.END))
        right_items = sorted(self.listbox_right.get(0, tk.END))

        # Clear the listboxes
        self.listbox_left.delete(0, tk.END)
        self.listbox_right.delete(0, tk.END)

        # Insert the sorted items back into the listboxes
        for item in left_items:
            self.listbox_left.insert(tk.END, item)
        for item in right_items:
            self.listbox_right.insert(tk.END, item)

    # def move_right(self):
    #     selected_indices = self.left_box.curselection()
    #     for index in reversed(selected_indices):
    #         item = self.left_box.get(index)
    #         self.right_box.insert(tk.END, item)
    #         self.left_box.delete(index)

    # def move_left(self):
    #     selected_indices = self.right_box.curselection()
    #     for index in reversed(selected_indices):
    #         item = self.right_box.get(index)
    #         self.left_box.insert(tk.END, item)
    #         self.right_box.delete(index)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    gui = GUIExample()
    gui.run()