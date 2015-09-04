from random import randint
from random import getrandbits
from copy import deepcopy

class DumbAgent:
	def __init__(self, board):
		self.board = board

	def __str__(self):
		return "Hi, Im dumb agent. I play randomly as player {}".format(self.player)

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


	def __str__(self):
		return "Hi, Im smart agent. I whatever move will net me the most points, or avail my enemy of points. I'm {}".format(self.player)

	def getNextMove(self, player):
		moves = dict()
		for i in range(1,10):
			if(self.board.getSquare(i)=='.'):
				board = deepcopy(self.board)
				board.setSquare(i, player)
				moves[i] = -self.decideMove(board, 'X' if player=='O' else 'O')
				print i, moves[i]

		maxVal = -100000.0; #Stupid small number
		maxMove = 1;

		for key, value in moves.iteritems():
			#Randomly replace with same values to have some variation
			if((value == maxVal and bool(getrandbits(1))) or value > maxVal):  
				maxVal = value
				maxMove = key

		return maxMove

	def decideMove(self, board, player):
		winner = board.testWin()
		if(winner!='.'):
			if(winner==player):
				return 10.0
			elif(winner=='T'):
				return 0.0
			else:
				return -10.0

		sum = 0;
		for i in range(3):
			for j in range(3):
				if(board.getSquareCoordinates(i,j)=='.'):
					nBoard = deepcopy(board)
					nBoard.setSquareCoordinates(i, j, player)
					sum = sum - self.decideMove(nBoard, 'X' if player=='O' else 'O')/10.0

		return sum