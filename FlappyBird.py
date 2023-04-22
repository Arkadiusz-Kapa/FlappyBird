import keyboard, os, random, time

#Zmienne globalne:
width, height = 200, 20
Bird_OY_Position = height // 2


#Budowa Ptaka/ gracza:

class Bird():
    
    def D_Bird(self, x ,y):
        Bird_OY_Position = y
        face = '>'
        body = '[]'