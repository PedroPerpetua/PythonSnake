import src.constants as constants

class Snake:
	def __init__(self, x, y):
		self.body = [(x, y), (x + 1, y), (x + 2, y)]
		self.direction = constants.WEST
		self.temp_direction = constants.WEST
		self.grow = 0
	def move(self):
		if self.temp_direction != self.direction:
			self.direction = self.temp_direction
		if self.direction == constants.NORTH:
			new_head = (self.body[0][0], (self.body[0][1] - 1) % constants.BOARD_SIZE)
		elif self.direction == constants.EAST:
			new_head = ((self.body[0][0] + 1) % constants.BOARD_SIZE, self.body[0][1])
		elif self.direction == constants.SOUTH:
			new_head = (self.body[0][0], (self.body[0][1] + 1) % constants.BOARD_SIZE)
		elif self.direction == constants.WEST:
			new_head = ((self.body[0][0] - 1) % constants.BOARD_SIZE, self.body[0][1])
		if self.grow > 0:
			self.body = [new_head] + self.body
			self.grow += -1
		else:
			self.body = [new_head] + self.body[:-1]
	def change_direction(self, new_direction):
		oposites = [(constants.NORTH, constants.SOUTH), (constants.SOUTH, constants.NORTH),
					(constants.EAST, constants.WEST), (constants.WEST, constants.EAST)]
		if (self.direction, new_direction) not in oposites:
			self.temp_direction = new_direction
	def lost(self):
		return self.body[0] in self.body[1:]