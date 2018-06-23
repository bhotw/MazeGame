import maze 
maze.start_maze("maze2.txt")
list_dir = { 
	"a" : "left",
	"d" : "right",
	"w" : "up",
	"s" : "down"
	}

def check_valid_move(x):
	y = maze.look_in_direction(x)
	if y == "X":
		return False
	else:
		return True 

maz_character_to_description = {
	"X" : "a wall",
	"K" : "a key" ,
	" " : "open space",
	"D" : " a door",
	"S" : "a snake",
	"M" : "a map",
	"C" : "coin",
	"W" : "a sword"
}	



def direction():
	main_space = maze.get_current_space()
	for i in list_dir:
		if user_input == i:
			if check_valid_move(list_dir[i]):
				maze.move(list_dir[i])
				maze.look_around()
			else:
				print("There is a wall/!")

def look():
	print ( maz_character_to_description[maze.get_current_space()])

def maps():
	if "M" in maze.get_inventory():
			maze.print_maze()
	else:
		print ("you don't have a map!")


def add_to_inventory():
	currLoc = maze.get_current_space()
	if currLoc == "K":
		maze.get_inventory().append(currLoc)
		maze.remove_item_from_space()
		print ( "You have picked up a key!")
	elif currLoc == "M":
		maze.get_inventory().append(currLoc)
		maze.remove_item_from_space()
		print("You have picked up a map!")
	elif currLoc == "C":
		maze.get_inventory().append(currLoc)
		maze.remove_item_from_space()
		print ( "You have picked up a coin!")
	elif currLoc == "W":
		maze.get_inventory().append(currLoc)
		maze.remove_item_from_space()
		print ("You have picked up a sword!")
	else:
		print("You are so dumb, how do you pick up something when nothing is there?")

def open_door():
	curntLocation = maze.get_current_space()
	if curntLocation == "D":
		for n in maze.get_inventory():
			if n == "K":
				print("You have escaped!")
				return False
		else:
			print ("You stupid, how are you gonna open the door if you don't have a key?")
			return True
	else:
		print("There is no door what the hack do you want me to open? dumb...dumb...")
		maze.look_around()

def kill():
	curntLocation = maze.get_current_space()
	if curntLocation == "S":
		if "W" in maze.get_inventory():
			print ("You have killed the snake!")
			maze.get_inventory().remove("W")
			maze.remove_item_from_space()
		else:
			print ("you don't have anything to kill the snake. So you are dead")
			return False
	else:
		print ("there is no snake what the hack do you want me to kill?")
		
def bribe():
	curntLocation = maze.get_current_space()
	if curntLocation == "S":
		if "C" in maze.get_inventory():
			print ("you have bribed the snake!")
			maze.get_inventory().remove("C")
		else:
			print ("You don't have anything the bribe the snake")
	else:
		print ("there is no snake, dummy.")


	






while True :
	user_input = input("what is the next command master: ")
	if user_input == "look around":
		maze.look_around()
	elif user_input in list_dir:
		direction()
	elif user_input == "look":
		look()
	elif user_input == "e":
		add_to_inventory()
	elif user_input == "inventory":
		print(maze.get_inventory())
	elif user_input == "m":
		maps()
	elif user_input == "o":
		if open_door() == False:
			break
	elif user_input == "k":
		if kill() == False:
			break
	elif user_input == "b":
		bribe()
	
	
