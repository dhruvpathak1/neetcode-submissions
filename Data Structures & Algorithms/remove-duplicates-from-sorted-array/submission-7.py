# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         nums2 = set(nums)
#         nums[:len(nums2)] = sorted(list(nums2))
#         return len(nums)

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique = sorted(set(nums))
        nums[:len(unique)] = unique
        return len(unique)