class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for st in strs:
            val = len(st)
            encoded += st
            encoded += '-'

        return encoded

    def decode(self, s: str) -> List[str]:
        str_list = []
        str_list = s.split('-')
        str_list.pop()
        return str_list
