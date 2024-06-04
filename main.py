# Imports
from PIL import Image
import numpy as np
import math

# Variables
ASCIIscale = list('.:-=+o*#%$@B&8WM')
resolution = len(ASCIIscale)

# Preprocessing: 
# Load image, resize, grayscale and convert to numpy array
image = Image.open('image.png')

width, height = image.size
sw = 140
sh = (height*sw)/width*(8/12)*0.6
image = image.resize((int(sw), int(sh)))

grayscale = image.convert('L')
matrix = np.array(grayscale)

# Scaling:
# Switch each value for its associated ASCII character an append to text file
rows = np.shape(matrix)[0]
columns = np.shape(matrix)[1]

with open('image.txt', 'w') as text:
    for i in range(rows):
        for j in range(columns):
            a = matrix[i][j] # get current element
            asc = math.floor(a/resolution) # element to ascii
            text.write(str(ASCIIscale[asc]))
        text.write("\n")

# Prints out Image to Terminal
with open('image.txt', 'r') as file:
    for line in file:
        print(line, end='') 


