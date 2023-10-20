"""Python function file to be imported in the notebook
"""
import numpy as np
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

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


def get_color(x, y, img):
    """Returns the color of the pixel at the coordinates (x,y) of the image

    Args:
        x (float): Coordinate X of the pixel
        y (float): Coordinate Y of the pixel
        img (PIL image): Image to be used as a size reference
        
    Returns:
        color (tuple): Tuple of the RGB values of the pixel
    """
    print(x, y)
    size = img.size
    
    while x > size[0]:
        x -= 1
    while x < 0:
        x += 1
    while y > size[1]:
        y -= 1
    while y < 0:
        y += 1

    color = img.getpixel((x, y))
    
    return color


def hexagon(x, y, hex_size):

    """Generates the coordinates of each corners of a hexagon with the coordinates of the top-left corner

    Args:
        x (float): Coordinate X of the top-left corner
        y (float): Coordinate Y of the top-left corner
        
    Returns:
        corners (list): List of the coordinates of each corners of the hexagon
    """

    corners = [(x, y),
               (x+hex_size, y), 
               (x+hex_size*3/2, y+hex_size*np.sqrt(3)/2), 
               (x+hex_size, y+hex_size*np.sqrt(3)), 
               (x, y+hex_size*np.sqrt(3)), 
               (x-hex_size/2, y+hex_size*np.sqrt(3)/2)]

    return corners


def hexagonal_grid(img, hex_size):

    """Generate a hexagon grid of the size of the image, with hexagons of the size of hex_size

    Args:
        img (PIL image): Image to be used as a size reference
        hex_size (float): Size of the hexagon
        
    Returns:
        grid (PIL image): Image of the hexagonal grid
    """

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    size = img.size
    grid = Image.new('RGB', size, WHITE)

    # We start drawing the hexagons from the top left corner of the image
    draw = ImageDraw.Draw(grid)
    xmax = size[0]
    ymax = size[1]
    hex_x = int(xmax/hex_size)
    hex_y = int(ymax/2*hex_size*np.sqrt(3)/2) + 5

    x = 0
    for i in range(hex_x):
        y = 0 - hex_size*np.sqrt(3)/2
        for j in range(hex_y):
            if (i+j)%2 == 0:
                # color = get_color(x + hex_size/2, y + hex_size*np.sqrt(3)/2, img)
                draw.polygon(hexagon(x, y, hex_size), fill=BLACK, outline=WHITE, width=1)
            y += hex_size*np.sqrt(3)/2
        x += hex_size*3/2

    return grid
