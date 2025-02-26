def max_area(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        curr_area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, curr_area)
        print(f'left: {left}, right: {right}, curr_area: {curr_area}, max_area: {max_area}')

        if height[left] < height[right]:
            
            left += 1
        else:
            right -= 1
    return max_area
    
height = [1,8,6,2,5,4,8,3,7]
print(max_area(height))