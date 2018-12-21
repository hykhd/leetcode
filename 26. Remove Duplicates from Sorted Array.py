class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2: return n
        i = 0
        j = 1
        while j < n:
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            j += 1
        # print(nums[:i+1])
        return i + 1


sol = Solution()
nums = [0, 0, 0, 1, 2, 3, 4, 5, 6, 6, 7, 8]
print(sol.removeDuplicates(nums))