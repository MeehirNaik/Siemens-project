import tkinter as tk


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


root = tk.Tk()
root.title("List Box Multi-Select")

frame = tk.Frame(root)
frame.pack(pady=10)

left_frame = tk.LabelFrame(frame, text="Left Box")
left_frame.pack(side=tk.LEFT, padx=10)

left_box = tk.Listbox(left_frame, selectmode=tk.MULTIPLE)
left_box.pack()

right_frame = tk.LabelFrame(frame, text="Right Box")
right_frame.pack(side=tk.RIGHT, padx=10)

right_box = tk.Listbox(right_frame, selectmode=tk.MULTIPLE)
right_box.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

right_button = tk.Button(button_frame, text=">", command=move_right)
right_button.grid(row=0, column=0, padx=5)

left_button = tk.Button(button_frame, text="<", command=move_left)
left_button.grid(row=0, column=1, padx=5)

items = ["wires", "chip", "registers", "capacitors", "transistors","LEDS"]
for item in items:
    left_box.insert(tk.END, item)

root.mainloop()
