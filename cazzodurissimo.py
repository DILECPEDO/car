
# import os
# import msvcrt
# from time import sleep
# from random import randint

# class linea:
#     def __init__(self, A, B, C, D):
#         self._ = "|" +A +"|" +B +"|" +C +"|" +D +"|" +"\n"

# class autostrada:
#     def __init__(self, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15):
#         self.l1 = l1
#         self.l2 = l2
#         self.l3 = l3
#         self.l4 = l4
#         self.l5 = l5
#         self.l6 = l6
#         self.l7 = l7
#         self.l8 = l8
#         self.l9 = l9
#         self.l10 =l10
#         self.l11 =l11
#         self.l12 =l12
#         self.l13 =l13
#         self.l14 =l14
#         self.l15 =l15

#     def metti_blocco(self, colonna):
#         if colonna == 1:
#             return linea(1, "X", " ", " ", " ")       
#         if colonna == 2:
#             return linea(1, " ", "X", " ", " ")
#         if colonna == 3:
#             return linea(1, " ", " ", "X", " ")
#         if colonna == 4:
#             return linea(1, " ", " ", " ", "X")

# class veicolo:
#     def __init__(self, colonna, lunghezza, blocco):
#         self.colonna = randint(5)
#         self.lunghezza = randint(5)


# a = autostrada(linea(" "," "," "," ")._ ,linea(" "," "," "," ")._ ,linea(" "," "," "," ")._ ,linea(" "," "," "," ")._ ,linea(" "," "," "," ")._ ,linea(" "," "," "," ")._ ,linea(" "," "," "," ")._ ,linea(" "," "," "," ")._, linea(" "," "," "," ")._, linea(1," "," "," "," ")._, linea(1," "," "," "," ")._, linea(1," "," "," "," ")._, linea(1," "," "," "," ")._, linea(1," "," "," "," ")._, linea(1," "," "," "," ")._)



# immagine = a.l1 +a.l2 +a.l3 +a.l4 +a.l5 +a.l6 +a.l7 +a.l8 +a.l9 +a.l10 +a.l11 +a.l12 +a.l13 +a.l14 +a.l15
# linee = [a.l1, a.l2, a.l3, a.l4, a.l5, a.l6, a.l7, a.l8, a.l9, a.l10, a.l11,  a.l12, a.l13, a.l14, a.l15]
# print(immagine)
# a.l1 = a.metti_blocco(4)
# a.l9 = a.metti_blocco(2)
# a.l15 = a.metti_blocco(3)
# print(immagine)


# --------------------------------------------------------------- PEDO


# import random
# import enum
# from aenum import MultiValueEnum
# import time
# import os
# import os
# import sys
# import tty
# import threading
# from queue import Queue 

# try:
#     import termios
# except:
#     import msvcrt

# def get_random_road(road_width,):
#     return [random.randint(0,3) for _ in range(road_width)]

# # class status(enum.Enum): 
# #     vuoto = 0
# #     pieno = 1

# class status(MultiValueEnum):
#     vuoto = 0
#     pieno = 1,2,3    

# class direction(MultiValueEnum):
#     right = "d" , "D"
#     left = "a" , "A"


# class griglia():
#     def __init__(self,larghezza, altezza):
#         self.larghezza = larghezza
#         self.altezza = altezza
#         self.structure = []
#         self.puntatore = 0
#         self.sleep_time = 1
#         self.score = 0
    
#     def create_grid(self):
#         for _ in range(self.altezza):
#             self.structure.append(get_random_road(self.larghezza) )
#         # self.puntatore = self.structure.index(0)
#         self.print()
#     def print(self):
#         for row in self.structure:
#             for coluomn in row:
#                 if status(coluomn) == status.vuoto:
#                     print("X", end="")
#                 else:
#                     print(" ", end="")
#             print()
#     def next(self, direction ):
#         direction = direction.get() 
#         print("57")
#         if direction == direction.left and self.puntatore > 0:
#             self.puntatore -=1
#         elif direction == direction.right and self.puntatore < self.larghezza:
#             self.puntatore += 1
#         else:
#             print("porco dio")
        
#         time.sleep(1/self.sleep_time)
#         self.sleep_time += 0.05
#         self.clear()
#         self.score += 1
#         self.structure.pop()
#         self.structure.insert(0,get_random_road(self.larghezza))
#         self.print()

#     def clear(self):
#         if os.name == 'nt': 
#             os.system('cls') 
#         else: 
#             os.system('clear') 

# def getch(sender):
#     if os.name == 'nt':
#         while True:
#             sender.put(direction(msvcrt.getch()))
#     else:
#         while True:
#             fd = sys.stdin.fileno()
#             old_settings = termios.tcgetattr(fd)
#             try:
#                 tty.setraw(sys.stdin.fileno())
#                 ch = sys.stdin.read(1)
#             finally:
#                 termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#             sender.put(direction(ch))


# griglia = griglia(4,6)
# griglia.create_grid()
# q= Queue()
# threading.Thread(target=getch, args =(q, )).start()
# while True:
#     griglia.next(q)



# ------------------------------------------------------------------- PROGRAMMA VERO  


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

# class status(enum.Enum): 
#     vuoto = 0
#     pieno = 1

class status(MultiValueEnum):
    vuoto = 0
    pieno = 1,2,3,4    

class direction(MultiValueEnum):
    right = "d" , "D"
    left = "a" , "A"


def get_random_road(road_width,):
    return [random.randint(0,4) for _ in range(road_width)]
def common_member(a, b): 
    a_set = set(a) 
    b_set = set(b) 
    if (a_set & b_set): 
        return True 
    else: 
        return False

def getIndexPositions(listOfElements, element):
    indexPosList = []
    for i in range(len(listOfElements)): 
        if status(listOfElements[i]) == status(element):
            indexPosList.append(i)
    return indexPosList 
class griglia():
    def __init__(self,larghezza, altezza):
        self.larghezza = larghezza
        self.altezza = altezza
        self.structure = []
        self.puntatore = 0
        self.sleep_time = 1
        self.score = 0

    def create_grid(self):
        self.clear()
        for _ in range(self.altezza):
            self.structure.append(get_random_road(self.larghezza) )
    # self.puntatore = self.structure.index(0)

        self.print()
    def print(self):
        for row in self.structure:
            for coluomn in row:
                if status(coluomn) == status.vuoto:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
    def new_row(self):
        free_sport_1 = []
        free_sport_2 = []
        while not common_member(free_sport_1, free_sport_2):
            nuovariga = get_random_road(self.larghezza)
            free_sport_1 = [k for k in range(self.larghezza) if k not in getIndexPositions( nuovariga , 0)]
            free_sport_2 = [k for k in range(self.larghezza) if k not in getIndexPositions(self.structure[0],  0)]
        return nuovariga

    def next(self ):
        # direction = direction.get() 
        # print("57")
        # if direction == direction.left and self.puntatore > 0:
        #     self.puntatore -=1
        # elif direction == direction.right and self.puntatore < self.larghezza:
        #     self.puntatore += 1
        # else:
        #     print("porco dio")
        
        time.sleep(1/self.sleep_time)
        if self.score < 250:
            self.sleep_time += 0.02
        self.clear()
        self.score += 1
        # print("score: ", self.score, "\nvelocita: ", self.sleep_time )
        self.structure.pop()
        nuovariga = self.new_row()
        self.structure.insert(0,nuovariga)
        self.print()
        print("score: ", self.score)
    def clear(self):
        if os.name == 'nt': 
            os.system('cls') 
        else: 
            os.system('clear')

griglia = griglia(4,15)
griglia.create_grid()
while True:
    griglia.next()

# codice di fede sul trovare spazzi liberi consecutivi
        # while True:
        #     i = 0
        #     nuovariga = get_random_road(self.larghezza)   
        #     nuovariga_riga_vuoti = getIndexPositions(nuovariga, 0)
        #     seconda_riga_vuoti = getIndexPositions(self.structure[1], 0)
        #     for num1 in nuovariga_riga_vuoti:
        #         for num2 in seconda_riga_vuoti:
        #             if num1 == num2:
        #                 i += 1
        #                 print(i)
        #     if i != 0:
        #         break
            
        # self.structure.insert(0,nuovariga)