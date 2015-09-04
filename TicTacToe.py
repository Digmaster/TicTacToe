from Model import GameBoard
from Agent import SmartAgent as Agent
import pygame
from pygame.locals import *
from GameSpace import GameSpace

moveStatement = "Move #{}: Player {} plays {}"
DESIRED_FPS = 60.0 # 60 frames per second

agents = input("Enter Choice (1 for single agent 2 for dual agents): ")
agent1 = None
agent2 = None

board = GameBoard()

# if __name__ == '__main__':
# 	gs = GameSpace()
# 	tick = LoopingCall(gs.main)
# 	tick.start(1.0 / DESIRED_FPS)

gs = GameSpace(board, agents)
gs.main()

if(board.testWin()=='T'):
	print "The game ends in a tie!"
else:
	print "Player", board.testWin(), "Wins!"