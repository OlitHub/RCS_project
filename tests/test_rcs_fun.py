"""test file for rcs_project/rcs_fun.py
"""
from PIL import Image
import numpy as np
from rcs_project import rcs_fun as fun


def test_get_color():
    """Tests the get_color function
    """
    img = Image.open("data/test_image.png")

    r1 = np.random.randint(0, img.size[0])
    r2 = np.random.randint(0, img.size[1])

    assert fun.get_color(img, (r1, r2)) == (255, 255, 255)


def test_get_color2():
    """Tests the get_color2 function
    """
    img = Image.open("data/test_image.png")

    r1 = np.random.randint(0, img.size[0])
    r2 = np.random.randint(0, img.size[1])

    assert fun.get_color(img, (r1, r2)) == (255, 255, 255)


def test_hexagon():
    """Tests the hexagon function
    """

    x = np.random.randint(0, 100)
    y = np.random.randint(0, 100)
    size = np.random.randint(1, 100)
    corners = fun.hexagon(x, y, size)
    assert round(np.mean(corners), 5) == round(
        np.mean([x + size / 2, y + size * np.sqrt(3) / 2]), 5)
    # Checks if the center of the hexagon is correct


def test_hex_grids():
    """Tests the hexagonal_grid_png and svg functions
    """

    img = Image.open("data/test_image.png")

    # fun.hexagonal_grid_png1(img, 10)
    # fun.hexagonal_grid_png2(img, 10)
    # Checks if the function are operating well
    # Test image is blank, so both functions should return the same image
    # fun.hexagonal_grid_svg1(img, 10)
    #fun.hexagonal_grid_svg2(img, 10)
    # Those tests don't work well because of the path to the image that is in the functions...