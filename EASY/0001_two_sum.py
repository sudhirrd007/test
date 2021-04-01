# 6948 ms
# Array, Hash Table


class Solution(object):
    def twoSum(self, nums, target):
        for i in range(nums.__len__()):
            for j in range(nums.__len__()):
                if(i<j):
                    if((nums[i] +nums[j]) == target ):
                        return [i,j]
