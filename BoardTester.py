from GameBoard import Board

def testConstructorAndDrawBoard():
	"""Provides tests for the functionality of the constructor and the draw board"""
	try:
		# Tests for the expected size_length and board when inputted 3
		test_board = Board(3)
		row = ['-','-','-']
		initial_board = [row for i in range(3)]
		if initial_board != test_board.board:
			print('-__- Bug Found: The board is not being correctly built')
			return False
		if test_board.side_length != 3:
			print('-__- Bug Found: When inputted with 3 the side_length of the board is", test_board.side_length')
			return False
		# Test for when inputted a negative number
		try:
			test_board = Board(-1)
			print('T-__- Bug Found: Constructor should raise a ValueError when inputted with a negative number')
			return False
		except:
			print('' ,end='') # Do nothing this is supposed to happen ...
		# Test for when inputted a natural number less than 3
		try:
			test_board = Board(2)
			print('-__- Bug Found: Constructor should raise a ValueError when inputted with a natural number less than 3')
			return False
		except ValueError:
			print('' ,end='') # Do nothing this is supposed to happen ...
	except Exception:
		print("Bug Found: The constructor or draw_board() raises an unexpected exception -__-")
		return False
	return True

def testUpdateBoardAndGetBoard():
	"""Provides tests for the functionality of the update_board and get_board methods"""
	try:
		test_board = Board(3)
		new_board = [['X','O','X'],['O','X','O'],['O','X','X']]
		# Provides test for update_board()
		test_board.update_board(new_board)
		if test_board.board != new_board:
			print('-__- Bug Found: update board does not correctly update the game board')
			return False
		# Provides test for get_board()
		if test_board.get_board() != new_board:
			print('-__- Bug Found: get board does not return the correct board')
			return False
	except:
		print('-__- Bug Found: update_board() or get_board() raised an unexpected error')
		return False
	return True



if __name__ == '__main__':
	print('Tests for constructor and draw_board():', testConstructorAndDrawBoard())
	print('Tests for update_board() and get_board():', testUpdateBoardAndGetBoard())
