def max_subarray(nums: list[int]) -> int:
    max_sum = float('-inf')
    curr_sum = 0
    for num in nums:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum
    
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))
nums = [1]
print(max_subarray(nums))
nums = [5,4,-1,7,8]
print(max_subarray(nums))