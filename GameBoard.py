class Board:
	"""Represents A single game board

	Attributes
	___________

	side_length : int
		the length of each side of the board
	board : 2D list of strings
		represents the current version of the square game board

	Methods
	________

	draw_board()
		draws the current version of the board
	update_board()
		updates the board to the most recent move
	get_board()
		returns the current version of the game board
	game_over()
		returns true if the game is over, returns false otherwise"""

	def __init__(self, side_length):
		"""creates a new instance of the game board """
		self.side_length = side_length
		self.board = [['-' for n in range(self.side_length)] for m in range(self.side_length)]

	def draw_board(self):
		"""draws the current version of the board"""
		print('The game board will be a ' + str(self.side_length) + 'x' + str(self.side_length))
		for row in range(self.side_length):
			current_line = ''
			for col in range(self.side_length):
				current_line += self.board[row][col] + '\t'
			print(current_line.strip())

	def update_board(self, new_board):
		self.board = new_board

	def get_board():
		temp = [[self.board[row][col] for row in range(side_length)] for col in range(side_length)]
		return temp

	def game_over():
		# TODO : check if the game is over yet
		return False