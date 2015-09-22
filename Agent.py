from random import randint
from random import getrandbits
from copy import deepcopy

class DumbAgent:
	def __init__(self, board):
		self.board = board

	def __str__(self):
		return "Hi, Im dumb agent. I play randomly as player {0}".format(self.player)

	def getNextMove(self, player):
		board = deepcopy(self.board)
		if(player!='X' and player!='O'):
			raise ValueError('The only valid players are X and O')

		while(True):
			try:
				square = randint(1, 9)
				board.setSquare(square, player)
				return square
			except ValueError:
				"""Do nothing"""

class SmartAgent:
	def __init__(self, board):
		self.board = board
		self.signal = False
		self.bestVal = None


	def __str__(self):
		return "Hi, Im smart agent. I whatever move will net me the most points, or avail my enemy of points. I'm {0}".format(self.player)

	def getNextMove(self, player):
		self.decideMove(deepcopy(self.board), player)
		return self.bestVal

	def decideMove(self, board, player):
		if(self.signal):
			return 0
		winner = board.testWin()
		if(winner!='.'):
			if(winner=='X'):
				return 1.0
			elif(winner=='T'):
				return 0.0
			else:
				return -1.0

		values = []
		moves = {}
		for i in range(1,10):
			if(self.signal):
				return 0
			if(board.getSquare(i)=='.'):
				nBoard = deepcopy(board)
				nBoard.setSquare(i, player)
				value = self.decideMove(nBoard, 'X' if player=='O' else 'O')
				values.append(value)
				moves[value] = i
				if(player=='X'and value==1):
					break
				elif(player=='O' and value==-1):
					break

		if(player=='X'):
			sum = max(values)
		else:
			sum = min(values)
		self.bestVal = moves[sum]

		return sum