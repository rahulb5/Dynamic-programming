#canSum(targetSum, numbers) takes in two arguments, targetSum: the number to be generated and numbers: the 
#the list of numbers and returns an array containing any compbination of elements adding up exactly to 
#targetSum. If there are multiple solutions, return any one
#you can use numbers as many times as you need and the unmbers are non negative
def howSum(targetSum, numbers, memo = None):
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    
    for i in numbers:
        remainder = targetSum - i
        temp = howSum(remainder, numbers, memo)
        if temp != None:
            temp = temp.copy()
            temp.append(i)
            memo[targetSum] = temp
            return memo[targetSum]
        
    memo[targetSum] = None
    return None

a = [7,14]

print(howSum(300,a))
