import keyboard, os, random, time

#Zmienne globalne:
width, height = 100, 10 #ustawienie wysokości i szerokości
Bird_OY_Position = height // 2
pipeSplitsQueue = []
gameBoard = [[0 for x in range(width)] for y in range(height)]
collision = False
firstPipePos = score = 0

class Game():
    def Pipe(self,OX_position, split):  #Funkcja rysująca rure
        for i in range(height):     # petla w zakresie do zmiennej height (wazne aby nei bylo tam stalej liczby a zmienna jesli chcemy latwiej zmieniac wielkosc ekranu gry)
            if(not(split-3 <= i <= split)):
                gameBoard[i][OX_position]= "#"
                if(OX_position+1 < width):  #jeżeli zmienna jest mniejsza niż wysokość, to do elementu gameBoard[i][xpos+1] przypisywany jest znak '#' o takim samym kolorze jak wcześniej
                    gameBoard[i][OX_position+1] = '#'
                    if(OX_position+2 < width):  #jeżeli zmienna jest mniejsza niż wysokość to do elementu gameBoard[i][xpos+2] przypisywany jest znak '-' 
                        gameBoard[i][OX_position+2] = '-' if (i < 8) else '=' #jeżli i>= 8 zostanie użyty znak '=' 
    def Pipe_del(self, OX_position):
            for i in range(height):
                gameBoard[i][OX_position] = '-'if (i < 8) else '='  #ustawia wartość elementu gameBoard[i][xpos] w zależności od zmiennej i używany jest znak '-' lub znak '='
                gameBoard[i][OX_position+1] = '-'if (i < 8) else '=' #ustawia analogicznie element gameBoard[i][xpos+1]
    
    def startGame(self):
     #funkcja startująca gre
        global firstPipePos, pipeSplitsQueue  #inicjalizacja globalnych zmiennych jako puste listy (firstPipePos będzie póżniej używane do przechowywania pozycji pierwszej rury
        pipeSplitsQueue = [] #lista służąca do przechowywania kolejki podziałów rur
        for i in range(height): 
            for j in range(width):
                gameBoard[i][j] ='-' if (i < 8) else '=' #iterator i iteruje po wszystkich elementach planszy, każdy element ustawiany jest na odpowiedni kolor
        firstPipePos = 15   #ustawienie pozycji pierwszej rury na 15  
        for i in range(15, 100, 15): #ustawianie pozycji innych rur co 15
            split = random.randint(5, 8)  #każda rura ma losową wartość split
            pipeSplitsQueue.append(split) #lista kolejek kolejnych rur jest wypełniana losowymi wartościami split <5,8>
            thisPipe = Game()#dla każdej rury tworzony jest obiekt klasy Game() a następnie wywoływana metoda drawPipe, która rysuje rurę na planszy. Metoda drawPipe przyjmuje dwa argumenty (pozycję rury(i) oraz split)
            thisPipe.Pipe(i, split)

    def printFrame(self): #funkcja ma na celu wyświetlić ramkę planszy gry na ekranie
        for i in range(height):
            res = ""      #dla każdej iteracji zmienna res jest inicjowana jako pusty łańcuch znaków
            for j in range(width):
                res += gameBoard[i][j] #w każdej iteracji pętli , wartość gameBoard[i][j] jest dodawana do łańcucha znaków res
            print(res) #po zakończeniu pętli całość planszy drukowana jest na ekranie
    def updatePipes(self, frames): #funckja ta jest odpowiedzialna za aktualizowanie rur w grze            
        
        if(frames % 3 == 0): #instrukcja if sprawdza, czy liczba ramek jest podzielna przez 3 za pomocą operatora modulo. Jeśli tak, to pozycja pierwszej rury jest zmniejszana o 1
            global score
            global firstPipePos
            firstPipePos -= 1  
                                                             
            if(firstPipePos == 5): #jeżeli pozycja rury wyniosła 5, to wynik gracza jest zwiększany o 1
                score += 1
            if(firstPipePos < 0):                       #Jeśli pozycja pierwszej rury jest mniejsza niż 0, oznacza to, że rura zniknęła z ekranu i należy ją usunąć. 
                                                        #Funkcja tworzy nową instancję klasy Game i wywołuje metodę deletePipe w celu usunięcia rury, która zniknęł z ekranu. 
                                                        # Pozycja pierwszej rury jest następnie zwiększana o 15, a pierwszy podział w kolejce podziałów dla nowych rur jest usuwany.
                thisPipe = Game()
                thisPipe.Pipe_del(firstPipePos+1)
                firstPipePos += 15
                pipeSplitsQueue.pop(0)
            c = 0
            for i in range(firstPipePos, width , 15): #pętla for przechodzi przez wszytkie pozycje na planszy pomiędzy pierwszą rurą a końcem planszy zdefiniowanej jako 'w'
                thisPipe = Game()  #dla każdej pozycji na planszy, tworzony jest nowy obiekt 'Game'
                if(c < len(pipeSplitsQueue)):   #sprawdzane jest czy istnieje już kolejka podziałów rury o odpowiedniej długości, w której są zapisane wyniki losowania z funkcji 'drawPipe'
                    thisPipe.Pipe(i, pipeSplitsQueue[c]) #jeśli istnieje, to rysujemy rure na bieżącej planszy, korzystając z podziau rury, który znajduje się w 'pipeSplitsQueue[c]'
                else: #w przeciwnym razie losujemy nowy podział rury i dodajemy go do kolejki, a następnie rysujemy rurę z tym podziałem 
                    split = random.randint(5, 8)
                    pipeSplitsQueue.append(split)
                    thisPipe.Pipe(i, split)
                c += 1 #zwiększamy wartość licznika c o 1, aby przejść do następnego podziału rury z kolejki podziałów rury

#Budowa Ptaka/ gracza:

class Bird():
    
    def D_Bird(self, x ,y):
        global Bird_OY_Position
        Bird_OY_Position = y
        face = '>'
        body = '[]'
        for i in range(height): #pętla for iterująca przez cała wysokość - 1
            for j in range(x, x+3):  #pętla for iterująca od wartości x do wartości x + 3
                coor = gameBoard[i][j] #utworzenie zmiennej 'coor' i nadanie jej wartości 'gameBoard[i][j]'
                if(coor == body or coor == face): #sprawdzenie czy któryś z elementów ptaka jest równy z 'coor' 
                    gameBoard[i][j] = '-' if (i < 8) else '=' #jeżeli tak to przypisuje 'gameBoard[i][j]' nową wartość 
        coor = gameBoard[y][x]
        right = gameBoard[y][x+1]
        twoR = gameBoard[y][x+2]
        pole = '#'

        if(coor == pole or right == pole or twoR == pole): #sprawdzenie czy ptak nie udeżył w rure ,jeżeli tak to kolizje ustawiamy na 'True"
            global collision
            collision = True

        mainBody = '[]'
        gameBoard[y][x] = mainBody            
        gameBoard[y][x+1] = '>'  
    def jump(self):     #zdefiniowanie funkcji 'jump'
        
        raise_by = 0        #inicjacja zmiennej 'raiseby' na 0, zmienna ta określa, o ile pikseli zostanie przesunięty ptak w górę w wyniku skoku
        if(Bird_OY_Position > 1):  #sprawdza, czy bieżąca pozycja ptaka jest większa niż 1, jest to potrzebne, ponieważ nie chcemy, aby pt ak skakał poza górną granicę okna gry
            raise_by = 1    #jeśli bieżąca pozycja ptaka jest większa niż 1, to zmienna raiseby zostaje ustawiona na 1, co oznacza, że ptak zostanie przesunięty o 1 piksel w górę
        bird = Bird()      #tworzy nowy obiekt klasy 'Bird', która zawiera informacje o wyglądzie i pozycji ptaka na ekranie   
        bird.D_Bird(5, Bird_OY_Position+raise_by) #wywołuje metodę 'drawBird()' na obiekcie bird, która rysuje ptaka na ekranie 
        #argumenty 5 i Bird_OY_Postition-raiseby przekazane do metody 'drawBird()' określają położenie ptaka na osi X oraz Y odpowiednio
    
    def gravity(self):  #zdefiniowanie funkcji 'gravity'
         
        dropBy = 1 #ustawienie wartości 'dropBy' na 1, czyli ptak spadnie o 1 piksel w każdym wywołaniu funckcji
        if(Bird_OY_Position+dropBy >= height):   #sprawdzenie, czy po dodania wartości dropBy do bieżącej pozycji ptaka  wartość ta przekracza wysokość okna gry (zmienna height)
            #jeśli tak, to zmienna dropBy zostaje ustawiona na 0, aby uniemożliwić dalsze opadanie ptaka
            dropBy = 0
        bird = Bird()   #tworzy nowy obiekt klasy "Bird", która zawiera informacje o wyglądzie i pozycji ptaka na ekranie
        bird.D_Bird(5, Bird_OY_Position+dropBy) #bird.drawBird(5, birdYPos+dropBy) - wywołuje metodę drawBird() na obiekcie bird, która rysuje ptaka na ekranie 


class Main():
    global collision, score    #deklaruje zmienne 'collision' i 'score' jako zmienne globalne, 'collision' przechowuje informację o tym, czy ptak zderzył się z rurą, a score przechowuje wynik gracza                                  
    jumped = endGame = scoreUpdated = False   #inicjuja trzech zmiennych boolowskich (jumped, endGame, scoreUpdated) na wartość False, jumped przechowuje informację o tym, czy ptak wykonał już skok, 
                                              #'endGame' przechowuje informację o tym, czy gra powinna się zakończyć, a scoreUpdated przechowuje informację o tym, czy wynik gracza został zaktualizowany                                    
    frames = 1                   #inicjuja zmiennej 'frames' na wartość 1, zmienna ta przechowuje informację o liczbie klatek gry, która została już wyświetlona                 
    frameTime = 0.2              #inicjuja zmiennej 'frameTime' na wartość 0.2, zmienna ta przechowuje informację o czasie trwania jednej klatki gry
    while(not endGame):          #rozpoczyna pętlę nieskończoną, która będzie działać, dopóki gra nie zostanie zakończona.
        score = 0                #ustawienie wartość wyniku gracza na 0.
        game = Game()            #tworzenie nowego obiektu klasy 'Game', który reprezętuje gre
        bird = Bird()            #tworzenie nowego obiektu klasy 'Bird', który reprezętuje ptaka w grze
        game.startGame()         #wywołanie metody 'startGame' na obiekcie 'game', która inicjuje rogrywke
        bird.D_Bird(5, Bird_OY_Position)              #narysowanie ptaka na ekranie, argumenty '5' i 'bird_OY_Position' określają położenie ptaka na osi X oraz Y odpowiednio
        while(not collision and not endGame):   #rozpoczęcie nieskończonej pętli, która będzie działać, dopóki ptak nie zderzy się z rurą lub gra nie zostanie zakończona
            scoreUpdated = False                #ustawienie zmiennej 'scoreUpdated' na wartość False.
            os.system('cls')
            if(not jumped):                     #sprawdzene, czy ptak wykonał już skok, jeśli nie, to wywołuje metodę 'gravity()' na obiekcie bird, która implementuje grawitację i aktualizuje położenie ptaka na ekranie
                bird.gravity()                  

            game.printFrame()               
  
            frames += 1                      #zwiększenie wartości 'frames' o 1 
            if(frames == 1000):              #jeśli wartość osiągnie wartość 1000 to resetujemy ją do frames = 1
                frames = 1
            print("Your score is " + str(score))       #wyświetlenie wyniku użytkownika na ekranie

            print("Press \"e\" to end the round")
            print("Press space to jump! ")
            t0 = time.time()                           #pobranie czasu rozpoczęcia interakcji użytkownika z klawiaturą i ustawiamy ją na wartość 'False'
            jumped = False                             
            while(time.time()-t0 < frameTime):         # utworzenie pętli, która działa przez określony czas 'frameTime' i czeka na interakcję użytkownika z klawiaturą, 
                                                       #jeśli użytkownik naciśnie spację, ustawiamy wartość 'jumped' na 'True' i wywołujemy metodę 'jump()' na obiekcie 'bird', która wykonuje skok ptaka,
                if keyboard.is_pressed(' '):           #jeśli użytkownik naciśnie klawisz e, to ustawiamy wartość 'endGame' na 'True' i kończymy grę
                    jumped = True;                     #
                    bird.jump()                        #
                    break;                             #
                elif keyboard.is_pressed('e'):         #
                    endGame = True                     #
                    break                              #

            wait = round(time.time()-t0, 2)                  #oblicznie czasu, który upłyną od momentu rozpoćżecia każej iteracji pętli gry do momentu, w którym użytkownik wykonał skok lub nacisnięto przycisk kończący gre
            
            time.sleep(frameTime-wait)                       #ustawienie przerwy w grze tak, aby każda iteracja trwała około 0,2 sekundy.

        if(collision):                                       #sprawdzenie, czy w trakcie gry doszło do kolizji między ptakiem a rurami, jeśli tak, wyświetla stosowny komunikat
            print("\nWhoops, you had a collision!")
        userIn = input("\nType \"end\" to end the game, press \"enter\" to play again:\n")
        if("end" in userIn):              #jeśli użytkownik wprowadził "end" na wejściu, ustawia wartość 'endGame' na True, co spowoduje zakończenie gry
            endGame = True
        else:                             #jeśli użytkownik wprowadził cokolwiek innego, ustawia wartości 'collision'i endGame na False, co umożliwi ponowne uruchomienie gry
            collision = endGame = False 


if __name__ == '__main__':
    Main()           #wywołanie funkcji 'main'