def two_sum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num

        if complement in nums[i + 1:]:
            return [i, i + 1 + nums[i + 1:].index(complement)]
            
nums = [2,7,11,15]
target = 9
print(two_sum(nums, target))
nums = [3,2,4]
target = 6
print(two_sum(nums, target))
nums = [3,3]
target = 6
print(two_sum(nums, target))