import tkinter as tk
from tkinter import filedialog
import numpy as np
from PIL import Image, ImageDraw, ImageTk
import matplotlib.pyplot as plt
import rcs_ui_fun as fun
import svgwrite as svg

def open_image():
    file_path = filedialog.askopenfilename()
    input_image = Image.open(file_path)
    integer_parameter = int(integer_entry.get())
    processed_image = fun.hexagonal_grid_png2(input_image, integer_parameter) # call our processing function
    show_processed_image(processed_image)
    
max_width = 750
max_height = 700
def show_processed_image(image):
    width, height = image.size
    if width > max_width or height > max_height:
        # If the image is larger, scale it down
        scale_factor = min(max_width / width, max_height / height)
        new_width = int(width * scale_factor)
        new_height = int(height * scale_factor)

        # Resize the image
        image = image.resize((new_width, new_height), Image.LANCZOS)
    image = ImageTk.PhotoImage(image)

    panel = tk.Label(window, image=image)
    panel.image = image  # keep a reference
    panel.pack()

window = tk.Tk()
window.title("Hexagonal Grid Image Processing")
window.geometry("800x800")

open_button = tk.Button(window, text="Open Image", command=open_image)
open_button.pack()

integer_entry = tk.Entry(window)
integer_entry.insert(0, "10")  # Set a default value
integer_entry.pack()


window.mainloop()

