import keyboard, os, random, time

#Zmienne globalne:
width, height = 200, 20 #ustawienie wysokości i szerokości
Bird_OY_Position = height // 2
pipeSplitsQueue = []
gameBoard = [[0 for x in range(w)] for y in range(h)]
collision = False

class Game():
    def Pipe(self,OX_position, spli): #Funkcja rysująca rure
        for i in range(height): # petla w zakresie do zmiennej height (wazne aby nei bylo tam stalej liczby a zmienna jesli chcemy latwiej zmieniac wielkosc ekranu gry)
            if(not(split-3 <= 1 <= split))


#Budowa Ptaka/ gracza:

class Bird():
    
    def D_Bird(self, x ,y):
        global Bird_OY_Position = y
        face = '>'
        body = '[]'