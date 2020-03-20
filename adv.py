from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

class Traversal_Graph:
    def __init__(self):
        self.rooms = {}
    
    def add_room(self, room):
        if room not in self.rooms:
            

    def traverse_rooms(self, room, player, visited=None, path=None):
        reverse = {'n':'s', 's':'n', 'e':'w', 'w':'e'}
        # Instantiate an empty set for visited rooms
        if visited is None:
            visited = set()
        # Instantiate an empty list to track traversal path
        if path is None:
            path = []
        # Add the first room to visited
        visited.add(player.current_room.id)
        # If we have visited all of the rooms, return path
        if len(visited) == 500:
            return path
        # Check available directions to move
        for direction in player.current_room.get_exits():
            # Update the player's current room to the available rooms in each direction
            player.current_room = player.current_room.get_room_in_direction(direction)
            # If room has not been visited...
            if player.current_room.id not in visited:
                # Create a new path and call traverse_rooms on the player's new current room
                new_path = self.traverse_rooms(player.current_room, visited, path)
                if new_path:
                    path = [direction] + new_path + reverse[direction]
                else:
                    new_path = [direction, reverse[direction]]
        # If path or new_path are not returned, return None
        return None

traversal_path = traverse_rooms(player.current_room, player)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
