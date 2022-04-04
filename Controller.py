# Main Controller File	

import math
from Problem import Problem
from BreadthFirst import breadth_first_search
from DepthFirst import depth_first_search
from IterativeDeepeningDepthFirst import iterative_deepening_w_depth_first_search
from AStarWHeuristics import a_star_search_with_heuristic
from IterativeDeepeningAStarWHeuristics import iterative_deepening_w_a_star_heuristic
from heuristics import get_out_of_place, get_manhattan_distance

def execute_search_from_input(inputFileName: str) -> str:
	retString = ""

	lines = []

	with open(inputFileName, "r") as f:
		lines = f.readlines()

	solution = None

	for line in lines:

		if not solution:
			solution = ("123456780", "123456789ABCDEF0")[math.sqrt(len(line)) == 4]

		line = line.strip()

		problem = Problem(line, solution)

		(n, e) = breadth_first_search(problem)
		retString += get_csv_metrics(n, e, "breadth_first_search", line)

		# (n, e) = depth_first_search(problem)
		# retString += get_csv_metrics(n, e, "depth_first_search", line)

		# (n, e) = iterative_deepening_w_depth_first_search(problem, 50)
		# retString += get_csv_metrics(n, e, "iterative_deepening_w_depth_first_search", line)

		# (n, e) = a_star_search_with_heuristic(problem, get_out_of_place)
		# retString += get_csv_metrics(n, e, "a_star_search_with_heuristic: get_out_of_place", line)

		# (n, e) = a_star_search_with_heuristic(problem, get_manhattan_distance)
		# retString += get_csv_metrics(n, e, "a_star_search_with_heuristic: get_manhattan_distance", line)

		# (n, e) = iterative_deepening_w_a_star_heuristic(problem, get_out_of_place, 50)
		# retString += get_csv_metrics(n, e, "iterative_deepening_w_a_star_heuristic: get_out_of_place", line)

		# (n, e) = iterative_deepening_w_a_star_heuristic(problem, get_manhattan_distance, 50)
		# retString += get_csv_metrics(n, e, "iterative_deepening_w_a_star_heuristic: get_manhattan_distance", line)

		print(retString, "\n")
		break
	return retString + " \n"

def get_csv_metrics(node, expandedNodes, functionName, originalState) -> str: 

	nodePath = Problem.buildNodePath(node)
	retString = ""
	retString += "{0},".format(functionName)
	retString += "{0},".format(''.join(node.state))
	retString += "{0}" .format(expandedNodes)
	if node.state != "Failure":
		retString += ","
		retString += "{0},".format(''.join(nodePath))
		retString += "{0},".format(len(nodePath))
		retString += "{0}".format(get_manhattan_distance(originalState, ''.join(node.state)))
	retString += "\n "

	return retString

def write_output_to_file(outputFileName, outputString):
	with open(outputFileName, "w") as f:
		f.write("Function Name, Final State, Nodes Expanded, Move Set, Path Cost, Heuristic\n")
		f.write(outputString)
		f.close()

def execute():
	inputFile = input("File To Execute: ")
	outputFile = input("File to Write To: ")

	if ".csv" not in outputFile:
		outputFile += ".csv"

	write_output_to_file(outputFile, execute_search_from_input(inputFile))


execute()