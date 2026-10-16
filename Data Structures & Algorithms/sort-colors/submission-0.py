class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        freq = [0]*3

        for i in nums:
            if i == 0:
                freq[0] += 1
            elif i == 1:
                freq[1] += 1
            else:
                freq[2] += 1
        nums2 = []
        j = 0
        for i in freq:
            nums2 += [j] * i
            j += 1


        nums[::] = nums2[::]
                

        