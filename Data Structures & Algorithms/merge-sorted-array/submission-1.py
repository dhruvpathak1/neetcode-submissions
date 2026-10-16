class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m-1
        j = n-1
        pointer = m+n-1

        while pointer >= 0:
            
            if i < 0:
                nums1[pointer] = nums2[j]
                j -= 1
            elif j < 0:
                nums1[pointer] = nums1[i]
                i -= 1
            elif nums2[j] > nums1[i]:
                nums1[pointer] = nums2[j]
                j -= 1
            else:
                nums1[pointer] = nums1[i]
                i -= 1
            pointer -= 1



        