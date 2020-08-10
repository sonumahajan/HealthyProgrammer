from datetime import datetime
from pygame import mixer
from time import time

print("\n \n")
print("="*60)
print("Welcome to programe which is made for programmer's health.")
print("="*60)
print("\n")

def mixerloop(file, stoper):
    mixer.init()
    mixer.music.set_volume(0.7)
    mixer.music.load(file)
    mixer.music.play()
    while True:
        print("Enter when you done.")
        ans = input("Enter: ")
        print("-"*40)
        if ans == stoper:
            mixer.music.stop()
            break

def log(msg):
    with open("logs/logs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()} \n")


if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersec = 60
    eyessec = 120
    exercisesec = 180
    while True:
        if time() - init_water > watersec:
            print("Drink some water.")
            print("Enter 'drank' to stop alarm.")
            mixerloop("sounds/water.mp3","drank")
            init_water = time()
            log("Drank water at ")

        if time() - init_eyes > eyessec:
            print("Do some eyes exercise.")
            print("Enter 'doney' to stop alarm.")
            mixerloop("sounds/eyes.mp3","doney")
            init_eyes = time()
            log("Eyes exercise at ")

        if time() - init_exercise > exercisesec:
            print("Do some exercise.")
            print("Enter 'donez' to stop alarm.")
            mixerloop("sounds/physical.mp3","donez")
            init_exercise = time()
            log("Exercise done at ")
