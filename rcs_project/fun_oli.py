# We first use the function `hexagon` to create the hexagonal grid.

def get_color(x, y, img):
    """Returns the color of the pixel at the coordinates (x,y) of the image

    Args:
        x (float): Coordinate X of the pixel
        y (float): Coordinate Y of the pixel
        img (PIL image): Image to be used as a size reference
        
    Returns:
        color (tuple): Tuple of the RGB values of the pixel
    """
    
    color = img.getpixel(x, y)
    
    return color

def hexagonal_grid(img, hex_size):
    
    """Generate a hexagon grid of the size of the image, with hexagons of the size of hex_size

    Args:
        img (PIL image): Image to be used as a size reference
        hex_size (float): Size of the hexagon
        
    Returns:
        grid (PIL image): Image of the hexagonal grid
    """

    WHITE = 1
    size = img.size
    grid = Image.new('RGB', size, WHITE)
    
    # We start drawing the hexagons from the top left corner of the image
    draw = ImageDraw.Draw(grid)
    x = 0
    y = 0
    xmax = size[0]
    ymax = size[1]
    hex_x = int(xmax/hex_size) + 1
    hex_y = int(ymax/2*hex_size*np.sqrt(3)/2) + 1
        
    for i in range(hex_x):
        y = 0
        for j in range(hex_y):
            if (i+j)%2 == 0:
                color = get_color(x, y, img)
                draw.polygon(hexagon(x, y, hex_size), fill=color, outline=None, width=1)
            y += hex_size*np.sqrt(3)/2
        x += hex_size*3/2
    
    return grid

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

hexagonal_grid(img, 10)
    