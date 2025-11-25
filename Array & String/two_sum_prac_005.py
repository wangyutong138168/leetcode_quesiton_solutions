class Solution(object):
    def twoSum(s, num, target):
        seen = {}

        for i, nums in enumerate(num):
            need = target - num

            if need in seen:
                return[seen[need], i]

