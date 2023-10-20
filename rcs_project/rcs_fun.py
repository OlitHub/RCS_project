"""Python function file to be imported in the notebook
"""
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

im = Image.open('./data/wallpaper.jpg')
print(im.format, im.size, im.mode)

def hex_pix2(im,center,hex_size):
    x=center[0]
    y=center[1]
    min_x = int(np.floor(x - hex_size))
    max_x = int(np.floor(x + hex_size))
    min_y = int(np.floor(y - hex_size))
    max_y = int(np.floor(y + hex_size))
    pixels = np.zeros((max_x-min_x,max_y-min_y,3))
    # Iterate through the hexagon
    i=-1
    j=0
    for row in range(min_x,max_x):
        i+1
        for col in range(min_y,max_y):
            pixels[i][j] = im.getpixel((row,col))
            j+1
    pixel = np.mean(pixels, axis=(0,1))

    return(pixel)

print(hex_pix2(im,(50,50),2))
