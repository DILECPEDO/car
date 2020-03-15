import random
import enum
from aenum import MultiValueEnum
import time
import os
import os
import sys
import tty
import threading
from queue import Queue 

try:
    import termios
except:
    import msvcrt

def get_random_road(road_width,):
    return [random.randint(0,3) for _ in range(road_width)]

# class status(enum.Enum): 
#     vuoto = 0
#     pieno = 1

class status(MultiValueEnum):
    vuoto = 0
    pieno = 1,2,3    

class direction(MultiValueEnum):
    right = "d" , "D"
    left = "a" , "A"


class griglia():
    def __init__(self,larghezza, altezza):
        self.larghezza = larghezza
        self.altezza = altezza
        self.structure = []
        self.puntatore = 0
        self.sleep_time = 1
        self.score = 0
    
    def create_grid(self):
        for _ in range(self.altezza):
            self.structure.append(get_random_road(self.larghezza) )
        # self.puntatore = self.structure.index(0)
        self.print()
    def print(self):
        for row in self.structure:
            for coluomn in row:
                if status(coluomn) == status.vuoto:
                    print("X", end="")
                else:
                    print(" ", end="")
            print()
    def next(self, direction ):
        direction = direction.get() 
        print("57")
        if direction == direction.left and self.puntatore > 0:
            self.puntatore -=1
        elif direction == direction.right and self.puntatore < self.larghezza:
            self.puntatore += 1
        else:
            print("porco dio")
        
        time.sleep(1/self.sleep_time)
        self.sleep_time += 0.05
        self.clear()
        self.score += 1
        self.structure.pop()
        self.structure.insert(0,get_random_road(self.larghezza))
        self.print()

    def clear(self):
        if os.name == 'nt': 
            os.system('cls') 
        else: 
            os.system('clear') 

def getch(sender):
    if os.name == 'nt':
        while True:
            sender.put(direction(msvcrt.getch()))
    else:
        while True:
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            sender.put(direction(ch))


griglia = griglia(4,6)
griglia.create_grid()
q= Queue()
threading.Thread(target=getch, args =(q, )).start()
while True:
    griglia.next(q)



