# !/usr/bin/python
from PIL import Image
import sys
import numpy as np

# help source : https://stackoverflow.com/a/3169874

target_color = (237, 28, 36) # RGB
replacement_color = (255, 255, 255) # RGB

source_file = "./test.png"
destination_file = "./dest.png"

# img = Image.open(sys.argv[1])
img = Image.open(source_file).convert('RGB')

data = np.array(img)
data[(data == target_color).all(axis = -1)] = replacement_color
img2 = Image.fromarray(data, mode='RGB')
img2.show()

img2.save(destination_file)
