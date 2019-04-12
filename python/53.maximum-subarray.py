#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (42.60%)
# Total Accepted:    454.5K
# Total Submissions: 1.1M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
#
# Example:
#
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
#
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
#
#
class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        if not nums:
            return 0
        N = len(nums)
        dp = [0] * N  #creat the dp array with the init num
        dp[0] = nums[0]
        for i in range(1, N):
            dp[i] = max(dp[i - 1], 0) + nums[
                i]  #update the dp array , if last one under the 0 . use the 0 + nums.
        return max(dp)


# using dp solution

#   √ Accepted
#   √ 202/202 cases passed (44 ms)
#   √ Your runtime beats 93.75 % of python3 submissions
#   √ Your memory usage beats 5.5 % of python3 submissions (13.8 MB)
