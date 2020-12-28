class Board:
	"""Represents A single game board

	Attributes
	___________

	side_length : int
		the length of each side of the board
	board : 2D list of strings
		represents the current version of the square game board
	empty_mark: str
		mark that represents an empty spot on the board

	Methods
	________

	draw_board()
		draws the current version of the board
	update_board()
		updates the board to the most recent move
	get_board()
		returns the current version of the game board
	game_over()
		returns true if the game is over, returns false otherwise
	get_filler
		returns the marking for an empty char
	"""

	def __init__(self, side_length):
		"""creates a new instance of the game board

		Parameters
		__________
		side_length : int
			the length of the dimensions for the square board

		Raises
		______
		ValueError
			raised when the length of the game board is less than 3
		"""

		if side_length < 3:
			raise ValueError('The Dimensions of the game board must at least be 3')
		self.empty_char = '-'
		self.side_length = side_length
		self.board = [[self.empty_char for n in range(self.side_length)] for m in range(self.side_length)]

	def draw_board(self):
		"""draws the current version of the board"""
		print('The game board will be a ' + str(self.side_length) + 'x' + str(self.side_length))
		for i in range(self.side_length):
			print('\t', end=str(i))
		print()
		for row in range(self.side_length):
			current_line = str(row) + '\t'
			for col in range(self.side_length):
				current_line += self.board[row][col] + '\t'
			print(current_line.strip())

	def update_board(self, new_board):
		"""Updates the current version of the board to a new inputted version

		Parameters
		__________
		new_board : 2D list of strings
			represents the new version of the board
		"""
		self.board = new_board

	def get_board(self):
		"""Accesspr method that returns the current state  of the board

		Returns
		_______
		a 2D list of strings which represent the current state of the board
		"""
		temp = []
		for row in range(self.side_length):
			current_row = []
			for col in range(self.side_length):
				current_row.append(self.board[row][col])
			temp.append(current_row)
		return temp

	def game_over():
		"""Returns true if the game should be over"""
		# TODO : check if the game is over yet
		return False
	def get_filler(self):
		return self.empty_char
if __name__ == '__main__':
	size = int(input('Enter the length for the dimensions of the board: '))
	game_one = Board(size)
	# game_one.draw_board
	print(game_one.get_board())