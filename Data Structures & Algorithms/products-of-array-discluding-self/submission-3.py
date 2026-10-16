class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = 1
        post = 1
        arr = []
        for i in range (0, len(nums)):
            if i == 0:
                arr.append(pre)
            else:
                pre *= nums[i-1]
                arr.append(pre)

        print(arr)
        
        for i in range (len(nums)-1, -1, -1):
            print(i)
            if i == (len(nums)-1):
                arr[i] *= 1
            else:
                post *= nums[i+1]
                arr[i] *= post

        return arr
        