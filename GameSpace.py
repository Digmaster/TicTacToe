import pygame
from pygame.locals import *
from Model import GameBoard
from Agent import SmartAgent as Agent
import threading
from copy import deepcopy

class GameSpace:
	moveStatement = "Move #{0}: Player {1} plays {2}"
	resourcesBase = "resources/"
	xChar = resourcesBase+"xChar.png"
	oChar = resourcesBase+"oChar.png"
	bChar = resourcesBase+"bChar.png"

	def __init__(self, board, numAgents):
		pygame.init()

		self.size = self.width, self.height = 64*3, 64*3
		self.black = 0, 0, 0
		self.screen = pygame.display.set_mode(self.size)

		self.board = board

		self.moveNum = 0
		self.agent1 = None
		self.agent2 = None

		if(numAgents >= 1):
			self.agent1 = Agent(board)
		if(numAgents == 2):
			self.agent2 = Agent(board)

		self.aiJob = False
		self.input = ""
		self.aiThread = None

	def update_screen(self):
		self.screen.fill(self.black)
		for i in range(3):
			for j in range(3):
				char = self.board.getSquareCoordinates(i, j)
				charSource = ""
				if(char=='X'):
					charSource = self.xChar
				elif(char=='O'):
					charSource = self.oChar
				else:
					charSource = self.bChar
				img = pygame.image.load(charSource)
				rec = img.get_rect()
				rec.top = i*64
				rec.left = j*64

				self.screen.blit(img, rec)
		pygame.display.update()

	def RunAI(self, agent, board, player):
		self.input = agent.getNextMove(player)
		self.aiJob = False


	def main(self):
		try:
			while(self.board.testWin() is '.'):
				self.update_screen()
				pygame.event.get() #Keeps the screen alive, otherwise it times out
				player = (self.moveNum%2) + 1
				move = None
				if(player == 1):
					if(self.agent1 != None):
						if(self.aiJob==False and self.input==""):
							self.aiJob=True
							self.aiThread = threading.Thread(target=self.RunAI, args=(self.agent1, deepcopy(self.board), 'X'))
							self.aiThread.start()
						elif(self.aiJob==False):
							move = self.input
							self.input = ""
							print self.moveStatement.format(self.moveNum, player, move)
					else:
						move = input(self.moveStatement.format(self.moveNum, player, ""))
				else:
					if(self.agent2 != None):
						if(self.aiJob==False and self.input==""):
							self.aiJob=True
							self.aiThread = threading.Thread(target=self.RunAI, args=(self.agent2, deepcopy(self.board), 'O'))
							self.aiThread.start()
						elif(self.aiJob==False):
							move = self.input
							self.input = ""
							self.moveStatement.format(self.moveNum, player, move)
					else:
						move = input(self.moveStatement.format(self.moveNum, player, ""))

				try:
					if(move!=None):
						self.board.setSquare(move, 'X' if player==1 else 'O')
						self.moveNum = self.moveNum+1
						print self.board
				except ValueError as e:
					print e
			self.update_screen();
		except KeyboardInterrupt:
			if(self.aiThread != None):
				print "Kill command received"
				print "Waiting for AI thread to terminate"
				self.aiThread.join()
		
