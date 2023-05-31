import keyboard, subprocess, os

    os.system('cls')
    print("navigate by pressing W or S")
    if keyboard.is_pressed("w"): level += 1
    if keyboard.is_pressed("s"): level -= 1
    #subprocess.run(["python", "FlappyBird.py"])     