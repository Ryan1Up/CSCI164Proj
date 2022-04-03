#Breadth First Search Algo

"""
Breadth First ignored Path Costs and Huerisitics while searching through the problem space.

It uses a FIFO Queue structure to maintain which nodes are to be expanded next, and also
uses a dictionary/hashtable to remember which states have already been seen.

"""
from Problem import Problem
from Node import Node 
import queue


def breadth_first_search(problem):
	node = Node(problem.initial[:], None, "", 0, problem.initial.index("0"))
	frontier = queue.Queue(0)
	frontier.put(node)
	reached = {''.join(node.state) : 1}
	nodesExpanded = 0
	while not frontier.empty():
		node = frontier.get()
		nodesExpanded += 1
		for child in problem.expandNode(node):
			hState = ''.join(child.state)
			if problem.isGoal(child.state):
				return (child, nodesExpanded)
			if not reached.get(hState):
				reached[hState] = child.path_cost
				frontier.put(child)
	return (Node("Failure", None, None, None, None), nodesExpanded)
