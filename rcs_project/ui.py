"""user interface for the hexagonal grid image processing project 
"""
import tkinter as tk
from tkinter import filedialog
import numpy as np
from PIL import Image, ImageDraw, ImageTk
import rcs_fun as fun
import svgwrite as svg
current_image = None

def open_image():
    """Open a file dialog window and open the selected image"""
    global panel
    file_path = filedialog.askopenfilename()
    input_image = Image.open(file_path)
    integer_parameter = int(integer_entry.get())
    processed_image =scale_image(fun.hexagonal_grid_png2(input_image, integer_parameter)) # call our processing function
    panel = tk.Label(window, image=processed_image)
    panel.image = processed_image # keep a reference
    panel.pack()
    

    # Disable the open button
    open_button.config(state="disabled")
    message_label.config(text="Image displayed. Click 'Reset' to pick another image or 'Save Image' to save.")

# Function to clear the image

max_width = 650
max_height = 800

def scale_image(image):
    global current_image
    """Scale down the image if it is too large to display"""
    width, height = image.size
    if width > max_width or height > max_height:
        # If the image is larger, scale it down
        scale_factor = min(max_width / width, max_height / height)
        new_width = int(width * scale_factor)
        new_height = int(height * scale_factor)

        # Resize the image
        image = image.resize((new_width, new_height), Image.LANCZOS)
    current_image = image
    image = ImageTk.PhotoImage(image)
    return image

def save_image():
    """Save the current image"""
    if current_image:
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            current_image.save(save_path)


def reset_image():
    """Reset the image to none and reactivate the open button"""
    panel.pack_forget()
    open_button.config(state="normal")
    message_label.config(text="No image displayed. Click 'Open Image'.")



window = tk.Tk()
window.title("Hexagonal Grid Image Processing")
window.geometry("800x800")

message_label = tk.Label(window, text="No image displayed. Click 'Open Image'.")
message_label.pack()

open_button = tk.Button(window, text="Open Image", command=open_image)
open_button.pack()


integer_entry = tk.Entry(window)
integer_entry.insert(0, "10")  # Set a default value
integer_entry.pack()

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

# Create the Reset button
reset_button = tk.Button(button_frame, text="Reset",command=reset_image)
reset_button.grid(row=0, column=0, padx=5)

# Create the Save button
save_button = tk.Button(button_frame, text="Save",command=save_image)
save_button.grid(row=0, column=1, padx=5)

# Create the Exit button
exit_button = tk.Button(button_frame, text="Exit",command=window.quit)
exit_button.grid(row=0, column=2, padx=5)

window.mainloop()