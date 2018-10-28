from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print ("This scene is not yet configured. Subclass it and implement enter().")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "You died.  You kinda suck at this.",
         "Your mom would be proud...if she were smarter.",
         "Such a luser.",
         "I have a small puppy that's better at this."
    ]

    def enter(self):
        print ("ee")
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print ("ee")
       

        action = raw_input("> ")

        if action == "shoot!":
            print ("ee")
          
            return 'death'

        elif action == "dodge!":
            print ("ee")
            return 'death'

        elif action == "tell a joke":
            print ("ee")
            return 'laser_weapon_armory'

        else:
            print ("ee")
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print ("ee")
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
           print ("ee")
           guesses += 1
           if guesses == 10:
              break
           print ("ee"), guesses
           guess = input("[keypad]> ")

        if guess == code:
            print ("ee")
            return 'the_bridge'
        else:
            print ("ee")
            return 'death'



class TheBridge(Scene):

    def enter(self):
        print ("ee")

        action = input("> ")

        if action == "throw the bomb":
            print ("ee")
            return 'death'

        elif action == "slowly place the bomb":
            print ("ee")
            return 'escape_pod'
        else:
            print ("ee")
            return "the_bridge"


class EscapePod(Scene):

    def enter(self):
        print ("ee")

        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")


        if int(guess) != good_pod:
            print ("ee")
            return 'death'
        else:
            print ("ee")

            return 'finished'

class Finished(Scene):

    def enter(self):
        print ("ee")
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('laser_weapon_armory')
a_game = Engine(a_map)
a_game.play()
