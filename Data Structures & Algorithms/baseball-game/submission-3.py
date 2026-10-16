class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []
        
        for val in operations:
            if val == 'D':
                op = stack[-1]
                stack.append(op*2)
            elif val == '+':
                op1 = stack[-1]
                op2 = stack[-2]
                stack.append(op1 + op2)
            elif val == 'C':
                stack.pop()
            else:
                stack.append(int(val))

            print(stack)
        
        return sum(stack)