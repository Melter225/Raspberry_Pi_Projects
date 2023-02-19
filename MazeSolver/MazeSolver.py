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
matrixf = matrix.flatten()
print(matrixf)

matrixfcopy = []
matrixcopy = []

for i in range(64):
    if matrixf[i] == "black":
        matrixfcopy.append(blackcolor)
    
    else:
        matrixfcopy.append(whitecolor)

for i in range(6):
    matrixfcopy[i+17] = blackcolor

for i in range(6):
    matrixfcopy[i+33] = blackcolor

for i in range(1, 7):
    matrixcopy.append([i][random.randint(1, 7), whitecolor])

matrixf = matrixfcopy

sense.set_pixels(matrixfcopy)