class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        # Handle empty lists to prevent errors, and append the initial single-element state
        if not pairs:
            return []
        
        l1 = [pairs[:]]
        
        for i in range(1, len(pairs)):
            j = i
            while j > 0 and pairs[j-1].key > pairs[j].key:
                pairs[j], pairs[j-1] = pairs[j-1], pairs[j]
                j -= 1
            l1.append(pairs[:])
        
        return l1