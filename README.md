# CSCI 164 Project 1  
### Ryan Anderson  
  
This repository contains the code for the following algorithms:  
    * Breadth-First Search  
    * Depth-First Search  
    * Iterative-Deepening Depth-First Search  
    * A* w/ Out-Of-Place, and Manhattan Distance Heuristics  
    * Iterative Deepening A* w/ Out-Of-Place, and Manhattan Distance Heuristics  


**Directions:** 
The controller file contains the algorithms to execute. It will read a file of containing
a number of states. By Default, it will solve for 123456780 and 123456789ABCDEF0 when the 
problem states are 3x3 or 4x4, respectively.  
  
Upon running Controller.py, it will ask for an input file. This will preferably be a text file, 
with each of the state inputs being separated by newlines (\n). It will then ask for an 
output file designation. It will create/overwrite the file designated, and will output
a csv containing: Function Name, Final State, Number of Expanded Nodes, Action List, Path Cost, and Manhattan Distance of the Original state. If a function fails, the output will contain only: Function Name, Final State, Number of Expanded Nodes, where
'Final State' is represented as "Failure"  
  
Controller.py will run all the algorithms on a set of input states, and output the measured metrics to a file. 
Interactive.py will ask for State and Action List, and will then apply the actions to the state and output the result to the console  


**Note**  
Due to memory constraints, certain algorithms were modified to allow more efficient use of memory, or to cut off when too 
much memory was used. Others, such as Iterative Deepening were modified to prevent the re-expansion of previously explored 
nodes, in an effort to reduce runtime to an acceptable limit.





