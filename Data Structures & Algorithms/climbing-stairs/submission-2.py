class Solution:

    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n+1)

        def combo(n):
            if 0 <= n <= 1:
                return 1
            elif memo[n] != -1:
                return memo[n]
            else:
                memo[n] = combo(n-1) + combo(n-2)
                return memo[n]
        return combo(n)