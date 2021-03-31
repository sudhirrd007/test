# File, 0001_two_sum.py
# #, 1
# Title, Two Sum
# Run Time, 6948 ms
# Difficulty, EASY
# Acceptance rate, 46.7%
# LeetCode Link, https://leetcode.com/problems/two-sum/
# Topics, Array, Hash Table


class Solution(object):
    def twoSum(self, nums, target):
        for i in range(nums.__len__()):
            for j in range(nums.__len__()):
                if(i<j):
                    if((nums[i] +nums[j]) == target ):
                        return [i,j]
