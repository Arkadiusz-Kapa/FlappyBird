import keyboard, os, random, time
width, height = 10, 20
Ball_OX = width // 2
Ball_OY = 2
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
        for i in range (5, 20 , 5):
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
    def Del_Plank(self, Ball_OY):
        for j in range(width):
            gameBoard[Ball_OY][j] = "-"

    def updatePlanks(self, frames):
        if frames % 3 == 0:
            global firstPlankPos
            firstPlankPos -= 1
            if firstPlankPos < 0:
                Plank = Game()
                Plank.Del_Plank(firstPlankPos+1)
                firstPlankPos += 5
                PlankSplitsQueue.pop(0)
            c = 0
            for i in range(firstPlankPos, height , 5):
                Plank = Game()
                if(c < len(PlankSplitsQueue)):
                    Plank.Plank(i, PlankSplitsQueue[c])
                else:
                    split = random.randint(4, 8)
                    PlankSplitsQueue.append(split)
                    Plank.Plank(i, split)
                c += 1
    def info(self):
        print(" e => koniec")
        print("press /a/ and /d/ to move")     

class Ball():
    def D_Ball(self, x, y):
        global Ball_OX, gameBoard
        Ball_OX = x
        body = "█"
        for i in range(y, y+1):
            for j in range (width):
                c1= gameBoard[i][j]
                if body == c1:
                    gameBoard[i][j] = "-"
        c1 = gameBoard[y][x]
        pole = '@'
        if c1 == pole:
            global collision
            collision = True
        MainBody = "█"
        gameBoard[Ball_OY][Ball_OX] = MainBody
        
    def Gravity(self):
        dropBy = 1
        ball = self
        ball.D_Ball(Ball_OX,Ball_OY+dropBy)

    def Move(self, d):    
        global Ball_OX 
        move_by = d       
        ball = self    
        if(Ball_OX > width): return
        Ball_OX += move_by
        ball.D_Ball(Ball_OX, 2)

ball = Ball()

class main():
    global collison, ball
    endGame = False
    game = Game()
    game.StartGame()
    ball.D_Ball(Ball_OX, 2)
    frames = 1
    f_time = 0.2
    while not endGame:
        score = 0
        game.printFrame()
        while (not collision and not endGame):
            os.system('cls')
            if True:
                ball.Gravity()
            game.updatePlanks(frames)         
            game.printFrame()
            frames +=1
            if frames == 1000:
                frames = 1
            game.info()
            t0 =time.time()
            while(time.time()-t0 < f_time):
                                                            
                if keyboard.is_pressed('a'):
                    ball.Move(-1)
                    os.system("cls")
                    game.printFrame()
                    game.info()
                    break
                if keyboard.is_pressed('d'):
                    ball.Move(1)
                    os.system("cls")
                    game.printFrame()
                    game.info()
                    break 
                elif keyboard.is_pressed('e'):
                    endGame = True
                    break 
            wait = round(time.time()-t0, 1)                  
                    
            time.sleep(f_time-wait)

        if(collision):
            print("\nPrzegrales!")
        userIn = input("\nNapisz \"end\" aby zakonczyc lub wpcisnij \"eneter\" aby zagrac jeszcze raz\n")
        if("end" in userIn):
            endGame = True      
        else:
            collision = endGame = False 
if __name__ == '__main__':
    main()