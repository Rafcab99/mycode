import random

# Define the player's attributes
player = {'name': 'Player', 'health': 100, 'attack': 10, 'defense': 5, 'current_room': 'hallway'}

# Define the enemy's attributes
enemy = {'name': 'Enemy', 'health': 50, 'attack': 5, 'defense': 2, 'current_room': 'hallway'}

# Define the rooms and their connections
rooms = {
    'hallway': {
        'description': 'You are in a dimly lit hallway. There are doors to the north, east, and west.',
        'connections': {'north': 'bedroom', 'east': 'kitchen', 'west': 'living room'}
    },
    'bedroom': {
        'description': 'You are in a bedroom. There is a bed, a dresser, and a window.',
        'connections': {'south': 'hallway'}
    },
    'kitchen': {
        'description': 'You are in a kitchen. There is a stove, a fridge, and a sink.',
        'connections': {'west': 'hallway'}
    },
    'living room': {
        'description': 'You are in a living room. There is a couch, a TV, and a coffee table.',
        'connections': {'east': 'hallway'}
    }
}

# Define a function for attacking
def attack(attacker, defender):
    damage = attacker['attack'] - defender['defense']
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
        if new_room == enemy['current_room']:
            print('You encounter the enemy!')
            return False
    else:
        print('You cannot go that way.')
    return True

# Start the game
print('Welcome to the RPG game!')
print(rooms[player['current_room']]['description'])
while True:
    command = input('What would you like to do? (attack/move) ')
    if command == 'attack':
        if not take_turn():
            break
    elif command == 'move':
        direction = input('Which direction would you like to go? (north/south/east/west) ')
        if not move(direction):
            break
    else:
        print('Invalid command.')

