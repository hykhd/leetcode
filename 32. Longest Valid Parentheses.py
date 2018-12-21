class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0 for i in range(n + 1)]
        for index, pair in enumerate(s, start=1):
            if pair == ')':
                if index - 2 >= 0 and s[index-2] == '(':
                    dp[index] = dp[index - 2] + 2
                elif index - dp[index - 1] - 2 >= 0 and s[index - dp[index - 1] - 2] == '(':
                    dp[index] = dp[index - dp[index - 1] - 2] + dp[index-1] +2
        print(dp)
        return max(dp)


s = "(()))())("

sol = Solution()
print(sol.longestValidParentheses(s))