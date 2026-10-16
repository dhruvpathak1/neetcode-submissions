class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) <=1:
            return False
        else:
            for i in s:
                if i == '(' or i == '{' or i == '[':
                    stack.append(i)
                else:
                    if stack:
                        ele = stack.pop()
                        if i == ')' and ele == '(':
                            continue
                        elif i == ']' and ele == '[':
                            continue
                        elif i == '}' and ele == '{':
                            continue
                        else:
                            return False
                    else:
                        return False
            if stack:
                return False
            else:
                return True


        