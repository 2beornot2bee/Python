#myoop_game_own_design_map
from rooms import *


class Map(object):

    rooms={
        'dark_room':DarkRoom(),
        'green_room':GreenRoom(),
        'final_room':FinalRoom(),
        }

    def __init__(self,start_room):
        self.start_room=start_room


    def next_room(self,room_name):
        val = Map.rooms.get(room_name)
        return val
    def opening_room(self):
        return self.next_room(self.star_room)
