from Model import GameBoard
from Agent import SmartAgent as Agent

moveStatement = "Move #{}: Player {} plays {}"

agents = input("Enter Choice (1 for single agent 2 for dual agents): ")
agent1 = None
agent2 = None

board = GameBoard()

if(agents >= 1):
	agent1 = Agent(board)
if(agents == 2):
	agent2 = Agent(board)
moveNum = 0
while(board.testWin() is '.'):
	print board
	player = (moveNum%2) + 1
	move = 0
	if(player == 1):
		if(agent1 != None):
			move = agent1.getNextMove('X')
			print moveStatement.format(moveNum, player, move)
		else:
			move = input(moveStatement.format(moveNum, player, ""))
	else:
		if(agent2 != None):
			move = agent2.getNextMove('O')
			print moveStatement.format(moveNum, player, move)
		else:
			move = input(moveStatement.format(moveNum, player, ""))

	try:
		board.setSquare(move, 'X' if player==1 else 'O')
		moveNum = moveNum+1
	except ValueError as e:
		print e
print board
if(board.testWin()=='T'):
	print "The game ends in a tie!"
else:
	print "Player", board.testWin(), "Wins!"