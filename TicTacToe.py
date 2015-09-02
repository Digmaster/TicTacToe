from Model import GameBoard

agents = input("Enter Choice (1 for single agent 2 for dual agents): ")
agent1 = None
agent2 = None

moveStatement = "Move #{}: Player {} plays "

if(agents >= 1):
	print("Pretend one agent was made")
if(agents == 2):
	print("Pretend a second agent was made")
board = GameBoard()
moveNum = 0
while(board.testWin() is '.'):
	print board
	player = (moveNum%2) + 1
	move = 0
	if(player == 1):
		if(agent1 != None):
			print("Agent1 does its move")
		else:
			move = input(moveStatement.format(moveNum, player))
	else:
		if(agent1 != None):
			print("Agent2 does its move")
		else:
			move = input(moveStatement.format(moveNum, player))

	try:
		board.setSquare(move, 'X' if player==1 else 'O')
		moveNum = moveNum+1
	except ValueError as e:
		print e
print board
print "Player", board.testWin(), "Wins!"