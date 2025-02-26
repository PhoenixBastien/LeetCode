def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    nums1[m:] = nums2
    nums1.sort()

nums1, m, nums2, n = [1,2,3,0,0,0], 3, [2,5,6], 3
merge(nums1, m, nums2, n)
print(nums1)

nums1, m, nums2, n = [1], 1, [], 0
merge(nums1, m, nums2, n)
print(nums1)

nums1, m, nums2, n = [0], 0, [1], 1
merge(nums1, m, nums2, n)
print(nums1)