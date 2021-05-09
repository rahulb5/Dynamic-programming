#canSum(targetSum, numbers) takes in two arguments, targetSum: the number to be generated and numbers: the 
#the list of numbers and returns a boolean if it is possible to generate targetSum from numbers
#you can use numbers as many times as you need and the unmbers are non negative

def canSum(targetSum, numbers, memo = {}):
    #check if the targetSum has already been encountered
    if targetSum in memo:
        return memo[targetSum]
    #base cases
    if targetSum == 0:
        return True
    elif targetSum < min(numbers):
        return False
    #branching out the targetSum by subtracting all the elements in numbers from targetSum
    for i in numbers:
        remainder = targetSum - i
        temp = canSum(remainder, numbers, memo)
        #if it is possible to generate, return True
        if temp == True:
            memo[remainder] = True
            return True
    #if can't get the sum, return false
    memo[targetSum] = False
    return False

a = [14,7]

print(canSum(300,a))