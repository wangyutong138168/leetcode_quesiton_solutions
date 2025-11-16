class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = {}
        operations = 0

        for x in nums:
            target = k - x
            
            if target in count and count[target] > 0:
                operations += 1
                count[target] -= 1
            else:
                count[x] = count.get(x,0) + 1

        return operations