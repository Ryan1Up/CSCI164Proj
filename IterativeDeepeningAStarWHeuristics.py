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


def interative_deepening_w_a_star_heuristic(problem, heuristic, limit):
	for i in range(1, limit):
		(node, nodesExpanded) = a_star_search_with_heuristic_and_limit(problem, heuristic, limit)
		if not node == i:
			return (node, val)
	return (Node("Failure", None, None, None, None), nodesExpanded)


orig = "087654321"

p = Problem(orig, "123456780")

(n1, e1) = a_star_search_with_heuristic_and_limit(p, get_out_of_place, 30)
(n2, e2) = a_star_search_with_heuristic_and_limit(p, get_manhattan_distance, 30)

Problem.printSolutionMetrics(n1, e1, "interative_deepening_w_a_star_heuristic: get_out_of_place", orig)
print()
Problem.printSolutionMetrics(n2, e2, "interative_deepening_w_a_star_heuristic: get_manhattan_distance", orig)