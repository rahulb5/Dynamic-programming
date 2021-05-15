#https://leetcode.com/problems/unique-paths-ii/submissions/

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
               
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1:
            return 0
        
        def obstacle_path(i, j, memo = None):            
            if memo == None:
                memo = {}
            
            curr_pos = str(i) + ',' + str(j)   
            if curr_pos in memo:
                return memo[curr_pos]
            if i == m or j == n:
                return 0
            if i == m-1 and j == n-1:
                if obstacleGrid[i][j] == 1:
                    return 0
                return 1
            
            down_step = 0
            right_step = 0
        
            if i+1 != m and obstacleGrid[i+1][j] != 1:
                down_step = obstacle_path(i+1, j, memo)
            if j+1 != n and obstacleGrid[i][j+1] != 1:
                right_step = obstacle_path(i, j+1, memo)
            
            memo[curr_pos] =  down_step + right_step
            return memo[curr_pos]
    
        return obstacle_path(0,0)
            
