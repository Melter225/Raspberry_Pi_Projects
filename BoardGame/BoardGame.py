from sense_hat import SenseHat
sense = SenseHat()
import random

#blue = ocean
#black = ship
#e, m, h = easy, medium, hard

blue = [0, 0, 255]
black = [0, 0, 0]
blackT = (0, 0, 0)
possible_colors = [
	[0,0,0],
	[20,20,10],
	[15,20,35],
	[135,20,34],
	[51,20,34],
	[32,51,0],
	[23,51,22],
	[20,15,0],
]
cached_items = []
matrix = [blue for i in range(64)]
sense.set_pixels(matrix)

placement = {
	"A1":[0,0],
	"A2":[0,1],
	"A3":[0,2],
	"A4":[0,3],
	"A5":[0,4],
	"A6":[0,5],
	"A7":[0,6],
	"A8":[0,7],
	"B1":[1,0],
	"B2":[1,1],
	"B3":[1,2],
	"B4":[1,3],
	"B5":[1,4],
	"B6":[1,5],
	"B7":[1,6],
	"B8":[1,7],
	"C1":[2,0],
	"C2":[2,1],
	"C3":[2,2],
	"C4":[2,3],
	"C5":[2,4],
	"C6":[2,5],
	"C7":[2,6],
	"C8":[2,7],
	"D1":[3,0],
	"D2":[3,1],
	"D3":[3,2],
	"D4":[3,3],
	"D5":[3,4],
	"D6":[3,5],
	"D7":[3,6],
	"D8":[3,7],
	"E1":[4,0],
	"E2":[4,1],
	"E3":[4,2],
	"E4":[4,3],
	"E5":[4,4],
	"E6":[4,5],
	"E7":[4,6],
	"E8":[4,7],
	"F1":[5,0],
	"F2":[5,1],
	"F3":[5,2],
	"F4":[5,3],
	"F5":[5,4],
	"F6":[5,5],
	"F7":[5,6],
	"F8":[5,7],
	"G1":[6,0],
	"G2":[6,1],
	"G3":[6,2],
	"G4":[6,3],
	"G5":[6,4],
	"G6":[6,5],
	"G7":[6,6],
	"G8":[6,7],
	"H1":[7,0],
	"H2":[7,1],
	"H3":[7,2],
	"H4":[7,3],
	"H5":[7,4],
	"H6":[7,5],
	"H7":[7,6],
	"H8":[7,7],
}

def place_in_range(p1, p2, length):
	while p1 not in placement:
		p1 = input("Enter valid starting position again:")

	while p2 not in placement:
		p2 = input("Enter valid ending position again:")

	x, y = 0, 0
	for i in range(placement[p1][0], placement[p2][0]):
		x += 1

	for i in range(placement[p1][1], placement[p2][1]):
		y += 1
	if x > 0 and y > 0:
		place_in_range("z0", "z1", length)
		return

	placeOnX = True if x > 0 else False

	if placeOnX:
		if x != length-1:
			place_in_range("z0", "z1", length)
			return
	else:
		if y != length-1:
			place_in_range("z0", "z1", length)
			return

	for i in range(placement[p1][0], placement[p2][0]+1):
		if sense.get_pixel(i, placement[p2][1]) == black or sense.get_pixel(i, y) == blackT:
			place_in_range("z0", "z1", length)
			return


	for i in range(placement[p1][1], placement[p2][1]+1):
		if sense.get_pixel(placement[p1][0], i) == black or sense.get_pixel(x, i) == blackT:
			place_in_range("z0", "z1", length)
			return

	for i in range(placement[p1][0], placement[p2][0]+1):
		sense.set_pixel(i, placement[p2][1], black)

	for i in range(placement[p1][1], placement[p2][1]+1):
		sense.set_pixel(placement[p1][0], i, black)

def generate_AI_board(p1, p2, length):
	values = [p1, p2]
	x, y = 0, 0
	for i in range(placement[p1][0], placement[p2][0]):
		x += 1

	for i in range(placement[p1][1], placement[p2][1]):
		y += 1
	if x > 0 and y > 0:
		values = chose_position_AI(length)

	placeOnX = True if x > 0 else False

	if placeOnX:
		if x != length-1:
			values = chose_position_AI(length)
	else:
		if y != length-1:
			values = chose_position_AI(length)

	for i in range(placement[p1][0], placement[p2][0]+1):
		if sense.get_pixel(i, placement[p2][1]) == black or sense.get_pixel(i, y) == blackT:
			values = chose_position_AI(length)

	for i in range(placement[p1][1], placement[p2][1]+1):
		if sense.get_pixel(placement[p1][0], i) == black or sense.get_pixel(x, i) == blackT:
			values = chose_position_AI(length)

	# print("starting point:", placement[values[0]])

	if values[0][1] == values[1][1]: 
		# i.e: D3 F3
		# X-axis
		# print("X AXIS:", placement[values[0]], placement[values[1]])
		print("X AXIS:", values[0],values[1])
		for i in range(placement[values[1]][0], placement[values[0]][0]+1):
			sense.set_pixel(i, placement[values[1]][1], black)

	else:
		# Y axis 
		print("Y AXIS:", values[0],values[1])
		for i in range(placement[values[0]][1], placement[values[1]][1]+1):
			sense.set_pixel(placement[values[0]][0], i, black)

def chose_position_AI(length):
	for i in range(length):
		value = random.choice(list(placement.keys()))
		voh = random.randint(0, 1)
		if voh == 0:
			endPoint = (value[0] + str(int(value[1]) + i - 1))
			# print("vertical" + value + endPoint)

		if voh == 1:
			new_letter = chr(ord(value[0]) - 1)
			endPoint = (new_letter + str(int(value[1])))
			# print("horizontal" + value + endPoint)

		while endPoint not in placement:
			value = random.choice(list(placement.keys()))
			if voh == 0:
				endPoint = (value[0] + str(int(value[1]) + i - 1))
				# print("vertical" + "regenerated" + value + endPoint)
			if voh == 1:
				new_letter = chr(ord(value[0]) - 1)
				endPoint = (new_letter + str(int(value[1])))  
				# print("horizontal" + "regenerated" + value + endPoint)
	return [value, endPoint]

def validate_position():
	for i in range(2, 6):
		value = random.choice(list(placement.keys()))
		voh = random.randint(0, 1)
		if voh == 0:
			endPoint = (value[0] + str(int(value[1]) + i - 1))
			# print("vertical" + value + endPoint)

		if voh == 1:
			new_letter = chr(ord(value[0]) - 1)
			endPoint = (new_letter + str(int(value[1])))
			# print("horizontal" + value + endPoint)


		while endPoint not in placement:
			value = random.choice(list(placement.keys()))
			if voh == 0:
				endPoint = (value[0] + str(int(value[1]) + i - 1))
				# print("vertical" + "regenerated" + value + endPoint)
			if voh == 1:
				new_letter = chr(ord(value[0]) - 1)
				endPoint = (new_letter + str(int(value[1])))  
				# print("horizontal" + "regenerated" + value + endPoint)
			
		generate_AI_board(value, endPoint, i)

validate_position()

mode = input("Chose a game mode: E, M, or H").lower()

def createboard(opt):
	if opt == "e":
		two_ship_first = input("Enter the starting point of your two ship:")
		two_ship_second = input("Enter the ending point of your two ship:")
		place_in_range(two_ship_first, two_ship_second, 2)
		three_ship_first = input("Enter the starting point of your three ship:")
		three_ship_second = input("Enter the ending point of your three ship:")
		place_in_range(three_ship_first, three_ship_second, 3)
		four_ship_first = input("Enter the starting point of your four ship:")
		four_ship_second = input("Enter the ending point of your four ship:")
		place_in_range(four_ship_first, four_ship_second, 4)
		five_ship_first = input("Enter the starting point of your five ship:")
		five_ship_second = input("Enter the ending point of your five ship:")
		place_in_range(five_ship_first, five_ship_second, 5)

def chose(opt):
	if opt == "e":
		createboard("e")

	if opt == "m":
		createboard("e")

	if opt == "h":
		createboard("e")

if mode == "e":
	chose("e")

if mode == "m":
	chose("m")

if mode == "h":
	chose("h")
