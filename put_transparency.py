# !/usr/bin/python
from PIL import Image
import sys
import numpy as np

# help source : https://stackoverflow.com/a/765829

target_color = (237, 28, 36, 255) # RGBA

source_file_name = "./test.png"
destination_file_name = "./dest.png"

img = Image.open(source_file_name)
img = img.convert("RGBA")

pixdata = img.load()

width, height = img.size
for y in range(height):
    for x in range(width):
        if pixdata[x, y] == target_color:
            pixdata[x, y] = (255, 255, 255, 0)

img.save(destination_file_name, "PNG")
