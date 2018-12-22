class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums) - 1
        ans = [-1, -1]
        if not nums:
            return ans
        while (start <= end):
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
        # print(end + 1)
        ans[0] = end + 1 if end + 1 <= len(nums) - 1 and nums[
            end + 1] == target else -1
        start = 0
        end = len(nums) - 1
        while (start <= end):
            mid = (start + end) // 2
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
        ans[1] = start - 1 if start > 0 and nums[start - 1] == target else -1
        return ans


nums = [1]
target = 1
sol = Solution()
print(sol.searchRange(nums, target))
