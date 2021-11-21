import os

def game_board(row_1,row_2,row_3):

	print(row_1[0],"|",row_1[1],"|",row_1[2])
	print(row_2[0],"|",row_2[1],"|",row_2[2])
	print(row_3[0],"|",row_3[1],"|",row_3[2])

def player_choice(turn):

	acceptable_range = ("1","2","3","4","5","6","7","8","9")
	choice = 'Wrong'
	player = 'P'

	if turn%2 == 0:
		player = 'Player2'
	else:
		player = 'Player1'

	while choice not in acceptable_range:

		choice = input(f"{player} please choose the position (1-9): ")

		if choice not in acceptable_range:
			print("Invalid choice, please choose from 1-9")

	return choice

def player_selection(start):

	acceptable_label = ("X","x","O","o")
	player1_mark = "."

	while start and player1_mark not in acceptable_label:
		player1_mark = input("Player 1, choose your mark (X/O): ")

		if player1_mark not in acceptable_label:
			print("please choose either X or O")

	if player1_mark == "x" or player1_mark == "X":
		player1_mark = "X"
		player2_mark = "O"
		start = False
	else:
		player1_mark = "O"
		player2_mark = "X"
		start = False

	return player1_mark, player2_mark, start

def replacement(row_1,row_2,row_3,choice,turn):

	int_choice = int(choice)
	int_choice -= 1
	label = ""

	if turn%2 == 0:
		label = player2_mark
	else:
		label = player1_mark

	if int_choice in [0,1,2]:
		if row_3[int_choice] == ".":
			row_3[int_choice] = label.upper()
			turn += 1
			return row_1,row_2,row_3, turn
		else:
			print("This place is already taken please choose an empty box")
			return row_1,row_2,row_3, turn

	if int_choice in [3,4,5]:
		if row_2[int_choice - 3] == ".":
			row_2[int_choice - 3] = label.upper()
			turn += 1
			return row_1,row_2,row_3, turn
		else:
			print("This place is already taken please choose an empty box")
			return row_1,row_2,row_3, turn

	if int_choice in [6,7,8]:
		if row_1[int_choice - 6] == ".":
			row_1[int_choice - 6] = label.upper()
			turn += 1
			return row_1,row_2,row_3, turn
		else:
			print("This place is already taken please choose an empty box")
			return row_1,row_2,row_3, turn
		
def gameon(row_1,row_2,row_3):

	# diagnol wins
	if row_1[0]==row_2[1]==row_3[2]==player1_mark or row_1[2]==row_2[1]==row_3[0]==player1_mark:
		print("Player 1 won!")
		return False

	if row_1[0]==row_2[1]==row_3[2]==player2_mark or row_1[2]==row_2[1]==row_3[0]==player2_mark:
		print("Player 2 won!")
		return False

	#vertical wins
	if row_1[0]==row_2[0]==row_3[0]==player1_mark or row_1[1]==row_2[1]==row_3[1]==player1_mark or row_1[2]==row_2[2]==row_3[2]==player1_mark:
		print("Player 1 won!")
		return False

	if row_1[0]==row_2[0]==row_3[0]==player2_mark or row_1[1]==row_2[1]==row_3[1]==player2_mark or row_1[2]==row_2[2]==row_3[2]==player2_mark:
		print("Player 2 won!")
		return False

	#Horizontal win
	if row_1[0]==row_1[1]==row_1[2]==player1_mark or row_2[0]==row_2[1]==row_2[2]==player1_mark or row_3[0]==row_3[1]==row_3[2]==player1_mark:
		print("Player 1 won!")
		return False

	if row_1[0]==row_1[1]==row_1[2]==player2_mark or row_2[0]==row_2[1]==row_2[2]==player2_mark or row_3[0]==row_3[1]==row_3[2]==player2_mark:
		print("Player 2 won!")
		return False

	elif row_3.count(".") + row_1.count(".") + row_2.count(".") == 0:
		print("It is a draw")
		return False

	else:
		return True

def play_again(will):

	want = 'wrong'
	want_acceptable = ['y','Y','n','N']

	if will == False:
		while want not in want_acceptable:
			want = input("Do you want to play again? (Y/N): ")

			if want not in want_acceptable:
				print("Please choose either Y or N")

	if want == 'y' or want == 'Y':
		return True, True

	else:
		return False, False

will = True
turn = 1
start = True
player1_mark = "."
player2_mark = "."

while will:
	if start:
		row_1 = [".",".","."]
		row_2 = [".",".","."]
		row_3 = [".",".","."]
		player1_mark = "."
		player2_mark = "."
		turn = 1
		game_board(row_1,row_2,row_3)
		(player1_mark,player2_mark,start) = player_selection(start)
		print(f"player1_mark is {player1_mark} and player player2_mark is {player2_mark}")
	choice = player_choice(turn)
	[row_1,row_2,row_3,turn] = replacement(row_1,row_2,row_3,choice,turn)
	os.system("cls")
	game_board(row_1,row_2,row_3)
	will = gameon(row_1,row_2,row_3)
	if will == False:
		[will,start] = play_again(will)
		os.system("cls")
