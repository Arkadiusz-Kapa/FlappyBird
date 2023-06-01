import keyboard, os, random, time

#Zmienne globalne:
width, height = 10, 40 #ustawienie wysokości i szerokości
Ball_OX = width // 2
PlankSplitsQueue = []
gameBoard = [[0 for x in range(width)] for y in range(height)]
collision = False
firstPlankPos = score = 0


class Game():
    def Plank(self,Ball_OY, split):
        for i in range(width):
            if(not(split-3 <= i <= split)):
                gameBoard[Ball_OY][i]= "@"
                if(Ball_OY+1 < height): 
                    gameBoard[Ball_OY+1][i] = '-'

    def StartGame(self):
        global firstPlankPos, PlankSplitsQueue
        for i in range(height):
            for j in range(width):
                gameBoard[i][j] = "-"
        
        firstPlankPos = 5
        for i in range (5, 40 , 5):
            split = random.randint(4,8)
            PlankSplitsQueue.append(split)
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
        global Ball_OX
        Ball_OX = x//2
        body = "█"
        for i in range(y, y+2):
            for j in range (width):
                c1= gameBoard[i][j]
                if body == c1:
                    gameBoard[i][j] = "-"
        c1 = gameBoard[i][j]
        pole = '@'
        if c1 == pole:
            global colision
            colision = True
        MainBody = "█"
        gameBoard[i][j] = MainBody
    
    def Gravity(self):
        dropBy = 1
        Ball = Ball()
        Ball.D_Ball(Bird_OY+dropBy, 5)



class main():
    global collison, score
    endGame = False
    frames = 1
    f_time = 0.2
    while not endGame:
        score = 0
        Ball = Ball()
        Game = Game()
        Game.StartGame()
        Ball.D_Ball(Ball_OX, 2)
        Game.printFrame()
        while (not collision and not endGame):
            #os.system('cls')
            frames +=1
            if frames == 1000:
                frames = 1
            t0 =time.time()
            while(time.time()-t0 < f_time):
                                                            
                if keyboard.is_pressed('a'):
                    Ball_OX +=1
                    break
                if keyboard.is_pressed('d'):
                    Ball_OX -=1
                    break 
            wait = round(time.time()-t0, 1)                  
                    
            time.sleep(f_time-wait)

if __name__ == '__main__':
    main()           #wywołanie funkcji 'main'        