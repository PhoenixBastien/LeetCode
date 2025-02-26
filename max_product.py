def max_product(nums: list[int]) -> int:
    max_prod = nums[0]
    curr_prod = 0
    for num in nums:
        curr_prod = max(num, curr_prod * num)
        max_prod = max(max_prod, curr_prod)
    return max_prod

nums = [2,3,-2,4]
print(max_product(nums))
nums = [-2,0,-1]
print(max_product(nums))