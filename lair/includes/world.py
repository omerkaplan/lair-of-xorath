#import includes.globals as globals # globals variables, most notebly 'done' for game over
import random
import numpy


# Generate world with monsters (encounter type 1) in it
# initial player position is in the global vars
# when calling out a coordinate, it's grid[row][column]

grid = [[0 for x in range(7)] for y in range(6)] # generates a blank world map
grid[0][3] = 99 # entry way
grid[random.randint(1,5)][random.randint(0,6)] = 98 # xorath encounter

#generate encounters

for column in grid:
    for i, item in enumerate(column):
        if item == 0:
           column[i] = numpy.random.choice(numpy.arange(1, 7), p=[0.2, 0.25, 0.1, 0.2, 0.05, 0.2])
