import keyboard, os, random, time

#Zmienne globalne:
width, height = 200, 20 #ustawienie wysokości i szerokości
Bird_OY_Position = height // 2
pipeSplitsQueue = []
gameBoard = [[0 for x in range(width)] for y in range(height)]
collision = False

class Game():
    def Pipe(self,OX_position, split):  #Funkcja rysująca rure
        for i in range(height):     # petla w zakresie do zmiennej height (wazne aby nei bylo tam stalej liczby a zmienna jesli chcemy latwiej zmieniac wielkosc ekranu gry)
            if(not(split-3 <= 1 <= split))
            gameBoard[i][OX_position]= "#"
            if(OX_position+1 < width):  #jeżeli zmienna jest mniejsza niż wysokość, to do elementu gameBoard[i][xpos+1] przypisywany jest znak '#' o takim samym kolorze jak wcześniej
                gameBoard[i][OX_position+1] = '#'
                if(OX_position+2 < width):  #jeżeli zmienna jest mniejsza niż wysokość to do elementu gameBoard[i][xpos+2] przypisywany jest znak '-' 
                    gameBoard[i][OX_position+2] = '-' if (i < 8) else '=' #jeżli i>= 8 zostanie użyty znak '=' 
    def Pipe_del(self, OX_position):
        gameBoard[i][xpos] = '-'if (i < 8) else '='  #ustawia wartość elementu gameBoard[i][xpos] w zależności od zmiennej i używany jest znak '-' lub znak '='
        gameBoard[i][xpos+1] = '-'if (i < 8) else '=' #ustawia analogicznie element gameBoard[i][xpos+1]
    
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
            thisPipe.drawPipe(i, split)

#Budowa Ptaka/ gracza:

class Bird():
    
    def D_Bird(self, x ,y):
        global Bird_OY_Position = y
        face = '>'
        body = '[]'
        for i in range(height): #pętla for iterująca przez cała wysokość - 1
            for j in range(x, x+3):  #pętla for iterująca od wartości x do wartości x + 3
                coor = gameBoard[i][j] #utworzenie zmiennej 'coor' i nadanie jej wartości 'gameBoard[i][j]'
                if(coor == body or coor == front or coor == beak): #sprawdzenie czy któryś z elementów ptaka jest równy z 'coor' 
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
        gameBoard[y][x+1] = mainBody  
        gameBoard[y][x+2] = '>'  
    def jump(self):     #zdefiniowanie funkcji 'jump'
        
        raise_by = 0        #inicjacja zmiennej 'raiseby' na 0, zmienna ta określa, o ile pikseli zostanie przesunięty ptak w górę w wyniku skoku
        if(Bird_OY_Position > 1):  #sprawdza, czy bieżąca pozycja ptaka (zmienna birdYPos) jest większa niż 1, jest to potrzebne, ponieważ nie chcemy, aby ptak skakał poza górną granicę okna gry
            raise_by = 1    #jeśli bieżąca pozycja ptaka jest większa niż 1, to zmienna raiseby zostaje ustawiona na 1, co oznacza, że ptak zostanie przesunięty o 1 piksel w górę
        bird = Bird()      #tworzy nowy obiekt klasy 'Bird', która zawiera informacje o wyglądzie i pozycji ptaka na ekranie   
        bird.D_Bird(5, Bird_OY_Position-raise_by) #wywołuje metodę 'drawBird()' na obiekcie bird, która rysuje ptaka na ekranie 
        #argumenty 5 i birdYPos-raiseby przekazane do metody 'drawBird()' określają położenie ptaka na osi X oraz Y odpowiednio
