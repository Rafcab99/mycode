import random

# Define the player's attributes
player = {'name': 'Player', 'health': 100, 'attack': 5, 'defense': 5, 'current_room': 'hallway', 'weapon': None}

# Define the enemy's attributes
enemy = {'name': 'Enemy', 'health': 75, 'attack': 5, 'defense': 5, 'current_room': 'living room'}

# Define the rooms and their connections
rooms = {
    'hallway': {
        'description': 'You are in a dimly lit hallway. There are doors to the north, east, and west.',
        'connections': {'north': 'bedroom', 'east': 'kitchen', 'west': 'living room'},
        'weapon': {'name': 'Sword', 'attack': 2}
    },
    'bedroom': {
        'description': 'You are in a bedroom. There is a bed, a dresser, and a window.',
        'connections': {'south': 'hallway'},
        'weapon': {'name': 'Axe', 'attack': 3}
    },
    'kitchen': {
        'description': 'You are in a kitchen. There is a stove, a fridge, and a sink.',
        'connections': {'west': 'hallway'},
        'weapon': {'name': 'Dagger', 'attack': 1}
    },
    'living room': {
        'description': 'You are in a living room. There is a couch, a TV, and a coffee table.',
        'connections': {'east': 'hallway'},
        'weapon': {'name': 'Mace', 'attack': 4}
    }
}

# Define a function for attacking
def attack(attacker, defender):
    damage = random.randint(1, 20) + attacker['attack'] - defender['defense']
    if damage < 0:
        damage = 0
    defender['health'] -= damage
    print(attacker['name'], 'attacks', defender['name'], 'for', damage, 'damage!')

# Define a function for taking a turn
def take_turn():
    # Decide who attacks first
    if random.randint(0, 1) == 0:
        attack(player, enemy)
        if enemy['health'] <= 0:
            print(player['name'], 'wins!')
            return False
        attack(enemy, player)
        if player['health'] <= 0:
            print(enemy['name'], 'wins!')
            return False
    else:
        attack(enemy, player)
        if player['health'] <= 0:
            print(enemy['name'], 'wins!')
            return False
        attack(player, enemy)
        if enemy['health'] <= 0:
            print(player['name'], 'wins!')
            return False
    return True

# Define a function for moving to a different room
def move(direction):
    current_room = player['current_room']
    if direction in rooms[current_room]['connections']:
        new_room = rooms[current_room]['connections'][direction]
        player['current_room'] = new_room
        print(rooms[new_room]['description'])
        #if new_room == enemy['current_room']:
         #   print('You encounter the enemy!')
          #  answer = input('Would you like to attack?: y/n')
           # if answer = 'y':
            #    take_turn()
            #else:

            #return False
        if 'weapon' in rooms[new_room]:
            weapon = rooms[new_room]['weapon']
            print('You found a', weapon['name'], 'with attack bonus', weapon['attack'])
            if player['weapon'] is None or player['weapon']['attack'] < weapon['attack']:
                player['weapon'] = weapon
    else:
        print("You cannot go that way")

def move_enemy():
    current_room = enemy['current_room']
    possible_directions = list(rooms[current_room]['connections'].keys())
    direction = random.choice(possible_directions)
    new_room = rooms[current_room]['connections'][direction]
    enemy['current_room'] = new_room
    print('The enemy moves', direction, 'to', new_room)
    if new_room == player['current_room']:
        print('You encounter the enemy!')
        answer = input('Would you like to attack?: y/n ')
        while answer == 'y':
            take_turn()
            break
        else:
            move(command)
        return False
    return True

# Start the game
print('Welcome to Raf\'s RPG game!')

# Main game loop
while True:
    # Print the current room's description
  #  print(rooms[player['current_room']]['description'])

    # Check if there is an enemy in the room
   # if player['current_room'] == enemy['current_room']:
    #    print('You encounter the enemy!')
     #   while True:
            # Take a turn
      #      if not take_turn():
       #         break

    # Ask the player what they want to do
    command = input('\nWhat would you like to do? ')

    # Process the player's command
    if command in ['north', 'south', 'east', 'west']:
        move(command)
        move_enemy()
    elif command == 'status':
        print('Name:', player['name'])
        print('Health:', player['health'])
        print('Attack:', player['attack'])
        print('Defense:', player['defense'])
        if player['weapon'] is not None:
            print('Weapon:', player['weapon']['name'], '(attack:', player['weapon']['attack'], ')')
    elif command == 'quit':
        break
    elif command == 'stay':
        move_enemy()
    else:
        print('Invalid command.')


