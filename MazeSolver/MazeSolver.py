#Error 2: ending point is faulty and sometimes does not show up
from sense_hat import SenseHat
sense = SenseHat()
import random
import numpy as np
from functools import lru_cache
from time import sleep

blue = [0, 0, 255]
black = "black"
white = "white"
blackcolor = [0, 0, 0]
whitecolor = [255, 255, 255]
matrix = np.array([[]])
red = [255, 0, 0]

def generate():
    global matrix
    matrix = np.array([[black, black, black, black, black, black, black, black],
            [black, red, white, white, white, white, white, black],
            [black, black, black, black, black, black, black, black],
            [black, white, white, white, white, white, white, black],
            [black, black, black, black, black, black, black, black],
            [black, white, white, white, white, white, white, black],
            [black, white, white, white, white, white, red, black],
            [black, black, black, black, black, black, black, black]])

    Flat = matrix.flatten()

    Flatcopy = []

    for i in range(64):
        if Flat[i] == "black":
            Flatcopy.append(blackcolor)

        elif Flat[i] == "white":
            Flatcopy.append(whitecolor)

        else:
            Flatcopy.append(red)

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

    #Flat = Flattened Edited Matrix
    Flat = Flatcopy

    matrix = [Flat[i:i+8] for i in range(0, len(Flat), 8)]
    for i in range(8):
        for j in range(8):
            if matrix[i][j] == [0, 0, 0]:
                matrix[i][j] = black
            elif matrix[i][j] == [255, 255, 255]:
                matrix[i][j] = white

    sense.set_pixels(Flatcopy)

generate()

def pathFind():
    global matrix
    @lru_cache(maxsize=None)
    def dfs(r, c):
        if matrix[r][c] == "black" or r < 0 or c < 0 or r > 7 or c > 7 or matrix[r][c] == "blue" or matrix[r][c] == red or matrix[r][c] == blackcolor or matrix[r][c] == blue:
            return

        matrix[r][c] = "blue"
        sense.set_pixel(c, r, blue)
        sleep(0.5)

        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c-1)
        dfs(r, c+1)

    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] == "white":
                dfs(row, column)
                break
pathFind()
