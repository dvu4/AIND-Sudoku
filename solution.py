assignments = []

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values


    
def naked_twins(values):
    '''A function with the naked twins strategy: If two squares within the same unit contain only
    the same two digits, both digits can be eliminated from all the other squares in that unit.'''
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}
    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    
    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers
    
    solved_boxes = [box for box in values.keys() if len(values[box]) >1 ]
    for box in solved_boxes:
        for unit in units[box]:
            # Searches for peers from the same unit
            for peer in set(unit).intersection(set(peers[box])):
                # If an item in the unit contains the same values as the box (but is not the box itself),
                # a naked pair is identified and those values are removed from all other items in the unit.
                
                #naked_twin_digits = list(set(list(values[peer])).intersection(set(list(values[square]))))
                naked_twin_digits = list(set(list(values[peer])) & set(list(values[box])))
                
                if ((len(naked_twin_digits) == 2) & (len(values[peer]) == 2) & (len(values[box]) == 2)):
                    digit1 = naked_twin_digits[0]
                    digit2 = naked_twin_digits[1]

                    for item in set(unit).difference(set([box, peer])):
                        # If the item is not in the naked twins pair, remove the naked twins' values
                        #print(box , peer, item , values[item], ':',digit1, digit2)
                        if digit1 in values[item]:
                            values[item] = values[item].replace(digit1,'')
                            #print('digit1 is:',type(digit1))
                            #print(box , peer, item , values[item], ':',digit1, digit2)
                            assign_value(values, item, values[item])
                            
                        if digit2 in values[item]:
                            values[item] = values[item].replace(digit2,'')
                            #print('digit2 is:',type(digit2))
                            #print(box , peer, item , values[item], ':',digit1, digit2)
                            assign_value(values, item, values[item])
                            
    
    return values



def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [i+j for i in A for j in B]
    #pass


##################    
rows = 'ABCDEFGHI'
cols = '123456789'

boxes = cross(rows, cols)
    
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
#diagonal_units = [elem for i in range(len(row_units)) for elem in row_units[i]  if elem in column_units[i]]

diagonal_units1 = [row + col for row, col in zip(list(rows), list(cols))]        # [A1,B2,C3,D4,E5,F6,G7,H8,I9]
diagonal_units2 = [row + col for row, col in zip(list(rows), list(cols)[::-1])] # [A9,B8,C7,D6,E5,F4,G3,H2,I1]

unitlist = row_units + column_units + square_units
unitlist.append(diagonal_units1)
unitlist.append(diagonal_units2)

units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)
#################




def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Input: A grid in string form. (i.e '273...98..1....') 
    Output: A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    chars = []
    digits = '123456789'
    for c in grid:
        if c in digits:
            chars.append(c)
        if c == '.':
            chars.append(digits)
    assert len(chars) == 81
    return dict(zip(boxes, chars))
    
    #pass

def display(values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return
    #pass

'''  
def eliminate(values):
    # Write a function that will take as an input, the sudoku in dictionary form,
    # run through all the boxes, applying the eliminate technique,
    # and return the resulting sudoku in dictionary form.
    unsolved_boxes = [box for box in values.keys() if len(values[box]) >1 ]
    
    #print(unsolved_boxes)
    #for i in unsolved_boxes:
    #    print(i, ':', values[i])
    
    #a=[1,2,3,4,5,6,7,8]
    #b=[2,4,1,11,9,12]
    #print(set(a).difference(b)) --> {3, 5, 6, 7, 8}
    
    
    for box in unsolved_boxes:
        new_unsolved_boxes = [i for i in unsolved_boxes if i != box]
        new_peers = list(set(peers[box]).difference(new_unsolved_boxes))
        #print(len(unsolved_boxes))
        #print(len(new_unsolved_boxes))
        #print(len(peers[box]))
        #print(len(new_peers),'\n')
        
        for peer in new_peers:
            if values[peer] in values[box]:
                values[box] = values[box].replace(values[peer], '')
    return values
    #pass
'''    
    
def eliminate(values):
    """
    Go through all the boxes, and whenever there is a box with a value, eliminate this value from the values of all its peers.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit,'')
            assign_value(values, peer, values[peer])
            
           
    return values
    #pass

def only_choice(values):
    """
    Go through all the units, and whenever there is a unit with a value that only fits in one box, assign the value to this box.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    for unit in unitlist:
        for digit in '123456789':
            digit_places  = [box for box in unit if digit in values[box]]
            print(digit, ':', digit_places)
            
            if len(digit_places) == 1:
                values[digit_places[0]] = digit
                assign_value(values, digit_places[0], digit)
                

    return values
    #pass
    
def reduce_puzzle(values):
    """
    Iterate eliminate() and only_choice(). If at some point, there is a box with no available values, return False.
    If the sudoku is solved, return the sudoku.
    If after an iteration of both functions, the sudoku remains the same, return the sudoku.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        
        values = only_choice(values)
        values = naked_twins(values)
        
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values
    #pass

    
def search(values):
    #"Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    # Output: new sudoku if it is solved
    #         False if it is not solved
    
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
        
    # Chose one of the unfilled square s with the fewest possibilities
    n, search_box = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    for digit in values[search_box]:
        new_sudoku = values.copy()
        new_sudoku[search_box] = digit
        attempt = search(new_sudoku)
        
        if attempt:
            return attempt
        

    #pass


   
      
def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    return search(values)

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))
    assign_value(solve(diag_sudoku_grid))
    
    
    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
