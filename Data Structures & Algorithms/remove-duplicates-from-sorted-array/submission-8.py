class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums2 = sorted(set(nums))
        k = len(nums2)
        nums[:len(nums2)] = nums2
        return k
        