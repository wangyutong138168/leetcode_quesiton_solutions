class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            need = target - num

            if need in seen:
                return [seen[need], i]

            seen[num] = i


sol = Solution()
print(sol.twoSum([2,4,6,8,10,12,13,-1], 10))
