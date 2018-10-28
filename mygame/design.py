from sys import exit

class Rooms(object):

    def entrance(self):
        print("Bu sahne henüz hazır değil")
        print("Alt class yap be entrance()'i uygula ")
        exit(1)
        



def InitEngine(object):
    def __init__(self,room_map):
        self.room_map=room_map

    def action(self):
        current_room=self.room_map.openning_room()
        last_room=self.room_map.next_room('final_room')


        while current_room != last_room:
            next_room_name=current_room.entrance()
            current_room=self.room_map.next_room(next_room_name)

        current_room.entrance()



