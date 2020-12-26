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

	Methods
	_______
	is_valid_move(row, col, game_board)
		returns true if a move can be made at that spot in the actual game board
	place_marking(row, col, game_board)
		places a marking down at the specified point on the game board
	has_won(game_board)
		returns true if the current player has won"""

	def __init__(self, marking):
		self.marking = marking
		self.turns = 0
		self.player_board = Board()