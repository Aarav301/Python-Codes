#GHOST GAME
from random import randint
print ("Ghost Game")
feeling_brave = True
score = 0
while feeling_brave:    
    ghost_door = randint(1, 5)
    print("five doors ahead...")
    print("a ghost behind one.")
    print("which door do you open?")
    door = input ("1, 2, 3, 4 or 5?")
    door_num = int(door)   
    if door_num == ghost_door:
        print ("GHOST!")
        feeling_brave = False
    else:        
        print ("No ghost")
        print ("You enter the next room.")
        score = score + 1
print("Run away!")
print("Game over! you scored", score)

        
