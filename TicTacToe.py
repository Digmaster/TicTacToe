from Model import GameBoard
from Agent import SmartAgent as Agent
import pygame
from pygame.locals import *
from GameSpace import GameSpace

# Get the number of agents
agents = input("Enter Choice (1 for single agent 2 for dual agents): ")

# Create the game board
board = GameBoard()
print board

#Create the game spcae and run the game
gs = GameSpace(board, agents)
gs.main()

#Check the status of the board and report on it
if(board.testWin()=='T'):
	print "The game is a tie."
elif(board.testWin()!='.'):
	print "Player", '1' if board.testWin()=='X' else '2', "has won."
else:
	print "Game was ended before it completed."