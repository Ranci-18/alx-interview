#!/usr/bin/python3
"""Island perimeter"""


def island_perimeter(grid):
    """
    function to calculate the perimeter
    of an island
    """
    perimeter = 0
    if not grid or not grid[0]:
        return perimeter

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4
                if j + 1 < len(grid[i]) and grid[i][j + 1] == 1:
                    perimeter -= 2
                if i + 1 < len(grid) and grid[i + 1][j] == 1:
                    perimeter -= 2

    return perimeter
