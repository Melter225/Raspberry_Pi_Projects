from sense_hat import SenseHat
sense = SenseHat()
import random
import numpy as np
from functools import lru_cache

blue = [0, 0, 255]
black = "black"
white = "white"
blackcolor = [0, 0, 0]
whitecolor = [255, 255, 255]
matrix = np.array([[]])


def generate():
    global matrix
    matrix = np.array([[black, black, black, black, black, black, black, black],
            [black, white, white, white, white, white, white, black],
            [black, black, black, black, black, black, black, black],
            [black, white, white, white, white, white, white, black],          
            [black, black, black, black, black, black, black, black],
            [black, white, white, white, white, white, white, black],
            [black, white, white, white, white, white, white, black],
            [black, black, black, black, black, black, black, black]])

    Flat = matrix.flatten()

    Flatcopy = []

    for i in range(64):
        if Flat[i] == "black":
            Flatcopy.append(blackcolor)
        
        else:
            Flatcopy.append(whitecolor)

    for i in range(6):
        Flatcopy[i+17] = blackcolor

    for i in range(6):
        Flatcopy[i+33] = blackcolor

    for i in range(2):
        randomplace = random.randint(17, 22)
        Flatcopy[randomplace] = whitecolor

    for i in range(2):
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

    sense.set_pixels(Flatcopy)

generate()

def pathFind():
    global matrix
    @lru_cache(maxsize=None)
    def dfs(r, c):
        if matrix[r][c] == "black" or r < 0 or c < 0 or r > 7 or c > 7 or matrix[r][c] == "blue":
            return
        
        matrix[r][c] = "blue"
        print(matrix[r][c])

        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c-1)
        dfs(r, c+1)

    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] == "white":
                dfs(row, column)
                continue

    PixelList = [item for sublist in matrix for item in sublist]
    PixelListCopy = []

    for i in PixelList:
        if i == "white":
            PixelListCopy.append(whitecolor)

        if i == "black":
            PixelListCopy.append(blackcolor)

        if i == "blue":
            PixelListCopy.append(blue)

    print(PixelListCopy)

    sense.set_pixels(PixelListCopy)

pathFind()