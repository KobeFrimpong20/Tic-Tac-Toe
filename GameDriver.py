from GamePlayer import Player
from GameBoard import Board
import random

def make_player():
	""" Creates a player"""
	player_name = str(input(' what is your name: '))
	player_mark = str(input('Enter a character to represent your moves: '))
	try:
		p = Player(player_mark, game_board, player_name)
	except ValueError as ex:
		print(ex)
		while len(player_mark) != 1:
			player_mark = str(input('Re-enter your mark: '))
	finally:
		p = Player(player_mark, game_board, player_name)
	return p

def take_turn(gamer, play_board):
	""" Takes a turn """
	print(gamer.get_name() + ': Your Turn')
	print('___________________________________')
	row = int(input('Enter the row you want to play at: '))
	col = int(input('Enter the column you want to play at:'))
	gamer.place_marking(row, col, game_board)
	print('\n\n')
	play_board.draw_board()

if __name__ == '__main__':

	print('Welcome to Tic-Tac-Toe')
	print('______________________')
	option = int(input('Enter\n\t1 - for single player\n\t2 - for two player\n'))

	game_board = Board()
	print('Player one', end='')
	player_one = make_player()

	board_length = game_board.get_side_length() - 1
	if option == 1:
		player_two = Player('+', game_board)
		print('\n\n')
		game_board.draw_board()
		while not game_board.game_over(player_one, player_two):
			take_turn(player_one, game_board)
			print('______________________')
			if game_board.game_over(player_one, player_two):
				break
			row = -1
			col = -1
			while not player_two.is_valid_move(row, col, game_board):
				row = random.randint(0, board_length)
				col = random.randint(0, board_length)
			player_two.place_marking(row, col, game_board)
			print(player_two.get_name() + ' is taking their turn....')
			game_board.draw_board()
			print('______________________')

	elif option == 2:
		print('\nPlayer two', end='')
		player_two = make_player()
		print('\n\n')
		game_board.draw_board()
		while not game_board.game_over(player_one, player_two):
			take_turn(player_one, game_board)
			if game_board.game_over(player_one, player_two):
				break
			take_turn(player_two, game_board)

	if player_one.has_won(game_board):
		print(player_one.get_name() + ' won the game !!')
	elif player_two.has_won(game_board):
		print(player_two.get_name() + ' won the game !!')
	else:
		print('Its a draw')