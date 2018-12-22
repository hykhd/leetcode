class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.index(needle) if needle in haystack else -1


sol = Solution()
haystack = "aaaaaa"
needle = "aaa"
print(sol.strStr(haystack, needle))
