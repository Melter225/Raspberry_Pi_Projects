from sense_hat import SenseHat
from random import randint
sense = SenseHat()

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

def pick_random_color():
	random_red = randint(0, 255)
	random_green = randint(0, 255)
	random_blue = randint(0, 255)
	return (random_red, random_green, random_blue)

sense.show_message("Testing", 0.05, pick_random_color())
