# Conway's Game of Life:
A program to calculate the next generation of [Conway's game of life](http://en.wikipedia.org/wiki/Conway%27s_Game_of_Life),
given any starting position. You start with a two dimensional grid
of cells, where each cell is either alive or dead. The grid is finite,
and no life can exist off the edges. When calculating the next generation
of the grid, follow these four rules:

1. Any live cell with fewer than two live neighbours dies,as if caused by underpopulation.
2. Any live cell with more than three live neighbours dies,as if by overcrowding.
3. Any live cell with two or three live neighbours lives on to the next generation.
4. Any dead cell with exactly three live neighbours becomes a live cell.

Examples: * indicates live cell, . indicates dead cell

##Hint:
=======
A particular cell has eight cells in a [Moore neighbourhood](http://en.wikipedia.org/wiki/Moore_neighborhood),as illustrated in the following diagram:

| (i-1,j-1) | (i-1,j)  | (i-1,j+1) |
|  (i,j-1)  |  (i,j)   |  (i,j+1)  |
| (i+1,j-1) | (i+1,j)  | (i+1,j+1) |

