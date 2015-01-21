#! /usr/bin/python

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
	This function generates a random patterned array,if empty.Otherwise,
	it substitutes '.' in place of 0(dead cells) and '*' in place of 1
	(live cells).
	"""
    

    #When the program is run for the first time the pattern array is empty
    if pattern_array == []:
        for i in range(0,rows):
            pat_row = []
            for j in range(0,cols):
            	#The cells on the top,right,bottom,left cells are always dead
                if (i == 0 or j == 0 or (i == rows - 1) or (j == cols - 1)):
                    pat_row += ['.']
                else:
                #Generates a random integer either 1 or 0.
                #If its 0 then the pattern is '.',if its 1 then its '*'.	
                    r = random.randint(0,1)
                    if r == 0:
                        pat_row += ['.']
                    else:
                        pat_row += ['*']
            pattern_array += [pat_row]
    #When the program is run for second or more generations,the pattern array
    #constitues of zeros and ones which are converted to '*' and '.' respectively
    else:
        for i in range(0,rows):
            for j in range(0,cols):
            	#The cells on the top,right,bottom,left cells are always dead
                if (i == 0 or j == 0 or (i == rows - 1) or (j == cols - 1)):
                    pattern_array[i][j]= '.'
                else:
                	#If its 0 then the pattern is '.',if its 1 then its '*'.
                    if pattern_array[i][j] == 0:
                        pattern_array[i][j]= '.'
                    else:
                        pattern_array[i][j]= '*'

    return pattern_array


def print_twodimensional_pattern(pattern_array):
	"""
	This function prints the pattern array in a two dimensional form
	"""
	

	for row in pattern_array:
		for i in row:
			print i,
		print