# Base Node class
class Node:

	def __init__(self, state, parent, action, path_cost, zeroIndex):
		self.state = state
		self.parent = parent
		self.action = action
		self.path_cost = path_cost
		self.zeroIndex = zeroIndex

	