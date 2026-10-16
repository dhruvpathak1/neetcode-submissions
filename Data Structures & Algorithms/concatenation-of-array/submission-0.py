class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = 2*len(nums)
        ans = [0 for _ in range (0,l)]
        count = 0
        for i in nums:
            ans[count], ans[count+len(nums)] = i,i
            count += 1
        return ans