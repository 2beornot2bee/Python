from random import randint
from design import *
class DarkRoom(Rooms):

    def entrance(self):
        print("""This is the dark room and you need to find light
                 to see the room and exit door.""")
        print("""There are three closed and one of them has the light""")
        print("""Which one does has the light?""")
        random_number= randint(1,3)
        door_number=input(">>>")
        if random_number == door_number:
            print("""Conrat you find the light. Go on.""")
            return 'green_room'
        else:
            print("""Go to the begining of the game and this time find the light""")
            return 'dark_room'  

class GreenRoom(Rooms):
    

    def entrance(self):
        print("""You are here but do not be happy.
                There are many dangerous creatures here to eat you up.""")
        print("""If you want to pass them you need the magic shoes to protect you""")
        print("""But you have to asnwer the question to deserve the shoes""")

        questions={"What is Galataray SC's establishment year?":"1905",
                   "What is Fenerbahce SC's establishment year?":"1907",
                   "What is Besiktas SC's establishment year?":"1903"}
        random_number= randint(1,3) ### hata olursa buraya bak
        question=questions[random_number]
        answer=input(">>>> ")

        if question==anwer:
            print("Yes you are righ go to next room")
            return 'final_room'
        else:
            print("No you have to start all over again")
            return 'green_room'


class FinalRoom(Rooms):

    def entrance(self):
        print("""You need to find a special key which can help you
                  to open last door for your famiy but you need to solve a problem """)
        print("""The problem is that what is 4+5/5""")
        answer =input(">>>> ")
        if answer=="5":
            print("You are with your family!!!")
            print("You finished the game")
            exit(1)
        else:
            print("sorry you have to to beginning...")
            return 'dark_room'
        

        

        
