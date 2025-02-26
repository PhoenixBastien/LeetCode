def longest_consecutive(nums: list[int]) -> int:
    if len(nums) in {0, 1}:
        return len(nums)
    sorted_nums = sorted(nums)
    max_count = 1
    curr_count = 1
    for i in range(1, len(sorted_nums)):
        if sorted_nums[i] == sorted_nums[i-1] + 1:
            curr_count += 1
        else:
            curr_count = 1
        if curr_count > max_count:
            max_count = curr_count
    return max_count
    
nums = [0,3,7,2,5,8,4,6,0,1]
print(longest_consecutive(nums))
nums = [100,4,200,1,3,2]
print(longest_consecutive(nums))