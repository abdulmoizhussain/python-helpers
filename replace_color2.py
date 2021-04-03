# !/usr/bin/python
from PIL import Image
import sys
import numpy as np

# source how to add requirements file: https://blog.usejournal.com/why-and-how-to-make-a-requirements-txt-f329c685181e
# TL;DR: $ pip freeze > requirements.txt
# help source : https://stackoverflow.com/a/765829

target_color = (127, 127, 127, 255)  # RGBA
replacement_color = (255, 255, 255, 255)  # RGBA

source_file_name = "./test.png"
destination_file_name = "./dest.png"

img = Image.open(source_file_name)
img = img.convert("RGBA")

pixdata = img.load()

width, height = img.size
for y in range(height):
    for x in range(width):
        if pixdata[x, y] == target_color:
            pixdata[x, y] = replacement_color

img.save(destination_file_name, "PNG")
