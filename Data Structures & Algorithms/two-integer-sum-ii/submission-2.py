class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mydict = {}
        diff = 0
        diff_pos = 0
        arr = []
        for i,num in enumerate(numbers):
            diff = target - num
            if diff in mydict:
                diff_pos = numbers.index(diff) + 1
                arr.append(i+1)
                arr.append(diff_pos)
                return sorted(arr)
            else:
                mydict[num] = i
        return []

        