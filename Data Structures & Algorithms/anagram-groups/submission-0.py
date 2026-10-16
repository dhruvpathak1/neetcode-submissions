class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = {}
        for i in strs:
            key = tuple(sorted(i))
            if key not in anag.keys():
                anag[key] = [i]
            else:
                anag[key].append(i)
        return list(anag.values())