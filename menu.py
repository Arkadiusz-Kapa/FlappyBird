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
    def plansza4():
        N_menu = width-4
        for i in range(int((height-1)/2)):
            print("-"*width*2)
        print("-"*N_menu+"!DropBy!"+ "-"*N_menu)
        for i in range(int((height-1)/2)):
            print("-"*width*2)
class main():
    os.system('cls')
    Board.plansza2()
    print("             current page: " + str(page) +"                                 <= s or w =>")
    
    f_time = 0.2
    while True: 
        t0 = time.time()
        while(time.time()-t0 < f_time):
                                                       
            if keyboard.is_pressed('w'):
                page +=1
                print("             current page: " + str(page) +"                 <= s or w =>")
                break
            if keyboard.is_pressed('s'):
                page -=1
                print("             current page: " + str(page) +"                 <= s or w =>")
                break                                                           

        wait = round(time.time()-t0, 1)                  
            
        time.sleep(f_time-wait)
        if page > 2: page = 0
        if page < 0: page = 0 
        if page == 0:
            os.system('cls')
            Board.plansza2()
            print("\n"+"                                  Press SPACE to select game")
            print("             current page: " + str(page) +"                 <= s or w =>")
        elif page == 1:
            os.system('cls')
            Board.plansza3()
            print("\n"+"                                  Press SPACE to select game")
            print("             current page: " + str(page) +"                 <= s or w =>")
            if keyboard.is_pressed(" "): 
                subprocess.run(["python", "FlappyBird.py"])
        elif page == 2:
            os.system('cls')
            Board.plansza4()
            print("\n"+"                                  Press SPACE to select game")
            print("             current page: " + str(page) +"                 <= s or w =>")
            if keyboard.is_pressed(" "): 
                subprocess.run(["python", "DropBy.py"])







if __name__ == '__main__':
    main()