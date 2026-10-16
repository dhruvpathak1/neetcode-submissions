class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kfreq = {}
        for num in nums:
            if num not in kfreq:
                kfreq[num] = 1
            else:
                kfreq[num] = kfreq[num]+1
        
        klist = []

        while k>0:
            max = 0
            pos = 0
            for key,val in kfreq.items():
                if val > max:
                    max = val
                    pos = key
            klist.append(pos)
            del kfreq[pos]
            k -= 1

            print(max, pos)
            print(klist)
            print(k)
        
        return klist

        