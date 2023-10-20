# Project - Refresher in Computer science

![The basic wallpaper](https://github.com/olithub/RCS_project/blob/main/data/wallpaper.jpg?raw=true)

## Description

We want to develop a Python application that reads the above picture (as a .png file) in a low resolution, to generate a scalable version (as a .svg file) that can be used as a high-resolution wallpaper for your computer. To do so, we intend to sample the colors of each hexagone to reproduce the same picture.

We are expected to use and apply all the skills we acquired in the context of this module (including Git, Python and their ecosystem).

The steps we need to cover are:

- Load the input picture using Image.open(INPUT_FILENAME) from the [PIL](https://he-arc.github.io/livre-python/pillow/index.html) library,
- Iterate through the pixels of the input image using an [hexagonal grid](https://www.redblobgames.com/grids/hexagons/)
- [Sample the color](https://www.geeksforgeeks.org/python-pil-getpixel-method/) of each hexagone (by iterating over a tens of pixels per hexagone)
- Create an [SVG hexagon](https://www.tutorialscampus.com/html5/svg-draw-hexagon.htm) with the average color sampled from input file
- Write the resulting output picture in as an .svg file using functions like:
    with open('output.svg', 'w') as f:
        f.write(svg_content)

Once we are able to reproduce the above picture, we can try to:

- Read any input picture (with any size/resolution) to generate its “hexagonal” wallpaper,
- Play around with the size of the hexagons to adjust the output rendering,
- Replace hexagon grid sampling by triangles,
- Generate any hexagon / triangle wallpaper from input color pallets and color distribution function.

In the end we got this image !

![Our beautiful wallpaper](https://github.com/olithub/RCS_project/blob/main/data/wallpaper_10_hexagonal_grid2.png?raw=true)

## Quality of our code

![Coverage](https://github.com/olithub/RCS_project/blob/main/coverage.svg?raw=true)
