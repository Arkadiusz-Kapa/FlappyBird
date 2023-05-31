import keyboard, subprocess, os, time

level = 0
width, height = 50, 9
page = 0
def plansza2():
    N_menu = width-6
    for i in range(int((height-1)/2)):
        print("-"*width*2)
    print("-"*N_menu+"!MENU!"+ "-"*width)
    for i in range(int((height-1)/2)):
        print("-"*width*2)
class main():
    os.system('cls')
    plansza2()
    print("\n"+"                                  Press SPACE to select game")
    while(time.time()):
        if keyboard.is_pressed("s"):
            page-=1
            print("             current page: " + str(page) +"          press s => page-1       w => next page")
            break
        if keyboard.is_pressed("w"):
            page+=1
            print("             current page: " + str(page) +"          press s => page-1       w => next page")
            break

    #subprocess.run(["python", "FlappyBird.py"])      