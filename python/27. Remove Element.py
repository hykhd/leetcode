class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = 0
        n = len(nums)
        if not n:
            return nums
        while j < n:
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
            # i += 1
        print(nums[:i])
        return i


sol = Solution()
nums = []
val = 3
print(sol.removeElement(nums, val))
