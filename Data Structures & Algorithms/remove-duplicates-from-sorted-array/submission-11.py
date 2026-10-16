class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr = sorted(set(nums))
        nums[0:len(arr)] = arr
        return len(arr)