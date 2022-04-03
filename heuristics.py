# Hueristic functions for Search Functions

def getOutOfPlace(state, goalState, boardSize) -> int:
	retVal = 0
	for s in goalState:
		if goalState.index(s) != state.index(s) and s != '0':
			retVal += 1

	return retVal

def getManhattanDistance(state, goalState, boardSize) -> int:
	retVal = 0
	for s in state:
		if s != '0':
			retVal += getManhattanForElement(s, state.index(s), goalState, boardSize)
	return retVal

def getManhattanForElement(element, index, goalState, boardSize) -> int:
	return rowOffset(element, index, goalState, boardSize) + columnOffset(element, index, goalState, boardSize)

def rowOffset(element, index, goalState, boardSize) -> int:
	return abs(getConversion(element)//boardSize - index//boardSize)

def columnOffset(element, index, goalState, boardSize) -> int:
	return abs(index % boardSize - getConversion(element)%boardSize)

def getConversion(element) -> int:
	if 64 < ord(element) < 71:
		return 14 - abs(int(element, 16) - int("F", 16))
	else:
		return int(element) - 1