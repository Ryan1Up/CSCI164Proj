import math
from Problem import Problem


def __main__(): 

	while True:
		state = input("Enter a State>: ")
		if state == "-1":
			break

		sequence = input("Enter an Action Sequence Using udlr>: ")

		state = list(state)
		sequence = list(sequence)

		Problem.executeActionList(state, sequence)

		print("\nResult: ", ''.join(state))

__main__()