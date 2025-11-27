class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):

            for value in seen:
                if value + num == target:
                    return [seen[value], i]
            
            seen[num] = i