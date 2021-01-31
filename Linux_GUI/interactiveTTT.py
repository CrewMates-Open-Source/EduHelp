# Tic Tac Toe game with GUI 
# using tkinter 

# importing all necessary libraries 
import random 
import tkinter 
from tkinter import *
from functools import partial 
from tkinter import messagebox 
from copy import deepcopy 
import cv2
import dlib
import numpy as np
import pyautogui
import threading
# sign variable to decide the turn of which player 
sign = 0

# Creates an empty board 
global board 
board = [[" " for x in range(3)] for y in range(3)] 

# Check l(O/X) won the match or not 
# according to the rules of the game 
def winner(b, l): 
	return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
			(b[1][0] == l and b[1][1] == l and b[1][2] == l) or
			(b[2][0] == l and b[2][1] == l and b[2][2] == l) or
			(b[0][0] == l and b[1][0] == l and b[2][0] == l) or
			(b[0][1] == l and b[1][1] == l and b[2][1] == l) or
			(b[0][2] == l and b[1][2] == l and b[2][2] == l) or
			(b[0][0] == l and b[1][1] == l and b[2][2] == l) or
			(b[0][2] == l and b[1][1] == l and b[2][0] == l)) 

# Check if the player can push the button or not 
def isfree(i, j): 
	return board[i][j] == " "

# Check the board is full or not 
def isfull(): 
	flag = True
	for i in board: 
		if(i.count(' ') > 0): 
			flag = False
	return flag 

# Decide the next move of system 
def pc(): 
	possiblemove = [] 
	for i in range(len(board)): 
		for j in range(len(board[i])): 
			if board[i][j] == ' ': 
				possiblemove.append([i, j]) 
	move = [] 
	if possiblemove == []: 
		return
	else: 
		for let in ['O', 'X']: 
			for i in possiblemove: 
				boardcopy = deepcopy(board) 
				boardcopy[i[0]][i[1]] = let 
				if winner(boardcopy, let): 
					return i 
		corner = [] 
		for i in possiblemove: 
			if i in [[0, 0], [0, 2], [2, 0], [2, 2]]: 
				corner.append(i) 
		if len(corner) > 0: 
			move = random.randint(0, len(corner)-1) 
			return corner[move] 
		edge = [] 
		for i in possiblemove: 
			if i in [[0, 1], [1, 0], [1, 2], [2, 1]]: 
				edge.append(i) 
		if len(edge) > 0: 
			move = random.randint(0, len(edge)-1) 
			return edge[move] 

# Configure text on button while playing with system 
def get_text_pc(i, j, gb, l1, l2): 
	global sign 
	if board[i][j] == ' ': 
		if sign % 2 == 0: 
			l1.config(state=DISABLED) 
			l2.config(state=ACTIVE) 
			board[i][j] = "X"
		else: 
			button[i][j].config(state=ACTIVE) 
			l2.config(state=DISABLED) 
			l1.config(state=ACTIVE) 
			board[i][j] = "O"
		sign += 1
		button[i][j].config(text=board[i][j], font=('Helvetica', 12)) 
	x = True

	if winner(board, "X"): 
		gb.destroy() 
		x = False
		box = messagebox.showinfo("Winner", "Player won the match") 
	elif winner(board, "O"): 
		gb.destroy() 
		x = False
		box = messagebox.showinfo("Winner", "Computer won the match") 
	elif(isfull()): 
		gb.destroy() 
		x = False
		box = messagebox.showinfo("Tie Game", "Tie Game") 
	if(x): 
		if sign % 2 != 0: 
			move = pc() 
			button[move[0]][move[1]].config(state=DISABLED) 
			get_text_pc(move[0], move[1], gb, l1, l2) 

# Create the GUI of game board for play along with system 
def gameboard_pc(game_board, l1, l2): 
	global button 
	button = [] 
	for i in range(3): 
		m = 3+i 
		button.append(i) 
		button[i] = [] 
		for j in range(3): 
			n = j 
			button[i].append(j) 
			print(i,j)
			get_t = partial(get_text_pc, i, j, game_board, l1, l2) 
			button[i][j] = Button(game_board, bd=5, command=get_t, height=16, width=32) 
			button[i][j].grid(row=m, column=n) 
	game_board.mainloop() 

# Initialize the game board to play with system 
def withpc(game_board): 
	game_board.destroy() 
	game_board = Tk() 
	game_board.title("Tic Tac Toe") 
	l1 = Button(game_board, text="Player : X", width=10) 
	l1.grid(row=1, column=1) 
	l2 = Button(game_board, text = "Computer : O", 
				width = 10, state = DISABLED) 
	
	l2.grid(row = 2, column = 1) 
	gameboard_pc(game_board, l1, l2) 

# main function 
def play(): 
	menu = Tk() 
	menu.geometry("400x150") 
	menu.title("Tic Tac Toe") 
	wpc = partial(withpc, menu) 
	
	head = Button(menu, text = "---Welcome to tic-tac-toe---", 
				activeforeground = 'red', 
				activebackground = "yellow", bg = "red", 
				fg = "yellow", width = 500, font = ('summer', 20), bd = 5) 

	B1 = Button(menu, text = "Single Player", command = wpc, 
				activeforeground = 'red', 
				activebackground = "yellow", bg = "red", 
				fg = "yellow", width = 500, font = ('summer', 15), bd = 5) 

	B3 = Button(menu, text = "Exit", command = menu.quit, activeforeground = 'red', 
				activebackground = "yellow", bg = "red", fg = "yellow", 
				width = 500, font = ('summer', 15), bd = 5) 
	head.pack(side = 'top') 
	B1.pack(side = 'top') 
	B3.pack(side = 'top') 
	menu.mainloop() 

def videocap():
    def shape_to_np(shape, dtype="int"):
        coords = np.zeros((68, 2), dtype=dtype)
        # loop over the 68 facial landmarks and convert them
        # to a 2-tuple of (x, y)-coordinates
        for i in range(0, 68):
            coords[i] = (shape.part(i).x, shape.part(i).y)
        # return the list of (x, y)-coordinates
        return coords


    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('Resources/shape_68.dat')

    cap = cv2.VideoCapture(0)
    ret, img = cap.read()

    i=0
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 1)
    for rect in rects:
        shape = predictor(gray, rect)
        shape = shape_to_np(shape)
    prev_mid =(shape[42] + shape[39]) // 2
    while(True):
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        rects = detector(gray, 1)
        h, w, l = img.shape
        for rect in rects:

            shape = predictor(gray, rect)
            shape = shape_to_np(shape)
            mid = (shape[42][0] + shape[39][0]) // 2
            curr_mid=(shape[42] + shape[39]) // 2

            # print(prev_mid - curr_mid)
            if(prev_mid[0]-curr_mid[0]>10):
                pyautogui.moveRel(20, 0, duration = 0.01)
            if(prev_mid[0]-curr_mid[0]<-10):
                pyautogui.moveRel(-20, 0, duration = 0.01)
            if(prev_mid[1]-curr_mid[1]>10):
                pyautogui.moveRel(0, -20, duration = 0.01)
            if(prev_mid[1]-curr_mid[1]<-10):
                pyautogui.moveRel(0, 20, duration = 0.01)
            if(abs(shape[37][1]-shape[41][1])<=5):
                i+=1
                if(i>15):
                    pyautogui.click()
                    i=0
        cv2.imshow('video feed', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
# Call main function 
if __name__ == '__main__': 
    p1 = threading.Thread(target=videocap)
    p2 = threading.Thread(target=play)
    p2.start()
    p1.start()
