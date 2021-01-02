from GamePlayer import Player
from GameBoard import Board

def testConstructorAndAccessors():
	"""Provides tests for the functionality of the constructor of the player class"""
	try:
		# Tests scenario of invalid marking and valid Board
		marking = '343'
		this_board = Board(3)
		try:
			p_one = Player(marking, this_board)
			return False
		except ValueError:
			print('',end='')	# Do nothing this is supposed to happen...
		# Tests scenario of valid marking and invalid Board
		marking = '$'
		this_board = None
		try:
			p_one = Player(marking, this_board)
			return False
		except ValueError:
			print('',end='')	# Do nothing this is supposed to happen...
		# Tests scenario of valid input for player
		this_board = Board(3)
		p_one = Player(marking, this_board)
		if p_one.get_marking() != marking:
			print('Bug Found -__-: get_marking() accessor is not functioning')
			return False
		if p_one.get_last_move() != this_board:
			print('Bug Found -__-: get_last_move accessor is not functioning')
	except:
		print('Bug Found -__-: One of the constructors or accessors raised an unexpected error'
		+' or exception')
		return False
	return True


def testIsValidMove():
	""" Provides tests for the functionality of the is_valid_move() method"""
	try:
		# Test scenario of empty Board with an input that is out of bounds
		row = 3
		col = 2
		test_board = Board(3)
		player_one = Player('@', test_board)
		try:
			if player_one.is_valid_move(row, col, test_board):
				print('Bug Found -__-: tested with a spot out of bounds (3,2): (row,col) your code'
					+ ' returned True.')
				return False
		except ValueError:
			print('',end='')	# Do nothing this is supposed to ...
		# Test scenario of empty Board with valid input
		row = 2
		if not player_one.is_valid_move(row, col, test_board):
			print('Bug Found -__-: tested with an empty board and spot inbounds your code'
			+' returned False.')
			return False
		# Test scenario of filled in board with valid input
		test_board.update_board([['X','O','X'],['O','X','O'],['O','X', test_board.get_filler()]])
		if not player_one.is_valid_move(row, col, test_board):
			print('Bug Found -__-: tested with valid move but your code returned False')
			return False
		# Test scenario of filled in board with out of bounds input
		try:
			row = 3
			if player_one.is_valid_move(row, col, test_board):
				print('Bug Found -__-: tested with a move out of bounds but your code returned true')
				return False
		except:
			print('',end='')	# Do nothing this is supposed to happen ...

		# Test scenario of filled in board with input on occupied spot
		row = 0
		if player_one.is_valid_move(row, col, test_board):
			print('Bug Found -__-: tested with a move on a spot that has already been marked'
			+' your code returned True')
			return False
	except:
		print('Bug Found -__-: is_valid_move() raised an unexpeceted error or exception')
		return False
	return True

def testPlaceMarking():
	"""Provides tests for functionality for the place_marking() method"""
	try:
		row = 2
		col = 2
		test_board = Board(3)
		test_board.update_board([['X','O','X'],['O','X','O'],['O','X', test_board.get_filler()]])
		player_one = Player('K', test_board)
		player_one.place_marking(row, col, test_board)
		# tests that both test board and player last move are updated correctly
		if test_board != player_one.get_last_move():
			print('Bug Found -__-: place_marking() does not correctly update the players last move'
				+ ' or the game board')
			return False
		# tests that both test board and player last move have the marking placed
		correct_board = [['X','O','X'],['O','X','O'],['O','X', player_one.get_marking()]]
		if correct_board != player_one.get_last_move().get_board():
			print('Bug Found -__-: place_marking() does not correctly place the marking on'
				+' the board')
			return False
	except:
		print('Bug Found -__-: place_marking() function raised an unexpected error or exception')
		return False
	return True

def testIsInBounds():
	"""Provides tests for the functionality of the __is_in_bounds() methods"""
	try:
		# Test scenario that is with in the bounds of the board
		row = 0
		col = 0
		test_board = Board(3)
		player_one = Player('#', test_board)
		if not player_one.is_in_bounds(row, col, test_board):
			print('Bug Found -__- is_in_bounds() returned false when inputted on a board at 0,0')
			return False
		# Test scenario that is with in the bounds of the board:
		row = 4
		col = 5
		if player_one.is_in_bounds(row, col, test_board):
			print('Bug Found -__- is_in_bounds() returned true when inputted with coordinates' +
				' that were off the board')
			return False
	except:
		print('Bug Found -__- is_in_bounds() threw an unexpected error or exception')
		return False
	return True

def testHasWon():
	"""Tests the functionality of the has_won() method"""
	try:
		# Test scenario: has_won() is called on an empty board
		test_board = Board(3)
		p_one = Player('$', test_board)
		if p_one.has_won(test_board):
			print('Bug Found -__- has_won() returned true when tested with empty board')
			return False
		# Test scenario: filled in board but the player has not won
		p_one.place_marking(0,0, test_board)
		p_one.place_marking(1,1, test_board)
		if p_one.has_won(test_board):
			print('Bug Found -__- has_won() returned true when tested with a board' +
				' that the player has not won')
			return False
		# Test scenario: filled in board player wins backward \
		p_one.place_marking(2,2, test_board)
		if not p_one.has_won(test_board):
			print('Bug Found -__- has_won() returned false when tested with a winning ' +
				'backward board')
			return False
		# Test scenario: filled in board players wins forward /
		test_board = Board(3)
		p_one = Player('$', test_board)
		p_one.place_marking(2,0, test_board)
		p_one.place_marking(1,1, test_board)
		p_one.place_marking(0,2, test_board)
		if not p_one.has_won(test_board):
			print('Bug Found -__- has_won() returned false when tested with a winning ' +
				'forward board')
			return False
		# Test scenario: filled in board players wins vertical |
		test_board = Board(3)
		p_one = Player('$', test_board)
		p_one.place_marking(2,0, test_board)
		p_one.place_marking(1,0, test_board)
		p_one.place_marking(0,0, test_board)
		if not p_one.has_won(test_board):
			print('Bug Found -__- has_won() returned false when tested with a winning ' +
				'vertical board')
			return False
		# Test scenario: filled in board players wins horizontal ---
		test_board = Board(3)
		p_one = Player('$', test_board)
		p_one.place_marking(2,2, test_board)
		p_one.place_marking(2,1, test_board)
		p_one.place_marking(2,0, test_board)
		if not p_one.has_won(test_board):
			print('Bug Found -__- has_won() returned false when tested with a winning ' +
				'horizontal board')
			return False
	except:
			print('Bug Found -__- has_won() threw an unexpected error or exception')
			return False
	return True

if __name__ == '__main__':
	print('Tests for Constructor and Accessors:', testConstructorAndAccessors())
	print('Tests for is_valid_move():', testIsValidMove())
	print('Tests for place_marking():', testPlaceMarking())
	print('Tests for is_in_bounds():', testIsInBounds())
	print('Tests for has_won():', testHasWon())