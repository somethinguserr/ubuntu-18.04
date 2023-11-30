# Perfect

def ConstBoard(board):
	for i in range(0,9):
		if(i>0 and i%3==0):
			print("\n")
		if (board[i]==0):
			print("| - |", end=" ")
		if (board[i]==1):
			print("| X |", end=" ")
		if (board[i]==-1):
			print("| O |", end=" ")
	print("\n")

def UserTurn(board):
	while True:
		pos =int(input("Enter your position: [1..9]"))
		if(pos<1 or pos>9):
			print("Wrong move!!")
			continue
		if(board[pos-1]!=0):
			print("Wrong move!!")
			continue

		break		
	board[pos-1]=1

def analyse(board):
	cb = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
	for i in range(0,8):
		if(board[cb[i][0]]!=0 and board[cb[i][0]] == board[cb[i][1]] and board[cb[i][0]]==board[cb[i][2]]):
			return board[cb[i][2]]
	return 0
def minmax(board,player):
	pos=-1
	value=-2
	x = analyse(board)
	if(x!=0):
		return(x*player)
	for i in range(0,9):
		if(board[i]==0):
			board[i]=player
			# score = - minmax(board, player*(/-1))
			score = - minmax(board, player*(-1))
			if(score>value):
				value = score
				pos = i
			board[i]=0
	if (pos==-1):
		return 0
	return value

def CompTurn(board):
	pos=-1
	value=-2
	for i in range(0,9):
		if(board[i]==0):
			board[i]=-1
			score = -minmax(board, 1)
			board[i]=0
			if (score>value):
				value = score
				pos = i
	board[pos]=-1

if __name__ == "__main__":
	board = [0,0,0,0,0,0,0,0,0]
	print("Computer-> O vs You-> X")
	player = int(input("Enter choice play 1st or 2nd:"))
	for i in range(0,9):
		if(analyse(board)!=0):
			break
		if((i+player)%2==0):
			CompTurn(board)
		else:
			ConstBoard(board)
			UserTurn(board)
	ConstBoard(board)
	x = analyse(board)
	if(x==0):
		print("Draw!!")
	if(x==1):
		print("X Wins!!")
	if(x==-1):
		print("O Wins!!")
	print("\n")
