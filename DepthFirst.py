#Depth First Search Algo

from Problem import Problem
from Node import Node 
import queue

def depth_first_search(problem):
	node = Node(problem.initial[:], None, "", 0, problem.initial.index("0"))
	frontier = queue.LifoQueue(0)
	frontier.put(node)
	reached = {}
	nodesExpanded = 0
	while not frontier.empty():
		node = frontier.get()
		hState = ''.join(node.state)
		if problem.isGoal(node.state):
			return (node, nodesExpanded)
		elif node.path_cost + 1 > 30:
			continue
		elif not reached.get(hState):
			if(nodesExpanded >= 2000000):
				break
			nodesExpanded += 1
			reached[hState] = True
			for child in problem.expandNode(node):
				frontier.put(child)
	return (Node("Failure", None, None, None, None), nodesExpanded)