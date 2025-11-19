class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        
        for i, num in enumerate(nums):
            need = target - num

            if need in seen:
                return [seen[need], i]

            seen[num] = i

s = Solution()
print(s.twoSum([2,7,11,15], 9))
