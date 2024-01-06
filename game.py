''' 
Game Rules:
Rock beats scissor
Scissor beats paper
Paper beats rock
'''
import random # this library to deal with computer choices randomly
from tkinter import * # this library to deal with GUI
from PIL import Image, ImageTk # this library to deal with images

''' If you delete these two lines below the welcoming messagge from Pygame community will appear on console.
pygame 2.5.2 (SDL 2.28.3, Python 3.11.1)
Hello from the pygame community. https://www.pygame.org/contribute.html
so i hide it with 'PYGAME_HIDE_SUPPORT_PROMPT' equal to any value
'''
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '3'

import pygame # this library to deal with sounds

#  Main Window
window = Tk()
window.geometry("410x430+650-400")
window.title("Rock Paper Scissor Game")
window.resizable(0,0)
window.config(bg="#282829")

# ---------- The Images -----------
rock_img = ImageTk.PhotoImage(Image.open("./Images/rock.png").resize((70, 70)))
paper_img = ImageTk.PhotoImage(Image.open("./Images/paper.png").resize((70, 70)))
scissor_img = ImageTk.PhotoImage(Image.open("./Images/scissor.png").resize((70, 70)))

reverse_rock_img = ImageTk.PhotoImage(Image.open("./Images/rock.png").transpose(Image.FLIP_LEFT_RIGHT).resize((70, 70)))
reverse_paper_img = ImageTk.PhotoImage(Image.open("./Images/paper.png").transpose(Image.FLIP_LEFT_RIGHT).resize((70, 70)))
reverse_scissor_img = ImageTk.PhotoImage(Image.open("./Images/scissor.png").transpose(Image.FLIP_LEFT_RIGHT).resize((70, 70)))

win_img=ImageTk.PhotoImage(Image.open("./Images/win.png").resize((150,150)))
lose_img=ImageTk.PhotoImage(Image.open("./Images/lose.png").resize((150,150)))
tie_img=ImageTk.PhotoImage(Image.open("./Images/tie.png").resize((150,150)))
play_img=ImageTk.PhotoImage(Image.open("./Images/start.png").resize((150,150)))

# ------------ Voices ------------------#
pygame.mixer.init() # initialise the pygame 
def winVoice():
	pygame.mixer.music.load("./Sounds/winvoice.mp3")
	pygame.mixer.music.play(loops=0)

def loseVoice():
	pygame.mixer.music.load("./sounds/losevoice.mp3")
	pygame.mixer.music.play(loops=0)

def tieVoice():
	pygame.mixer.music.load("./sounds/draw.mp3")
	pygame.mixer.music.play(loops=0)


def computer_Value():
	com_choice = random.choice(['Rock', 'Paper', 'Scissor'])
	if com_choice == "Rock":
		rock_label.config(bg="red")
	elif com_choice =="Paper":
		paper_label.config(bg="red")
	else:
		scissor_label.config(bg="red")
	return com_choice

def button_disable():
	rock_btn["state"] = "disable"
	paper_btn["state"] = "disable"
	scissor_btn["state"] = "disable"

# ----------Buttons command------------ #
def isRock():
	rock_btn.config(bg="blue")
	com_choice = computer_Value()
	if com_choice == "Rock":
		result.config(image=tie_img)
		tieVoice()

	elif com_choice == "Scissor":
		result.config(image=win_img)
		player_score.config(text = str(int(player_score.cget("text")) + 1))
		winVoice()

	else:
		result.config(image=lose_img)
		com_score.config(text = str(int(com_score.cget("text")) + 1))
		loseVoice()	

	button_disable()
	
def isPaper():
	paper_btn.config(bg="blue")
	com_choice = computer_Value()
	if com_choice == "Rock":
		result.config(image=win_img)
		player_score.config(text = str(int(player_score.cget("text")) + 1))
		winVoice()

	elif com_choice == "Scissor":
		result.config(image=lose_img)
		com_score.config(text = str(int(com_score.cget("text")) + 1))
		loseVoice()

	else:
		result.config(image=tie_img)
		tieVoice()

	button_disable()

def isScissor():
	scissor_btn.config(bg="blue")
	com_choice = computer_Value()
	if com_choice == "Rock":
		com_score.config(text = str(int(com_score.cget("text")) + 1))
		result.config(image=lose_img)
		loseVoice()

	elif com_choice == "Scissor":
		result.config(image=tie_img)
		tieVoice()

	else:
		result.config(image=win_img)
		player_score.config(text = str(int(player_score.cget("text")) + 1))
		winVoice()

	button_disable()

def play_again():
	rock_btn["state"] = "active"
	paper_btn["state"] = "active"
	scissor_btn["state"] = "active"
	# return all buttons and labels to their original color
	rock_btn.config(bg = "#f0f0f0")
	paper_btn.config(bg = "#f0f0f0")
	scissor_btn.config(bg = "#f0f0f0")
	rock_label.config(bg="#f0f0f0")
	paper_label.config(bg="#f0f0f0")
	scissor_label.config(bg="#f0f0f0")
	# reset the result board
	result.config(image = play_img)
	
def reset():
	# call play_again function
	play_again()
	# reset the counters
	com_score.config(text = "0")
	player_score.config(text = "0")
	
# Game Title
Label(window,
	text="Rock Paper Scissor",
	padx=10,
	fg="white",
	relief="solid",
	bg="#F77A05",
	font="system 20 bold").pack(pady=20)

frame = Frame(window) 
frame.config(bg="#282829")
frame.pack()
player_label = Label(frame,
		text="Player",
		padx=5,
		relief = "ridge", 
		fg = "#fff",
		bg = "#1E90FF",
		width=6,
		font=10)

player_score = Label(
	frame,
	bg = "#1E90FF",
	fg = "white",
	relief = "ridge", 
	text="0",
	width=5,
	height=2)

vs_label = Label(frame,
		fg = "#EE2C2C",
		bg = "#282829",
		text="VS",
		font=("Times",25,"bold"))
      
com_score = Label(
	frame,
	bg = "#ff0000",
	fg = "white",
	text="0",
	relief = "ridge", 
	width=5,
	height=2)

com_label = Label(frame,
		fg = "#fff",
		bg = "#ff0000",
		relief = "ridge", 
        text="Com",
		width=6,
        font=10)
# Result board
result = Label(window, image=play_img)

# place the widgets
player_label.pack(side=LEFT,padx=10)
player_score.pack(side=LEFT)
vs_label.pack(side=LEFT,padx=35)
com_score.pack(side=LEFT)
com_label.pack(side=LEFT,padx=10)
result.pack(pady=10)

# ----- Player clickable Buttons --------- #
# Rock_Button
rock_btn = Button(window, image = rock_img, relief="solid", command = isRock)
rock_btn.place(x = 10, y = 135)

# Paper button
paper_btn = Button(window, image = paper_img, relief="solid", command = isPaper)
paper_btn.place(x = 10, y = 215)

# Scissor button
scissor_btn = Button(window, image = scissor_img, relief="solid", command = isScissor)
scissor_btn.place(x=10, y=295)

# Computer unclickable pictures
rock_label = Label(window, image = reverse_rock_img)
rock_label.place(x=325, y=135)

paper_label = Label(window, image = reverse_paper_img)
paper_label.place(x=325, y=215)

scissor_label = Label(window, image = reverse_scissor_img)
scissor_label.place(x=325, y=295)

# play again button
Button(window,
	text="Play Again",
	fg = "#fff",
	bg="#F77A05",
	font=10,
	width=10,
	command = play_again).pack(pady=10)

# reset button
Button(window,
	text="Reset",
	fg = "#fff",
	bg = "#F77A05",
	font=10,
	width=10,
	command = reset).pack()

window.mainloop()
