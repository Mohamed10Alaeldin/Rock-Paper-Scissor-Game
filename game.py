import random
from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.geometry("400x400+650-400")
window.title("Rock Paper Scissor Game")
window.resizable(0,0)

def computer_Value():
    value =  random.choice(['Rock', 'Paper', 'Scissor'])
    if value == "Rock":
        button4.config(bg="red")
    if value == "Paper":
    	button5.config(bg="red")
    if value == "Scissor":
    	button6.config(bg="red")
    
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
	button4.config(bg="#f0f0f0")
	button5.config(bg="#f0f0f0")
	button6.config(bg="#f0f0f0")
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
		match_result = "You Win"
		score_player1.config(text = str(int(score_player1.cget("text")) + 1))
	else:
		match_result = "Com Win"
		score_com.config(text = str(int(score_com.cget("text")) + 1))
	l4.config(text=match_result)
	button_disable()
	
def isPaper():
	button2.config(bg="blue")
	c_v = computer_Value()
	if c_v == "Rock":
		match_result = "You Win"
		score_player1.config(text = str(int(score_player1.cget("text")) + 1))
	elif c_v == "Scissor":
		match_result = "Com Win"
		score_com.config(text = str(int(score_com.cget("text")) + 1))
	else:
		match_result = "Tie"
	l4.config(text=match_result)
	button_disable()

def isScissor():
	button3.config(bg="blue")
	c_v = computer_Value()
	if c_v == "Rock":
		match_result = "Com Win"
		score_com.config(text = str(int(score_com.cget("text")) + 1))
	elif c_v == "Scissor":
		match_result = "Tie"
	else:
		match_result = "You Win"
		score_player1.config(text = str(int(score_player1.cget("text")) + 1))
	l4.config(text=match_result)
	button_disable()

Label(window,
	text="Rock Paper Scissor",
	borderwidth=5,
	relief="solid",
	padx=10,
	font="normal 20 bold",
	fg="#76EE00").pack(pady=20)

frame = Frame(window)
frame.pack()

l1 = Label(frame,
		text="Player1",
		borderwidth=2,relief="solid",
        bg="blue",
		padx=5,
		font=10)
score_player1 = Label(frame,text="0",bg="white",width=5,height=2,borderwidth=1,relief="solid")

l2 = Label(frame,
		text="VS",
		fg ="#FF7F00",
		font=("Times",25,"bold"))

        
score_com = Label(frame,text="0",bg="white",width=5,height=2,borderwidth=1,relief="solid")
l3 = Label(frame,
        text="Com",
		borderwidth=2,
		relief="solid",
        bg="red",
		padx=5,
		width=20,
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
button1.place(x=10, y=135)

img2 = ImageTk.PhotoImage(Image.open("paper.png").resize((70, 70)))
button2 = Button(window, image=img2 , command=isPaper)
button2.place(x=10, y=215)

img3 = ImageTk.PhotoImage(Image.open("scissor.png").resize((70, 70)))
button3 = Button(window, image=img3,command=isScissor)
button3.place(x=10, y=295)

revers_img = ImageTk.PhotoImage(Image.open("rock.png").rotate(180).resize((70, 70)))
button4 = Button(window,image=revers_img,state="disabled")
button4.place(x=325, y=135)

revers_img2 = ImageTk.PhotoImage(Image.open("paper.png").rotate(180).resize((70, 70)))
button5 = Button(window,image=revers_img2,state="disabled")
button5.place(x=325, y=215)

revers_img3 = ImageTk.PhotoImage(Image.open("scissor.png").rotate(180).resize((70, 70)))
button6 = Button(window,image=revers_img3,state="disabled")
button6.place(x=325, y=295)



again_button = Button(window, text="Play Again",
	font=10, fg="white",
	bg="#007FFF",
	width=10,
	command = again).pack(pady=20)
Button(window, text="reset",
	font=10, fg="white",
	bg="#E3CF57",
	width=10,
	command = reset).pack()

window.mainloop()