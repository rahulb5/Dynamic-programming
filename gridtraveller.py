#You are a traveller starting at the top left corner of a grid. You goal is to reach the bottom right corner 
#of the grid. You can travel only down and right. How many ways you can reach the bottom?

def gridtraveller(m,n, memo = {}):
    #Checking for base cases
    if m == 0 or n == 0:
        return 0
    elif m == 1 and n == 1:
        return 1
    #checking if the node is already evaluated and the value for m,n == n,m
    key = str(m) + ',' + str(n)
    key2 = str(n) + ',' + str(m)
    if key in memo:
        return memo[key]
    elif temp2 in memo:
        return memo[key2]
    
    #store in the dictionary
    memo[key] = gridtraveller(m - 1, n, memo) + gridtraveller(m, n-1, memo)
    return memo[key]



print(gridtraveller(2,3))
print(gridtraveller(9,9))
print(gridtraveller(18,18))
