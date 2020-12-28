from GameBoard import Board
class player:
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

	def __init__(self, marking, game_board):
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
		self.player_board = game_board

	def is_valid_move(row, col, game_board):
		"""Checks if the player can make a move at the given location on the board"""
		check_board = game_board.get_board()
		return check_board[row][col] != game_board.get_filler()
if __name__ == '__main__':


