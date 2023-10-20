"""test file for rcs_project/rcs_fun.py
"""
from PIL import Image
import numpy as np
from rcs_project import rcs_fun as fun

def test_get_color():
    """Test the get_color function
    """
    img = Image.open("data/test_image.png")
    
    r1 = np.random.randint(0, img.size[0])
    r2 = np.random.randint(0, img.size[1])
    
    assert fun.get_color(img, (r1, r2)) == (255, 255, 255)
    
def test_get_color2():
    """Test the get_color2 function
    """
    img = Image.open("data/test_image.png")
    
    r1 = np.random.randint(0, img.size[0])
    r2 = np.random.randint(0, img.size[1])
    
    assert fun.get_color(img, (r1, r2)) == (255, 255, 255)
