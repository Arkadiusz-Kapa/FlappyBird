import keyboard, subprocess, os

width, height = 100, 30
menu = [[0 for x in range(width)] for y in range(height)]
level = 0
class menu():
    for i in range(height): 
        for j in range(width):
            menu[i][j] ='-' if (i < 8) else '='
    for i in range(height):
        res = " "
        for j in range(width):
            res += menu[i][j]    
        print(res)
    os.system('cls')
    print("navigate by pressing W or S")
    if keyboard.is_pressed("w"): level += 1
    if keyboard.is_pressed("s"): level -= 1
    #subprocess.run(["python", "FlappyBird.py"])     