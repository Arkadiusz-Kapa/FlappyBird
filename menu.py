import keyboard, subprocess, os, time

level = 0
width, height = 50, 9
page = 0
class Board():
    def plansza2():
        N_menu = width-6
        for i in range(int((height-1)/2)):
            print("-"*width*2)
        print("-"*N_menu+"!MENU!"+ "-"*width)
        for i in range(int((height-1)/2)):
            print("-"*width*2)
    def plansza3():
        N_menu = width-6
        for i in range(int((height-1)/2)):
            print("-"*width*2)
        print("-"*N_menu+"!FlappyBird!"+ "-"*N_menu)
        for i in range(int((height-1)/2)):
            print("-"*width*2)
class main():
    os.system('cls')
    Board.plansza2()
    print("             current page: " + str(page) +"                                 w => next page")
    while(time.time()): 
        if keyboard.is_pressed("s"):
            page-=1
            break
        if keyboard.is_pressed("w"):
            page+=1
            print("             current page: " + str(page) +"          press s => page-1       w => next page")
            break
    while(time.time()):
        if page == 1:
            os.system('cls')
            Board.plansza3()
            print("\n"+"                                  Press SPACE to select game")
            print("             current page: " + str(page) +"          press s => page-1       w => next page")
            if keyboard.is_pressed(" "): 
                subprocess.run(["python", "FlappyBird.py"])
                break







if __name__ == '__main__':
    main()