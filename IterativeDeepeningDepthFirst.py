#Iterative Deepening Depth First Search

from Problem import Problem
from Node import Node 
import queue

def depth_first_search_modified(problem, limit):
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
		elif node.path_cost + 1 > limit:
			continue
		elif not reached.get(hState):
			nodesExpanded += 1
			reached[hState] = True
			for child in problem.expandNode(node):
				frontier.put(child)
	return (limit, nodesExpanded)
	
def iterative_deepening_w_depth_first_search(problem, max_depth):
	for i in range(1, max_depth):
		(node, nodesExpanded) = depth_first_search_modified(problem, i)
		if not node == i:
			return (node, nodesExpanded)
	return (Node("Failure", None, None, None, None), nodesExpanded)

