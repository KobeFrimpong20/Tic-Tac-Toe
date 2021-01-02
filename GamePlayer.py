from GameBoard import Board
class Player:
	"""Represents a player in the Tic-Tac-Toe game

	Attributes
	__________
	marking : str
		A single character that is placed for each of the player's moves
	turns : int
		the number of moves that the player has made
	player_board : Board
		The board after this player's last move
	moves : 2D list
		List of all the moves that the player has made()

	Methods
	_______
	is_valid_move(row, col, game_board)
		returns true if a move can be made at that spot in the actual game board
	place_marking(row, col, game_board)
		places a marking down at the specified point on the game board
	has_won(game_board)
		returns true if the current player has won
	get_marking()
		Accessor that returns that marking of the player
	get_last_move()
		Accessor that returns the last version of the board that the player played on
		(Version of the board after the players last move)
	get_turns()
		accessor that returns the total turns the player has made
	get_name()
		accessor that returns the name of the player
	"""

	def __init__(self, marking, game_board, name='AI BoT'):
		"""Creates new instance of a player

		Parameters
		__________
		marking: str
			The marking that the user will be using when they take a turn

		Raises
		______
		ValueError
			Raised when marking is more than one character
		"""
		if len(marking) != 1:
			raise ValueError('Your marking must be one character like X or O or even $')
		if game_board is None:
			raise ValueError('The board you are trying to play on has not been created')
		self.marking = marking
		self.turns = 0
		self.name = name
		self.player_board = game_board
		self.moves = []

	def is_valid_move(self, row, col, game_board):
		"""Checks if the player can make a move at the given location on the board

		PARAMETERS
		__________
		row : int
			the row coordinate of the spot that is being tested
		col : int
			the column coordinate of the spot that is being tested
		game_board : Board
			the board that the has the spot that is being tested

		RETURNS
		_______
		True
			if the move being tested is on the board and not occupied
		False
			Otherwise
		"""
		if not self.is_in_bounds(row, col, game_board):
			return False
		return game_board.get_board()[row][col] == game_board.get_filler()

	def get_marking(self):
		""" accessor for the players marking"""
		return self.marking

	def get_last_move(self):
		""" accessor for the board after the players last move"""
		return self.player_board

	def get_name(self):
		""" accessor that returns the name of the player"""
		return self.name

	def place_marking(self, row, col, game_board):
		"""places a marking on the board for the player

		PARAMETERS
		__________
		row : int
			the row that the user attempts to place a marking at
		col : int
			the column that the user attempts to place a markking at
		game_board : Board
			the board that is currently being played on
		"""
		while not self.is_valid_move(row, col, game_board):
			print('Enter a different spot to play at')
			row = int(input('New Row: '))
			col = int(input('New Column: '))
		temp_board = game_board.get_board()
		temp_board[row][col] = self.marking
		game_board.update_board(temp_board)
		self.player_board.update_board(temp_board)
		self.moves.append([row, col])
		self.turns += 1

	def is_in_bounds(self, row, col, game_board):
		"""Determines if a spot is within the bounds of the game board

		PARAMETERS
		__________
		row : int
			the row coordinate of the spot being tested
		col : int
			the column coordinate of the spot being tested
		game_board : Board
			the board that each spot is being tested on

		RETURNS
		_______
		True
			if the spot is within the bounds of the board
		False
			otherwise
		"""
		valid_row = row >= 0 and row < game_board.get_side_length()
		valid_col = col >= 0 and col < game_board.get_side_length()
		return valid_row and valid_col


	def has_won(self, game_board):
		"""Determines if the player has won using the player's last move

		PARAMETERS
		__________
		game_board : Board
			the board that is currently being played on

		RETURNS
		_______
			True
				if the player has won on this board
			False
				otherwise
		"""
		if len(self.moves) == 0:
			 return False
		n = self.moves[len(self.moves) - 1]
		vert = True
		horiz = True
		forward = True
		backward = True
		row = n[0]
		col = n[1]
		game_matrix = game_board.get_board()
		i = 0
		while i < game_board.get_side_length() and (vert or horiz or forward or backward):
			# Check vertically |
			if vert and game_matrix[i][col] != self.marking:
				vert = False
			# Check horizontally --
			if horiz and game_matrix[row][i] != self.marking:
				horiz = False
			# Check the forward diagonal /
			if forward and game_matrix[i][i] != self.marking:
				forward = False
			if backward and game_matrix[game_board.get_side_length() - 1 - i][i] != self.marking:
				backward = False
			i += 1
		return vert or horiz or forward or backward

	def get_turns(self):
		"""Returns the amount of turns this player has taken"""
		return self.turns