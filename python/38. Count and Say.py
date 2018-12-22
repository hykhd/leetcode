class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        start = '1'
        for _ in range(n - 1):
            ans = []
            for s in start:
                if not ans or s != ans[-1]:
                    ans.append(1)
                    ans.append(s)
                else:
                    ans[-2] += 1
            # print(ans)
            start = ''.join(str(e) for e in ans)
            # print(start)
        return start


sol = Solution()
n = 5
print(sol.countAndSay(n))