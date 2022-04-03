# A* Search algorithm using heuristics: Out of Place, Manhattan

#Python allows functions to be treated as objects so pass the huerisitc function as an arguement.
# By default, each heuristic function takes state, and goal as parameters
from Problem import Problem
from Node import Node 
from queue import PriorityQueue
import heuristics

def a_star_search_with_heuristic(problem, heuristic):
	node = Node(problem.initial[:], None, "", 0, problem.initial.index("0"))
	frontier = PriorityQueue(0)
	frontier.put((node.path_cost + heuristic(node.state, problem.goalState), node.path_cost, node))
	reached = {''.join(node.state): 0 }
	nodesExpanded = 0

	while not frontier.empty():
		(val, val2, node) = frontier.get()
		if problem.isGoal(node.state):
			return (node, nodesExpanded)
		nodesExpanded += 1
		for child in problem.expandNode(node):
			hState = ''.join(child.state)
			if not reached.get(hState) or child.path_cost < reached.get(hState):
				reached[hState] = child.path_cost
				frontier.put((child.path_cost + heuristic(child.state, problem.goalState), child.path_cost, child))
	return (Node("Failure", None, None, None, None), nodesExpanded)
