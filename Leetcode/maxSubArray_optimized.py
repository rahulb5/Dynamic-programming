#https://leetcode.com/problems/maximum-subarray/
def maxSubArray(nums):
    
    max_sum = nums[0]
    cur_sum = 0
    for i in nums:
        cur_sum = cur_sum + i
        if cur_sum < i:
            cur_sum = i
        if cur_sum > max_sum:
            max_sum = cur_sum
#        print(max_sum)
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))
