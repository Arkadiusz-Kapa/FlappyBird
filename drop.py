import keyboard, os, random, time

#Zmienne globalne:
width, height = 10, 100 #ustawienie wysokości i szerokości
Ball_OX = width // 2
PlankSplitsQueue = []
gameBoard = [[0 for x in range(width)] for y in range(height)]
collision = False
firstPlankPos = score = 0


class Game():
    def Plank(self,Ball_OY, split):
        for i in range(width):
            if(not(split-3 <= i <= split)):
                gameBoard[i][Ball_OY]= "@"
                if(Ball_OY+1 < width):
                    gameBoard[i][Ball_OY+1] = '@'
                    if(Ball_OY+2 < width): 
                        gameBoard[i][Ball_OY+2] = '-'

    def StartGame(self):
        global firstPlankPos, PlankSplitsQueue
        for i in range(height):
            for j in range(width):
                gameBoard[i][j] = "-"
        
        firstPlankPos = 10
        for i in range (10, 100 , 10):
            split = random.randint(4,8)
            PlankSplitsQueue.append= split
            ThisPlank = Game()
            ThisPlank.Plank(i,split)
    def printFrame(self):
        for i in range(height):
            res = " "
            for j in range(width):
                res += gameBoard[i][j]    
            print(res)

class Ball():
    def D_Ball(seld, x, y):
        global Ball_OY
        Ball_OY = y

class main():
        while True:
            Game.startGame()
            Game.printFrame
        while(time.time()-t0 < f_time):
                                                       
            if keyboard.is_pressed('w'):
                page +=1
                print("             current page: " + str(page) +"                 <= s or w =>")
                break
            if keyboard.is_pressed('s'):
                page -=1
                print("             current page: " + str(page) +"                 <= s or w =>")
                break 

if __name__ == '__main__':
    main()           #wywołanie funkcji 'main'        