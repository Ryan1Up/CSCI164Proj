# Base Problem Class
class Problem():


	actionDict = {"l":"r", "r":"l", "u":"d", "d":"u"}

	def __init__(self, initial, goal, boardSize):
		self.initial = initial[:]
		self.zeroIndex = initial.index("0")
		self.boardSize = boardSize
		self.goalState = goal[:]

	def getInvertedActions(actions):
		retList = []
		for act in actions:
			retList.append(Problem.actionDict.get(act))
		retList.reverse()
		return retList

	def isGoal(self, state) -> bool:
		return ''.join(state) == ''.join(self.goalState)

	def action_cost(self, state, action, newState) -> int:
		return 1

	def getMostRecentZeroIndex(self) -> int:
		return self.zeroIndex 

	def executeActionList(state, actions):
		for act in actions.lower():
			Problem.executeAction(state, act, state.index("0"))

	def executeAction(state, action, zIndex):
		boardSize = int(math.sqrt(len(state)))
		if Problem.isValidMove(state, action, zIndex):
			if action == "u":
				Problem.swap(zIndex, zIndex - boardSize, state)
			elif action == "d":
				Problem.swap(zIndex, zIndex + boardSize, state)
			elif action == "l":
				Problem.swap(zIndex, zIndex - 1, state)
			elif action == "r":
				Problem.swap(zIndex, zIndex + 1, state)

	def isValidMove(state, action, zIndex):
		boardSize = int(math.sqrt(len(state)))
		if action == " u":
			return zIndex > boardSize - 1
		elif action == "d":
			return zIndex//boardSize < boardSize - 1
		elif action == "l":
			return zIndex%boardSize != 0
		elif action == "r":
			return zIndex%boardSize < boardSize - 1

	def swap(zIndex, moveToIndex, state):
		temp = state[moveToIndex]
		state[moveToIndex] = state[zIndex]
		state[zIndex] = temp

