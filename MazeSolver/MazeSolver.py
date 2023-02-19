from sense_hat import SenseHat
sense = SenseHat()
import random
import numpy as np

blue = [0, 0, 255]
black = "black"
white = "white"
blackcolor = [0, 0, 0]
whitecolor = [255, 255, 255]

matrix = np.array([[black, black, black, black, black, black, black, black],
          [black, white, white, white, white, white, white, black],
          [black, black, black, black, black, black, black, black],
          [black, white, white, white, white, white, white, black],          
          [black, black, black, black, black, black, black, black],
          [black, white, white, white, white, white, white, black],
          [black, white, white, white, white, white, white, black],
          [black, black, black, black, black, black, black, black]])

matrix.flatten()
Flat = matrix.flatten()

Flatcopy = []
matrixcopy = []

for i in range(64):
    if Flat[i] == "black":
        Flatcopy.append(blackcolor)
    
    else:
        Flatcopy.append(whitecolor)

for i in range(6):
    Flatcopy[i+17] = blackcolor

for i in range(6):
    Flatcopy[i+33] = blackcolor

randomplace = random.randint(17, 22)
Flatcopy[randomplace] = whitecolor

randomplace2 = random.randint(33, 38)
Flatcopy[randomplace2] = whitecolor

for i in range(1):
    randomplace3 = random.randint(41, 46)
    Flatcopy[randomplace3] = blackcolor

for i in range(3):
    randomplace4 = random.randint(49, 54)
    Flatcopy[randomplace4] = blackcolor

Flat = Flatcopy

matrix = [Flat[i:i+8] for i in range(0, len(Flat), 8)]
for i in range(8):
    for j in range(8):
        if matrix[i][j] == [0, 0, 0]:
            matrix[i][j] = black
        else:
            matrix[i][j] = white

print(matrix)
sense.set_pixels(Flatcopy)