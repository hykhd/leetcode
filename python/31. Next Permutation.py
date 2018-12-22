class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return

        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def reverse(nums, i, j):
            while (i < j):
                swap(nums, i, j)
                i += 1
                j -= 1

        j = n - 2
        while j >= 0:
            if nums[j] < nums[j + 1]:
                break
            j -= 1
        print(j)
        if j == -1:
            reverse(nums, 0, n-1)
            print(nums)
            return
        i = j
        while i < n - 1:
            if nums[i+1] <= nums[j]:
                break
            i += 1
        print(i)
        swap(nums, j, i)
        reverse(nums, j + 1, n - 1)
        print(nums)


sol = Solution()
nums = [1,5,1]
sol.nextPermutation(nums)