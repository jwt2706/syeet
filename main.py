import random, sys, time, os
from termcolor import cprint 
from pyfiglet import figlet_format
def pause(delay):
    time.sleep(delay)
def b(text, color='white', font='5lineoblique'):
    cprint(figlet_format(str(text),str(font)),str(color))
    p(".wav", "default", "instant", True)
#cybermedium, doom, starwars; block; larry3d, isometric1; 5lineoblique
def p(text, color = "default", type = "null", noline = False):
    if color == "red" or color == "r":
        text = "\033[1;31;48m" + text + "\033[1;37;48m"
    elif color == "blue" or color == "b":
        text = "\033[1;34;48m" + text + "\033[1;37;48m"
    elif color == "green" or color == "g":
        text = "\033[1;32;48m" + text + "\033[1;37;48m"
    elif color == "purple" or color == "p":
        text = "\033[1;35;48m" + text + "\033[1;37;48m"
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        if type == "slow" or type == "s":
            delay = (random.randint(1, 6) / 10)
        elif type == "fast" or type == "f":
            delay = (random.randint(1, 5) / 100)
        elif type == "instant" or type == "i":
            delay = 0
        else:
            delay = (random.randint(1, 13) / 100)
        pause(delay)
    if noline == False:
        sys.stdout.write("\n> ")
        pause(random.randint(3,40)/10)
p("Booting systems...", "g", "null", True)
pause(2)
p("\nSystems ready.", "b", "instant", True)
pause(1/2)
os.system("clear")
p("Fetching latest track...", "g", "null", True)
pause(1)
p("\nNow playing: ", "b", "null", True)
#--------------------------------------------------- TRACK NAME BELOW
p("", "p", "null", True)
#--------------------------------------------------- TRACK NAME ABOVE
p(".wav", "default", "null", True)
pause(2)
os.system("clear")
p("Starting requested program...", "g", "null", True)
pause(1)
p("\nAll set. Enjoy.", "b", "instant", True)
pause(1)
os.system("clear")
sys.stdout.write("C:\ \bUsers\defaultuser0\Documents\Programs\syeet.exe:\n> ")
sys.stdout.flush()
pause(random.randint(2,4))
#----------------------------------------------------- EDIT BELOW 
p("")
#----------------------------------------------------- EDIT ABOVE
pause(random.randint(3,6))
sys.stdout.write("\nEntry completed? (y/n): ")
sys.stdout.flush()
pause(random.randint(3,20)/10)
p("y\n", "null", True)
pause(random.randint(5,15)/10)
print("Save completed.")
pause(2)
os.system("clear")
p("Shutting down...", "g", "slow", True)
pause(2)
p("\nGoodnight. See you next time.", "b", "instant", True)
pause(5)
os.system("clear")
pause(30)
