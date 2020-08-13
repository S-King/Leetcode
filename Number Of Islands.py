from typing import List
'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is
formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011

Output: 3
'''


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        total_islands = 0

        # Need to know the dimensions of the array so I know when there isn't another neighbor to check (edge nodes)
        number_rows = len(grid)
        number_columns = len(grid[0])

        for i in range(0,number_rows):
            for j in range(0,number_columns):
                if grid[i][j] == '1':
                    # Keep a queue of the neighbors to search
                    neighbors = []

                    # once we hit land we need to increment by one island (since we know our grid is surrounded by water)
                    total_islands += 1

                    # Now take this node out of the picture and start the BFS search
                    grid[i][j] = 0

                    # Do BFS we need to enqueue each each of the neighbor nodes then search them
                    # This BFS will continue until we don't have any neighbors with 1's

                    # Check the above neighbor (so long as it isn't on the top row)
                    neighbors.append([i,j])
                    while neighbors:
                        # print(neighbors)
                        # Removing from the zero-th position implements our queue behavior
                        row_index, column_index = neighbors.pop(0)

                        if (row_index-1) >= 0 and grid[row_index-1][column_index] == '1':
                            neighbors.append([row_index-1,column_index])
                            grid[row_index-1][column_index] = 0
                        # Check right neighbor (so long as it isn't the last column)
                        if (column_index+1) < number_columns and grid[row_index][column_index+1] == '1':
                            neighbors.append([row_index,column_index+1])
                            grid[row_index][column_index+1] = 0
                        # Check the bottom neighbor (not last row)
                        if (row_index+1) < number_rows and grid[row_index+1][column_index] == '1':
                            neighbors.append([row_index+1,column_index])
                            grid[row_index+1][column_index] = 0
                        # Finally left neighbor
                        if (column_index-1) >= 0 and grid[row_index][column_index-1] == '1':
                            neighbors.append([row_index,column_index-1])
                            grid[row_index][column_index-1] = 0

        return total_islands




    def numIslands_attemptTwo(self, grid: List[List[str]]) -> int:
        def numIslands(self, grid: List[List[str]]) -> int:
            num_rows = len(grid)
            if num_rows <= 0:
                return 0
            num_cols = len(grid[0])
            num_islands = 0
            for row in range(0, num_rows):
                for col in range(0, num_cols):
                    if grid[row][col] == '1':
                        num_islands += 1
                        grid[row][col] = '0'
                        queue = []
                        queue.append([row, col])
                        while len(queue) > 0:
                            row_and_col = queue.pop(0)
                            r = row_and_col[0]
                            c = row_and_col[1]
                            if r - 1 >= 0 and grid[r - 1][c] == '1':  # down
                                queue.append([r - 1, c])
                                grid[r - 1][c] = '0'
                            if r + 1 < num_rows and grid[r + 1][c] == '1':  # up
                                queue.append([r + 1, c])
                                grid[r + 1][c] = '0'
                            if c - 1 >= 0 and grid[r][c - 1] == '1':  # left
                                queue.append([r, c - 1])
                                grid[r][c - 1] = '0'
                            if c + 1 < num_cols and grid[r][c + 1] == '1':  # right
                                queue.append([r, c + 1])
                                grid[r][c + 1] = '0'
            return num_islands








test = '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
mySolution = Solution()
print(mySolution.numIslands(test))