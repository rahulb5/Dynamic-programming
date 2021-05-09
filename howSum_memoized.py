#canSum(targetSum, numbers) takes in two arguments, targetSum: the number to be generated and numbers: the 
#the list of numbers and returns an array containing any compbination of elements adding up exactly to 
#targetSum. If there are multiple solutions, return any one
#you can use numbers as many times as you need and the unmbers are non negative

def howSum(targetSum, numbers, answer = [], memo = {}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < min(numbers):
        return None
    
    for i in numbers:
        remainder = targetSum - i
        temp = howSum(remainder, numbers, answer)
        if temp != None:
            answer.append(i)
            memo[i] = answer
            return memo[i]
        
    memo[targetSum] = None
    return memo[targetSum]

a = [7,14]

print(howSum(300,a))