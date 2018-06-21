import maze 
maze.start_maze("maze2.txt")
list_dir = [ "left", "right", "up", "down"]

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
def look():
	print ( maz_character_to_description[maze.get_current_space()])


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
		for s in maze.get_inventory():
			if s == "W":
				print ("You have killed the snake!")
				maze.get_inventory().remove(s)
		else:
			print ("you don't have anything to kill the snake with.")
	else:
		print ("there is no snake what the hack do you want me to kill?")
		
def bribe():
	curntLocation = maze.get_current_space()
	if curntLocation == "S":
		for c in maze.get_inventory():
			if c == "C":
				print ("you have bribed the snake!")
				maze.get_inventory().remove(c)
			else:
				print ("You don't have anything the bribe the snake")
	else:
		print ("there is no snake, dummy.")
	



while True :
	user_input = input("what is the next command master: ")
	if user_input == "look around":
		maze.look_around()
	elif user_input in list_dir:
		if check_valid_move(user_input):
			maze.move(user_input)
			maze.look_around()
		else:
			print("There is a wall! the player can not move.")
	elif user_input == "look":
		look()
	elif user_input == "pick up":
		add_to_inventory()
	elif user_input == "inventory":
		print(maze.get_inventory())
	elif user_input == "map":
		maze.print_maze()
	elif user_input == "open":
		if open_door() == False:
			break
	elif user_input == "kill":
		kill()
	elif user_input == "bribe":
		bribe()
		