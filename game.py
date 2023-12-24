import random
from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.geometry("400x400+650-400")
window.title("Rock Paper Scissor Game")

def computer_Value():
    value =  random.choice(['Rock', 'Paper', 'Scissor'])
    if value == "Rock":
    	rock_label.config(bg="red")
    if value == "Paper":
    	paper_label.config(bg="red")
    if value == "Scissor":
    	scissor_label.config(bg="red")
    
    return value

def button_disable():
	button1["state"] = "disable"
	button2["state"] = "disable"
	button3["state"] = "disable"

def again():
	button1["state"] = "active"
	button2["state"] = "active"
	button3["state"] = "active"
	button1.config(bg = "#f0f0f0")
	button2.config(bg = "#f0f0f0")
	button3.config(bg = "#f0f0f0")
	rock_label.config(bg="#f0f0f0")
	paper_label.config(bg="#f0f0f0")
	scissor_label.config(bg="#f0f0f0")
	l4.config(text="")
	
def reset():
	again()
	score_com.config(text = "0")
	score_player1.config(text = "0")

def isRock():
	button1.config(bg="blue")
	c_v = computer_Value()
	if c_v == "Rock":
		match_result = "Tie"
	elif c_v == "Scissor":
		match_result = "Player Win"
		score_player1.config(text = str(int(score_player1.cget("text")) + 1))
	else:
		match_result = "Computer Win"
		score_com.config(text = str(int(score_com.cget("text")) + 1))
	l4.config(text=match_result)
	button_disable()
	
def isPaper():
	button2.config(bg="blue")
	c_v = computer_Value()
	if c_v == "Rock":
		match_result = "Player Win"
		score_player1.config(text = str(int(score_player1.cget("text")) + 1))
	elif c_v == "Scissor":
		match_result = "Computer Win"
		score_com.config(text = str(int(score_com.cget("text")) + 1))
	else:
		match_result = "Tie"
	l4.config(text=match_result)
	button_disable()

def isScissor():
	button3.config(bg="blue")
	c_v = computer_Value()
	if c_v == "Rock":
		match_result = "Computer Win"
		score_com.config(text = str(int(score_com.cget("text")) + 1))
	elif c_v == "Scissor":
		match_result = "Tie"
	else:
		match_result = "Player Win"
		score_player1.config(text = str(int(score_player1.cget("text")) + 1))
	l4.config(text=match_result)
	button_disable()

Label(window,
	text="Rock Paper Scissor",
	font="normal 20 bold",
	fg="black").pack(pady=20)

frame = Frame(window)
frame.pack()

l1 = Label(frame,
		text="Player1",
        bg="blue",
		font=10)
score_player1 = Label(frame,text="0",bg="white",width=5,height=2,borderwidth=1,relief="solid")

l2 = Label(frame,
		text="VS",
		font=("Times",25,"bold"))

        
score_com = Label(frame,text="0",bg="white",width=5,height=2,borderwidth=1,relief="solid")
l3 = Label(frame,
        text="Computer",
        bg="red",
        font=10)

l4 = Label(window,
		text="",
		font="normal 15 bold",
		bg="white",
		width=10,
        height=3,
		borderwidth=2,
		relief="solid")

l1.pack(side=LEFT,pady=0,padx=5)
score_player1.pack(side=LEFT)
l2.pack(side=LEFT,pady=0,padx=35)
score_com.pack(side=LEFT)
l3.pack(side=LEFT,pady=0,padx=5)
l4.pack(pady=10)

#Rock_Button
img = ImageTk.PhotoImage(Image.open("rock.png").resize((70, 70)))
button1 = Button(window, image=img ,command=isRock)
button1.place(x=10, y=130)

img2 = ImageTk.PhotoImage(Image.open("paper.png").resize((70, 70)))
button2 = Button(window, image=img2 , command=isPaper)
button2.place(x=10, y=210)

img3 = ImageTk.PhotoImage(Image.open("scissor.png").resize((70, 70)))
button3 = Button(window, image=img3,command=isScissor)
button3.place(x=10, y=290)

rock_label = Label(window,
        text="rock",
        font=10)
rock_label.place(x=325, y=130)

paper_label = Label(window,
        text="paper",
        font=10)
paper_label.place(x=325, y=210)

scissor_label = Label(window,
        text="scissor",
        font=10)
scissor_label.place(x=325, y=290)


again_button = Button(window, text="Play Again",
	font=10, fg="white",
	bg="green",
	width=10,
	command = again).pack(pady=20)
Button(window, text="reset",
	font=10, fg="red",
	bg="black",
	width=10,
	command = reset).pack()

window.mainloop()