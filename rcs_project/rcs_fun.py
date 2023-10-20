"""Python function file to be imported in the notebook
"""
import numpy as np
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import svgwrite as svg

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

def get_color(x, y, img):
    """Returns the color of the pixel at the coordinates (x,y) of the image

    Args:
        x (float): Coordinate X of the pixel
        y (float): Coordinate Y of the pixel
        img (PIL image): Image to be used as a size reference
        
    Returns:
        color (tuple): Tuple of the RGB values of the pixel
    """
    size = img.size
    
    while (x > size[0] - 1):
        x = x - 1.
    
    while (x < 0):
        x = x + 1.
    
    while (y > size[1] - 1):
        y = y - 1.
    
    while (y < 0):
        y = y + 1.
        
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


def hexagonal_grid_png(img, hex_size):

    """Generate a hexagon grid of the size of the image, with hexagons of the size of hex_size

    Args:
        img (PIL image): Image to be used as a size reference
        hex_size (float): Size of the hexagon
        
    Returns:
        grid (PIL image): Image of the hexagonal grid
    """
    path = '../data/'
    name = img.filename.split('/')[-1].split('.')[0]
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    size = img.size
    image_grid = Image.new('RGB', size, WHITE)

    # We start drawing the hexagons from the top left corner of the image
    draw = ImageDraw.Draw(image_grid)
    xmax = size[0]
    ymax = size[1]
    hex_x = int(xmax/hex_size)
    hex_y = int(ymax/(hex_size*np.sqrt(3)/2)) + 2
    
    x = 0
    for i in range(hex_x):
        y = 0 - hex_size*np.sqrt(3)/2
        for j in range(hex_y):
            if (i+j)%2 == 0:
                color = hex_pix2(img, (x + hex_size/2, y + hex_size*np.sqrt(3)/2), hex_size)
                draw.polygon(hexagon(x, y, hex_size), fill=color, outline=None, width=1)
            y += hex_size*np.sqrt(3)/2
        x += hex_size*3/2

    image_grid.save(path + name + '_' + str(hex_size) + '_hexagonal_grid.png')
    return image_grid

def hexagonal_grid_svg(img, hex_size):
    
    size = img.size
    
    path = '../data/'
    name = img.filename.split('/')[-1].split('.')[0]
    name_tot = path + name + '_' + str(hex_size) + '_hexagonal_grid.svg'
    dwg = svg.Drawing(name_tot, size=size, profile='tiny')
    
    # We start drawing the hexagons from the top left corner of the image
    xmax = size[0]
    ymax = size[1]
    hex_x = int(xmax/hex_size)
    hex_y = int(ymax/(hex_size*np.sqrt(3)/2)) + 2
    
    x = 0
    for i in range(hex_x):
        y = 0 - hex_size*np.sqrt(3)/2
        for j in range(hex_y):
            if (i+j)%2 == 0:
                color = get_color(x + hex_size/2, y + hex_size*np.sqrt(3)/2, img)
                dwg.add(dwg.polygon(points=hexagon(x, y, hex_size), fill=svg.rgb(color[0], color[1], color[2])))
            y += hex_size*np.sqrt(3)/2
        x += hex_size*3/2
    
    dwg.save()
    
    return dwg