class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles = sorted(piles)
                
        l = 1
        r = max(piles)
        minK = r

        def calcHours(bananas: int)->int:
            time = 0
            for pile in piles:
                if pile <= bananas:
                    time += 1
                elif pile % bananas == 0:
                    time += int(pile//bananas)
                else:
                    time += int(pile//bananas) + 1
            return time

        while l<=r:
            mid = (l+r)//2
            result = calcHours(mid)
            if result > h:
                l = mid+1
            else:
                minK = mid
                r = mid-1
        
        return minK