# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

The traditional sudoku game is played on a 9×9 board and has the following rules simple rules: each row, column and sub-matrix must be a permutation of the numbers 1 . . . 9. The sub-matrices are simply the 3×3 matrices that tile the larger board

In the task, I refer to the entire 81-square 'play area' as the grid. The vertical elements are rows, the column elements are columns, and the nine 3x3 units in the grid are boxes. Each square belongs to 3 units: a row, a column and a box. Each square has twenty peers, or other squares that belong to the same units. Peers to a square cannot contain the same value as that square. However, 17 squares on the diagonal belong to 4 units a row, a column, a box and a diagonal unit.

Following the naming convention, each square ("box") has its own label. The rows will be labelled by the letters A, B, C, D, E, F, G, H, I and the columns will be labelled by the numbers 1, 2, 3, 4, 5, 6, 7, 8, 9.. (e.g. the units for the first row are A1, A2, A3... A9, and the last column A9, B9, C9, ..., I9. The units and peers of each square are contained in dictionaries, with the square's label as key and lists of the squares' units (or peers) as values. At the start of the program, it computes a dictionary containing all the possible values for each square, and the possible values of this dictionary are gradually eliminated to arrive at the solution.


# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: The naked twins strategy is used when two squares are found within the same unit, containing only the same two possible digits. This means that no other square in the same unit can contain either of the values, and so the values can safely be eliminated from all the other squares in the unit.

For example : given {'F3': '23', 'I3':'23', ...}, we can conclude that 2 and 3 must be in F3 and I3 (although we don't know which is where), and we can therefore eliminate 2 and 3 from every other square in the 3 column unit in this case is D3 and E3.


Image(filename='nakedtwin.png', width=500, height=500)

![alt tag](https://raw.githubusercontent.com/username/projectname/branch/path/to/img.png)

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: In this task, I added 2 more digonal units {'A1', 'B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8', 'I9'} and {'A9', 'B8', 'C7', 'D6','E5', 'F4', 'G3', 'H2', 'I1'}. Then  two heuristic strategies, the 'naked twins' strategy and recursive search strategy are applied to find the final solution.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.