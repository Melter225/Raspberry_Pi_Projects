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

randomplace = random.randint(17, 22)
matrixfcopy[randomplace] = whitecolor

randomplace2 = random.randint(33, 38)
matrixfcopy[randomplace2] = whitecolor

for i in range(1):
    randomplace3 = random.randint(41, 46)
    matrixfcopy[randomplace3] = blackcolor

for i in range(3):
    randomplace4 = random.randint(49, 54)
    matrixfcopy[randomplace4] = blackcolor

matrixf = matrixfcopy

sense.set_pixels(matrixfcopy)