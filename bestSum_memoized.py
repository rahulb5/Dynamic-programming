#bestSum(targetSum, numbers) takes two arguments, the sum that you want and numbers, the array of numbers from
#which the sum is to be made. You need to return the shortest array possible that adds to the targetSum
##all numbers are positive and you can reuse the numbers

def bestSum(targetSum, numbers, memo = None):
    #checking if the targetSum has previously been encountered
    if memo == None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    #defining the base cases
    if targetSum == 0:
        return []
    if targetSum < min(numbers):
        return None
    
    answer = None
    #branching the targetSum into trees
    for i in numbers:
        remainder = targetSum - i
        temp = bestSum(remainder, numbers, memo)
        if temp != None:
            temp = temp.copy()
            temp.append(i)
            if answer == None or len(temp) < len(answer) :
                answer = temp
    memo[targetSum] = answer
    return answer


print(bestSum(7,[5,3,4,7]))
print(bestSum(8, [2,3,5]))
print(bestSum(8,[1,4,5]))
print(bestSum(100, [1,5,25]))