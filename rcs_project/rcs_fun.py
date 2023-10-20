"""Python function file to be imported in the notebook
"""
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

im = Image.open('./data/screenshot.jpg')
print(im.format, im.size, im.mode)

def hex_pix(im):
    height,width = im.size
    hexagon_size = 50
    pixels = np.zeros((height, width,3))
    # Define the size and spacing of the hexagons
    horizontal_spacing = hexagon_size * 3/4
    vertical_spacing = hexagon_size * (3 ** 0.5 / 2)
    # Iterate through the hexagonal grid
    for row in range((height)//int(vertical_spacing)):
        for col in range((width)//int(horizontal_spacing)):
            x = row * vertical_spacing
            y = col* horizontal_spacing

            # If the row is odd, shift every second column
            if row % 2 == 1:
                y += horizontal_spacing

            pixels[row][col] = im.getpixel((x, y))

    return(pixels,pixels.shape)

print(hex_pix(im))