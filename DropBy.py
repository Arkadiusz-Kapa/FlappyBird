import keyboard, os, random, time

#This kinda looks like obfuscated code lol
#Zmienne globalne:
width, height = 10, 20 #ustawienie wysokości i szerokości
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



class Ball():
    def D_Ball(self, x, y):
        global Ball_OX, gameBoard
        Ball_OX = x
        body = "█"
        for i in range(y, y+3):
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
    collision=endGame = False
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
            t0 =time.time()
            while(time.time()-t0 < f_time):
                                                            
                if keyboard.is_pressed('a'):
                    ball.Move(-1)
                    os.system("cls")
                    game.printFrame()
                    break
                if keyboard.is_pressed('d'):
                    ball.Move(1)
                    os.system("cls")
                    game.printFrame()
                    break 
            wait = round(time.time()-t0, 1)                  
                    
            time.sleep(f_time-wait)

        if(collision):                                       #sprawdzenie, czy w trakcie gry doszło do kolizji między ptakiem a rurami, jeśli tak, wyświetla stosowny komunikat
            print("\nPrzegrales!")
        userIn = input("\nNapisz \"end\" aby zakonczyc lub wpcisnij \"eneter\" aby zagrac jeszcze raz\n")
        if("end" in userIn):              #jeśli użytkownik wprowadził "end" na wejściu, ustawia wartość 'endGame' na True, co spowoduje zakończenie gry
            endGame = True      
        else:                             #jeśli użytkownik wprowadził cokolwiek innego, ustawia wartości 'collision'i endGame na False, co umożliwi ponowne uruchomienie gry
            collision = endGame = False 
if __name__ == '__main__':
    main()           #wywołanie funkcji 'main'