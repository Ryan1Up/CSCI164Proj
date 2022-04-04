# Iterative Deepening with A* using Heuristics
from Problem import Problem
from Node import Node 
from queue import PriorityQueue
from heuristics import get_out_of_place, get_manhattan_distance

def a_star_search_with_heuristic_and_limit(problem, heuristic, limit):
	node = Node(problem.initial[:], None, "", 0, problem.initial.index("0"))
	frontier = PriorityQueue(0)
	frontier.put((node.path_cost + heuristic(node.state, problem.goalState), node.path_cost, node))
	reached = {''.join(node.state): 0 }
	nodesExpanded = 0

	while not frontier.empty():
		(val, val2, node) = frontier.get()
		if problem.isGoal(node.state):
			return (node, nodesExpanded)
		if node.path_cost + 1 > limit:
			return (limit, nodesExpanded)
		nodesExpanded += 1
		for child in problem.expandNode(node):
			hState = ''.join(child.state)
			if not reached.get(hState) or child.path_cost < reached.get(hState):
				reached[hState] = child.path_cost
				frontier.put((child.path_cost + heuristic(child.state, problem.goalState), child.path_cost, child))
	return (Node("Failure", None, None, None, None), nodesExpanded)


def iterative_deepening_w_a_star_heuristic(problem, heuristic, max_depth):
	for i in range(1, max_depth):
		(node, nodesExpanded) = a_star_search_with_heuristic_and_limit(problem, heuristic, i)
		if (isinstance(node, Node)) or not i == node:
			return (node, nodesExpanded)
	return (Node("Failure", None, None, None, None), nodesExpanded)
