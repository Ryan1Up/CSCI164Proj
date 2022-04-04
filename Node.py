# Base Node class
class Node:

	def __init__(self, state, parent, action, path_cost, zeroIndex):
		self.state = state
		self.parent = parent
		self.action = action
		self.path_cost = path_cost
		self.zeroIndex = zeroIndex

	
	def __lt__(self, other):
		if not other or not self:
			return False
		else:
			return self.path_cost < other.path_cost


	def __eq__(self, other):
		if not other or not self:
			return False
		else:
			return self.path_cost == other.path_cost

	def __gt__(self, other):
		if not other or not self:
			return False
		else:
			return self.path_cost > other.path_cost