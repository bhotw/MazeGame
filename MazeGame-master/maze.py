
mazeData = {}

######################
# Provided Functions #
######################

#Removes item from current space of the player
def remove_item_from_space():
  mazeData['maze'][mazeData['startY']][mazeData['startX']] = ' '

#Returns current space of the player ('X', ' ', 'K', 'D', etc.)
def get_current_space():
  global mazeData
  return mazeData['maze'][mazeData['startY']][mazeData['startX']]

#Returns what is in the direction provided ('up', 'down', 'left', 'right')
def look_in_direction(direction):
  global mazeData
  if direction == 'up':
    return mazeData['maze'][mazeData['startY'] - 1][mazeData['startX']]
  elif direction == 'down':
    return mazeData['maze'][mazeData['startY'] + 1][mazeData['startX']]
  elif direction == 'left':
    return mazeData['maze'][mazeData['startY']][mazeData['startX'] - 1]
  elif direction == 'right':
    return mazeData['maze'][mazeData['startY']][mazeData['startX'] + 1]
  return 'X'

def get_inventory():
  global mazeData
  return mazeData['inventory']

# Moves 'up', 'down', 'left', or 'right'
def move(direction):
  global mazeData
  if direction not in ['up', 'down', 'left', 'right']:
    print("Not a valid direction")
    return
  if direction == 'up':
    mazeData['startY'] -= 1
  elif direction == 'down':
    mazeData['startY'] += 1
  elif direction == 'left':
    mazeData['startX'] -= 1
  else:
    mazeData['startX'] += 1
  
# Given a maze and the coordinates of the player, print out the maze
def look_around():
  global mazeData
  maze = mazeData['maze']
  playerX = mazeData['startX']
  playerY = mazeData['startY']
  
  currentX = 0
  currentY = max(playerY - 1, 0)
  while currentY <= min(playerY + 1, len(mazeData['maze'])):
    line = maze[currentY]
    for character in line:
      if currentX == playerX and currentY == playerY:
        print("O", end=" ") 
      elif abs(currentX - playerX) <= 1 and abs(currentY - playerY) <= 1:
        print(character, end=" ")
      else:
        print(" ", end=" ")
      currentX = currentX + 1
    print()
    currentY = currentY + 1
    currentX = 0
  print()

# Print out the maze
def print_maze():
  global mazeData
  maze = mazeData['maze']
  playerX = mazeData['startX']
  playerY = mazeData['startY'
  ]
  currentX = 0
  currentY = 0
  for line in maze:
    for character in line:
      if currentX == playerX and currentY == playerY:
        print("O", end=" ") 
      else:
        print(character, end=" ")
      currentX = currentX + 1
    print()
    currentY = currentY + 1
    currentX = 0
  print()

# Given a file name, return a dictionary with the maze and coordinates of the start and end
def importFile(fileName):
  global mazeData
  # Open the file in 'read' mode
  file = open(fileName, 'r')
  
  # The data to be returned
  mazeData = {
      'maze': [],
      'startX': 0,
      'startY': 0,
      'endX': 0,
      'endY': 0,
      'inventory': []
  }
  
  # Extract the maze data from the opened file
  currentX = 0
  currentY = 0
  for line in file:
    mazeRow = []
    
    for character in line:
      # '\n' indicates the end of each line in the file and should be ignored
      if (character != "\n"):
        if (character == "B"):
          mazeData['startX'] = currentX
          mazeData['startY'] = currentY
          character = ' '
        elif (character == "D"):
          mazeData['endX'] = currentX
          mazeData['endY'] = currentY
        mazeRow.append(character)
      currentX = currentX + 1
    
    # Add the row to the maze data        
    mazeData['maze'].append(mazeRow)
    
    # Increment the y counter and reset the x counter for the next row
    currentY = currentY + 1
    currentX = 0

# Starts the maze game for the given file
def start_maze(file_name):
    importFile(file_name)
    print("Welcome to the maze!")
    print("You find yourself in an unfamiliar place. Hope you can find your way out.")