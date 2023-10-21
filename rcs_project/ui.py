"""user interface for the hexagonal grid image processing project 
"""
import tkinter as tk
from tkinter import filedialog
import numpy as np
from PIL import Image, ImageDraw, ImageTk
import rcs_ui_fun as fun
import svgwrite as svg

def open_image():
    global panel # make panel a global variable so we can access it later
    file_path = filedialog.askopenfilename()
    input_image = Image.open(file_path)
    integer_parameter = int(integer_entry.get())
    processed_image =scale_image(fun.hexagonal_grid_png2(input_image, integer_parameter)) # call our processing function
    panel = tk.Label(window, image=processed_image)
    panel.image = processed_image # keep a reference
    panel.pack()

max_width = 700
max_height = 800

def scale_image(image):
    width, height = image.size
    if width > max_width or height > max_height:
        # If the image is larger, scale it down
        scale_factor = min(max_width / width, max_height / height)
        new_width = int(width * scale_factor)
        new_height = int(height * scale_factor)

        # Resize the image
        image = image.resize((new_width, new_height), Image.LANCZOS)
    image = ImageTk.PhotoImage(image)
    return image

def reset_image():
    panel.pack_forget()

window = tk.Tk()
window.title("Hexagonal Grid Image Processing")
window.geometry("800x800")

open_button = tk.Button(window, text="Open Image", command=open_image)
open_button.pack()


integer_entry = tk.Entry(window)
integer_entry.insert(0, "10")  # Set a default value
integer_entry.pack()

reset_button = tk.Button(window, text="Reset", command=reset_image)
reset_button.pack()


window.mainloop()