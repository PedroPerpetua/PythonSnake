import src.constants as constants

class Snake:
	def __init__(self, x, y):
		self.body = [(x, y), (x + 1, y), (x + 2, y)]
		self.direction = constants.WEST
	def move(self):
		if self.direction == constants.NORTH:
			new_head = (self.body[0][0], (self.body[0][1] - 1) % constants.BOARD_SIZE)
		elif self.direction == constants.EAST:
			new_head = ((self.body[0][0] + 1) % constants.BOARD_SIZE, self.body[0][1])
		elif self.direction == constants.SOUTH:
			new_head = (self.body[0][0], (self.body[0][1] + 1) % constants.BOARD_SIZE)
		elif self.direction == constants.WEST:
			new_head = ((self.body[0][0] - 1) % constants.BOARD_SIZE, self.body[0][1])
		self.body = [new_head] + self.body[:-1]
	def change_direction(self, new_direction):
		oposites = [(constants.NORTH, constants.SOUTH), (constants.SOUTH, constants.NORTH),
					(constants.EAST, constants.WEST), (constants.WEST, constants.EAST)]
		if (self.direction, new_direction) not in oposites:
			self.direction = new_direction
	def grow(self):
		if self.direction == constants.NORTH:
			new_head = (self.body[0][0], (self.body[0][1] - 1) % constants.BOARD_SIZE)
		elif self.direction == constants.EAST:
			new_head = ((self.body[0][0] + 1) % constants.BOARD_SIZE, self.body[0][1])
		elif self.direction == constants.SOUTH:
			new_head = (self.body[0][0], (self.body[0][1] + 1) % constants.BOARD_SIZE)
		elif self.direction == constants.WEST:
			new_head = ((self.body[0][0] - 1) % constants.BOARD_SIZE, self.body[0][1])
		self.body = [new_head] + self.body