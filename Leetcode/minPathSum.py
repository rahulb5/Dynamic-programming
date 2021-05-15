#https://leetcode.com/problems/minimum-path-sum/

class Solution(object):
    def minPathSum (self, grid):
    
        m = len(grid)
        n = len(grid[0])
        
        if m == 1:
            return sum(grid[0])
        
        def minPath(i,j, memo = None):
            if memo == None:
                memo = {}
        
            curr_pos = str(i) + ','  + str(j)
            if curr_pos in memo:
                return memo[curr_pos]
        
            if i == m or j == n:
                return 40000000
            if i == m-1 and j == n-1:
                return grid[i][j]
        
            cur_sum = min(minPath(i+1,j,memo),minPath(i,j+1,memo))
            memo[curr_pos] = cur_sum + grid[i][j]
            return memo[curr_pos]
    
        return minPath(0,0)
