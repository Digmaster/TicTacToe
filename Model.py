# The model for the game board and a test to see if there is a winner in the current state

class GameBoard:
	"""  012
		0...
		1...
		2..."""
	def __init__(self):
		self.board = [['.' for x in range(3)] for x in range(3)]

	def __str__(self):
		out = ""
		for i in range(3):
			for j in range(3):
				out = out + self.board[i][j]
			out = out + '\n'
		return out

	# taking the chosen move and converting it to grid coordinates
	def getSquare(self, square):
		square = square - 1
		if(square > 8 or square < 0):
			raise ValueError("Square number must be between 1 and 9")
		x = (int)(square/3)
		y = (int)(square%3)
		return self.getSquareCoordinates(x, y)

	# Make sure that coordinates are on the board
	def getSquareCoordinates(self, x, y):
		if(x > 2 or x < 0 or y > 2 or y < 0):
			raise ValueError("Coordiantes are not on the board")

		return self.board[x][y]

	# Set the choosen move to the square
	def setSquare(self, square, player):
		square = square - 1
		if(square > 8 or square < 0):
			raise ValueError("Square number must be between 1 and 9")
		x = (int)(square/3)
		y = (int)(square%3)
		self.setSquareCoordinates(x, y, player)

	# Ensure the proper marker (X or O) is put onto the board
	def setSquareCoordinates(self, x, y, player):
		if(x > 2 or x < 0 or y > 2 or y < 0):
			raise ValueError("Coordiantes are not on the board")

		if(self.board[x][y]!='.'):
			raise ValueError('There is already a move at that spot')

		if(player!='X' and player!='O'):
			raise ValueError('The only valid players are X and O')

		self.board[x][y] = player

	# Test for a winning state or tie
	def testWin(self):
		""" Check horizontal wins """
		for i in range(3):
			left = self.board[0][i]
			if(left!='.'):
				if(self.board[1][i]==left and self.board[2][i]==left):
					return left

		""" Check verical wins """
		for i in range(3):
			top = self.board[i][0]
			if(top!='.'):
				if(self.board[i][1]==top and self.board[i][2]==top):
					return top

		""" Check diagonal left-right win """
		top = self.board[0][0]
		if(top!='.'):
			if(self.board[1][1]==top and self.board[2][2]==top):
				return top

		""" Check diagonal right-left win """
		top = self.board[2][0]
		if(top!='.'):
			if(self.board[1][1]==top and self.board[0][2]==top):
				return top

		""" Check for existance of a tie """
		isTie = True
		for i in range(3):
			for j in range(3):
				if(self.board[i][j]=='.'):
					isTie = False
		if(isTie):
			return 'T'
			
		""" No win, return . """
		return '.'



