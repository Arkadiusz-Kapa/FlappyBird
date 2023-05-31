import keyboard, subprocess, os

width, height = 20, 11
menu = []
def plansza():
    os.system('cls')
    for i in range(height): 
        res = ['#' for i in range(width)]
        menu.append(res)
    print(*menu, sep ='\n')

print(plansza())
   #subprocess.run(["python", "FlappyBird.py"])     