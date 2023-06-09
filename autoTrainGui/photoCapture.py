import tkinter as tk
import cv2
from PIL import Image, ImageTk
import datetime

class CameraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Camera App")
        
        # Create a label to display the camera feed
        self.camera_label = tk.Label(self.root)
        self.camera_label.pack()
        
        # Create a button to capture the image
        self.capture_btn = tk.Button(self.root, text="Capture", command=self.capture_image)
        self.capture_btn.pack()
        
        # Create a button to select the save location
        self.location_btn = tk.Button(self.root, text="Select Location", command=self.select_location)
        self.location_btn.pack()

        # Create a button to go back
        self.back_btn = tk.Button(self.root, text="back", command=self.go_back)
        self.back_btn.pack()
        
        # Set default save location
        self.save_location = "C:/"

        # Start the camera feed
        self.capture = cv2.VideoCapture(0)
        self.root.protocol("WM_DELETE_WINDOW", self.close_camera)  # Handle window closing event
        self.show_camera_feed()

        

    def close_camera(self):
        # Release camera resources
        self.capture.release()
        self.root.destroy()  # Close the Toplevel window

    def show_camera_feed(self):
        ret, frame = self.capture.read()
        if ret:
            # Convert the frame from BGR to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Convert the frame to PIL ImageTk format
            image = Image.fromarray(frame)
            image = ImageTk.PhotoImage(image)
            # Update the camera label with the new image
            self.camera_label.configure(image=image)
            self.camera_label.image = image
            
            # Check if the Toplevel window is closed
            if not self.root.winfo_exists():
                self.close_camera()  # Release camera resources
        self.camera_label.after(10, self.show_camera_feed)

    def capture_image(self):
        ret, frame = self.capture.read()
        if ret:
            # Generate a unique name for the image
            current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            image_name = f"captured_image_{current_time}.jpg"
            # Save the captured image to the specified location
            image_path = self.save_location + "/" + image_name
            cv2.imwrite(image_path, frame)
            print("Image saved successfully:", image_name)

    def select_location(self):
        from tkinter import filedialog
        self.save_location = filedialog.askdirectory()
        print("Save location set to:", self.save_location)

    

    def go_back(self):
        # Check if the Toplevel window is closed
        if not self.root.winfo_exists():
            self.close_camera()  # Release camera resources

def run_camera_app():
    root = tk.Toplevel()
    app = CameraApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_camera_app()
