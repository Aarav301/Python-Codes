from random import randint
from tkinter import *

score = 0

window = Tk()
window.title("Heads or Tails Game")

canvas = Canvas(window, width=400, height=200)
canvas.pack()

def Heads():
    global score
    random_no = randint(0, 1)
    if random_no == 0:
        canvas.delete("all") 
        canvas.create_text(200, 100, text="Heads - You won! Score: " + str(score + 1), font=("Helvetica", 14))
        score += 1
    else:
        canvas.delete("all") 
        canvas.create_text(200, 100, text="Tails - You lose", font=("Helvetica", 14))

def Tails():
    global score
    random_no = randint(0, 1)
    if random_no == 1:
        canvas.delete("all")  
        canvas.create_text(200, 100, text="Tails - You won! Score: " + str(score + 1), font=("Helvetica", 14))
        score += 1
    else:
        canvas.delete("all")  
        canvas.create_text(200, 100, text="Heads - You lose", font=("Helvetica", 14))

Button1 = Button(window, text="Heads", command=Heads)
Button2 = Button(window, text="Tails", command=Tails)

Button1.pack(side=LEFT, padx=10)
Button2.pack(side=RIGHT, padx=10)

window.mainloop()
