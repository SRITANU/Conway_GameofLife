#! /usr/bin/python
# Author - Sritanu Chakraborty
# Email - sritanu25@gmail.com
# Date - 21st Jan,2015

"""
A program to calculate the next generation of Conway's game of life,
given any starting position. You start with a two dimensional grid
of cells, where each cell is either alive or dead. The grid is finite,
and no life can exist off the edges. When calculating the next generation
of the grid, follow these four rules:

1. Any live cell with fewer than two live neighbours dies,
   as if caused by underpopulation.
2. Any live cell with more than three live neighbours dies,
   as if by overcrowding.
3. Any live cell with two or three live neighbours lives
   on to the next generation.
4. Any dead cell with exactly three live neighbours becomes
   a live cell.

Examples: * indicates live cell, . indicates dead cell

"""

import random
import time


def generate_random_pattern(cols, rows, pattern_array):
    """
    This function generates and returns a random patterned array,if empty.
    Otherwise,it substitutes '.' in place of 0(dead cells) and '*' in place
    of 1(live cells).
    """

    # When the program is run for the first time the pattern array is empty
    if pattern_array == []:
        for i in range(0, rows):
            pat_row = []
            for j in range(0, cols):
                # The cells on the top,right,bottom,left cells are always dead
                if (i == 0 or j == 0 or (i == rows - 1) or (j == cols - 1)):
                    pat_row += ['.']
                else:
                    # Generates a random integer either 1 or 0.
                    # If its 0 then the pattern is '.',if its 1 then its '*'.
                    r = random.randint(0, 1)
                    if r == 0:
                        pat_row += ['.']
                    else:
                        pat_row += ['*']
            pattern_array += [pat_row]
    # When the program is run for second or more generations,the pattern array
    # constitues of zeros and ones which are converted to '*' and '.'
    # respectively
    else:
        for i in range(0, rows):
            for j in range(0, cols):
                # The cells on the top,right,bottom,left cells are always dead
                if (i == 0 or j == 0 or (i == rows - 1) or (j == cols - 1)):
                    pattern_array[i][j] = '.'
                else:
                    # If its 0 then the pattern is '.',if its 1 then its '*'.
                    if pattern_array[i][j] == 0:
                        pattern_array[i][j] = '.'
                    else:
                        pattern_array[i][j] = '*'

    return pattern_array


def print_twodimensional_pattern(pattern_array):
    """
    This function prints the pattern array in a two dimensional form
    """

    for row in pattern_array:
        for i in row:
            print i,
        print


def pattern_to_binary_converter(cols, rows, pattern_array):
    """
    This function converts a patterned array into an array consisting
    of zeros,ones and crosses and returns it.
    '.' = 0
    '*' = 1
    '.'(Outside most dead cells-top,right,left,bottom) = 'x'
    """

    for i in range(rows):
        for j in range(cols):
            if (i == 0 or j == 0 or (i == rows - 1) or (j == cols - 1)):
                pattern_array[i][j] = "x"
            elif pattern_array[i][j] == '.':
                pattern_array[i][j] = 0
            else:
                pattern_array[i][j] = 1
    return pattern_array


def next_generation_pattern_generator(cols, rows, binary_array, next_generation):
    """
    This function generates and returns the next generation pattern array based
    on the rules of the game.
    """

    # List comprehension to initiate the next_generation_pattern with zeros
    next_generation = [([0] * cols) for row in range(rows)]
    # Need to process only the cells except the outside most cells
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            next_generation[i][j] = process_neighbours(i, j, binary_array)

    return next_generation


def process_neighbours(a, b, current_pattern):
    """
    This function decides the value of the cell for the next_generation pattern
    and returns it to the next_generation_pattern_generator function.

    The following are the rules:
    1. Any live cell with fewer than two live neighbours dies,
       as if caused by underpopulation.
    2. Any live cell with more than three live neighbours dies,
       as if by overcrowding.
    3. Any live cell with two or three live neighbours lives
       on to the next generation.
    4. Any dead cell with exactly three live neighbours becomes
       a live cell.

    """

    count = count_neighbours(a,b,current_pattern)
    
    # Condition 1
    if current_pattern[a][b] == 1 and count < 2:
        return 0
    # Condition 2
    if current_pattern[a][b] == 1 and count > 3:
        return 0
    # Condition 4
    if current_pattern[a][b] == 0 and count == 3:
        return 1
    # Condition 3
    else:
        return current_pattern[a][b]

def count_neighbours(a,b,current_pattern):
    """
    This function counts the neighbours of a particular cell.

    A particular cell has eight cells in a Moore neighbourhood,as illustrated
    in the following diagram:

    (i-1,j-1) | (i-1,j) | (i-1,j+1)
    -------------------------------
     (i,j-1)  |  (i,j)  |  (i,j+1)
    -------------------------------
    (i+1,j-1) | (i+1,j) | (i+1,j+1)

    So,the two loops runs from (i-1) to (i+1) and (j-1) to (j+1) to determine
    the postion and value of the neighbourhood cells,considering the fact that
    the own value of a particular cell should not be taken into account while
    counting and processing the neighbourhood cells.
    """
    count = 0
    for j in range(b - 1, b + 2):
        for i in range(a - 1, a + 2):
            if not(i == a and j == b):
                if current_pattern[i][j] != 'x':
                    count += current_pattern[i][j]

    return count


def main():
    """
    The main function where the user is asked to input the no.of rows,columns
    and generations he/she wants the game to perform on.
    """
    while True:
        print "Welcome to Conway's Game of Life"
        print "================================"

        try:
            rows = int(raw_input("Enter the no.of rows > ").replace(" ",''))
        except ValueError:
            print "Oops!  That was no valid number.  Try again..."
            continue
    
        try:
            columns = int(raw_input("Enter the no.of columns > ").replace(" ",''))
        except ValueError:
            print "Oops!  That was no valid number.  Try again..."
            continue

        try:
            generations = int(raw_input("Enter the no.of generations > ").replace(" ",''))
        except ValueError:
            print "Oops!  That was no valid number.  Try again..."
            continue

        time_delay = 0.2
        current_generation = []
        next_generation = []

        if rows > 0 and columns > 0:
            if generations > 0:
                for i in range(generations):
                    print "Conway's Game of Life -- Generation " + str(i + 1)
                    print_twodimensional_pattern(
                        generate_random_pattern(columns, rows, current_generation))
                    binary_array = pattern_to_binary_converter(
                        columns, rows, current_generation)
                    next_generation = next_generation_pattern_generator(
                        columns, rows, binary_array, next_generation)
                    time.sleep(time_delay)
                    current_generation, next_generation = next_generation, current_generation
            else:
                print "Please input positive integer for number of generations"
        else:
            print "Please input postive integer number for rows and columns"

        replay =  raw_input("Do you want to play again(y/n) ? > ").strip()
        if replay.lower() == 'n' or replay.lower() == 'no':
            break

if __name__ == '__main__':
    main()
