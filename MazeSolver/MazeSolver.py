from sense_hat import SenseHat
sense = SenseHat()
import random

blue = [0, 0, 255]
black = [0, 0, 0]
white = [255, 255, 255]

matrix = [black, black, black, black, black, black, black, black,
          black, white, white, white, white, white, white, black,
          black, white, white, white, white, white, white, black,
          black, white, white, white, white, white, white, black,          
          black, white, white, white, white, white, white, black,
          black, white, white, white, white, white, white, black,
          black, white, white, white, white, white, white, black,
          black, black, black, black, black, black, black, black]

for i in range(5):
    random_value = random.randint(1, 2)
    if random_value == 1:
        matrix[i+17] = black

    if random_value == 2:
        matrix[i+17] = white

sense.set_pixels(matrix)