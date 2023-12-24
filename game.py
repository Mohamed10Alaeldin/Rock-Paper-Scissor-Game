''' 
Rock beats Scissor
Scissor beats paper
paper beats Rock
'''

import random
from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.geometry("400x400+650-400")
window.title("Rock Paper Scissor Game")
window.resizable(0,0)

def computer_Value():
	com_choice = random.choice(['Rock', 'Paper', 'Scissor'])
	if com_choice == "Rock":
		rock_pic.config(bg="red")
	elif com_choice =="Paper":
		paper_pic.config(bg="red")
	else:
		scissor_pic.config(bg="red")
	return com_choice

def button_disable():
	# make the buttons unclickable
	rock_btn["state"] = "disable"
	paper_btn["state"] = "disable"
	scissor_btn["state"] = "disable"

def again():
	rock_btn["state"] = "active"
	paper_btn["state"] = "active"
	scissor_btn["state"] = "active"
	# return all buttons to their original color
	rock_btn.config(bg = "#f0f0f0")
	paper_btn.config(bg = "#f0f0f0")
	scissor_btn.config(bg = "#f0f0f0")
	rock_pic.config(bg="#f0f0f0")
	paper_pic.config(bg="#f0f0f0")
	scissor_pic.config(bg="#f0f0f0")
	# reset the result board
	result.config(text="")
	
def reset():
	# call again function
	again()
	# reset the counters
	com_score.config(text = "0")
	player_score.config(text = "0")

def isRock():
	rock_btn.config(bg="blue")
	com_choice = computer_Value()
	if com_choice == "Rock":
		match_result = "Tie"
	elif com_choice == "Scissor":
		match_result = "You Win"
		player_score.config(text = str(int(player_score.cget("text")) + 1))
	else:
		match_result = "Com Win"
		com_score.config(text = str(int(com_score.cget("text")) + 1))
	# print the match_result
	result.config(text=match_result)
	button_disable()
	
def isPaper():
	paper_btn.config(bg="blue")
	com_choice = computer_Value()
	if com_choice == "Rock":
		match_result = "You Win"
		player_score.config(text = str(int(player_score.cget("text")) + 1))
	elif com_choice == "Scissor":
		match_result = "Com Win"
		com_score.config(text = str(int(com_score.cget("text")) + 1))
	else:
		match_result = "Tie"
	result.config(text=match_result)
	button_disable()

def isScissor():
	scissor_btn.config(bg="blue")
	com_choice = computer_Value()
	if com_choice == "Rock":
		match_result = "Com Win"
		com_score.config(text = str(int(com_score.cget("text")) + 1))
	elif com_choice == "Scissor":
		match_result = "Tie"
	else:
		match_result = "You Win"
		player_score.config(text = str(int(player_score.cget("text")) + 1))
	result.config(text=match_result)
	button_disable()
# first label contains the Game Title
Label(window,
	text="Rock Paper Scissor",
	borderwidth=5,
	relief="solid",
	padx=10,
	font="normal 20 bold",
	fg="#76EE00").pack(pady=20)

frame = Frame(window)
frame.pack()
# hold player name
player_label = Label(frame,
		text="Player",
		borderwidth=2,
		relief="solid",
        bg="blue",
		padx=5,
		font=10)

player_score = Label(
	frame,
	text="0",
	bg="white",
	width=5,
	height=2,
	borderwidth=1,
	relief="solid")

vs_label = Label(frame,
		text="VS",
		fg ="#FF7F00",
		font=("Times",25,"bold"))
      
com_score = Label(
	frame,
	text="0",
	bg="white",
	width=5,
	height=2,
	borderwidth=1,
	relief="solid")

com_label = Label(frame,
        text="Com",
		borderwidth=2,
		relief="solid",
        bg="red",
		padx=5,
		width=20,
        font=10)

result = Label(window,
		text="",
		font="normal 15 bold",
		bg="white",
		width=10,
        height=3,
		borderwidth=2,
		relief="solid")

# place the widgets
player_label.pack(side=LEFT,pady=0,padx=10)
player_score.pack(side=LEFT)
vs_label.pack(side=LEFT,pady=0,padx=35)
com_score.pack(side=LEFT)
com_label.pack(side=LEFT,pady=0,padx=5)
result.pack(pady=10)

# ----- Player clickable Buttons --------- #
# resize the image to fit in button
img = ImageTk.PhotoImage(Image.open("rock.png").resize((70, 70)))
# Rock_Button
rock_btn = Button(window, image = img, command = isRock)
rock_btn.place(x = 10, y = 135)

img2 = ImageTk.PhotoImage(Image.open("paper.png").resize((70, 70)))
# Paper button
paper_btn = Button(window, image = img2, command = isPaper)
paper_btn.place(x = 10, y = 215)

img3 = ImageTk.PhotoImage(Image.open("scissor.png").resize((70, 70)))
# Scissor button
scissor_btn = Button(window, image = img3, command = isScissor)
scissor_btn.place(x=10, y=295)

# ------------- Unclickable Buttons (just images hhhh) ------ #
reverse_img = ImageTk.PhotoImage(Image.open("rock.png").rotate(180).resize((70, 70)))
rock_pic = Button(window, image = reverse_img, state="disabled")
rock_pic.place(x=325, y=135)

reverse_img2 = ImageTk.PhotoImage(Image.open("paper.png").rotate(180).resize((70, 70)))
paper_pic = Button(window,image=reverse_img2,state="disabled")
paper_pic.place(x=325, y=215)

reverse_img3 = ImageTk.PhotoImage(Image.open("scissor.png").rotate(180).resize((70, 70)))
scissor_pic = Button(window,image=reverse_img3,state="disabled")
scissor_pic.place(x=325, y=295)

# play again button
Button(window,
	text="Play Again",
	font=10,
	fg="white",
	bg="#007FFF",
	width=10,
	command = again).pack(pady=10)

# reset button
Button(window,
	text="Reset",
	font=10,
	fg="white",
	bg="#E3CF57",
	width=10,
	command = reset).pack()

window.mainloop()