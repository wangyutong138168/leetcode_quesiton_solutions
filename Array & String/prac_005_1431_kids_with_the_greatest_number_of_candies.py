class Solution(object):
    def updateCandies(self,candies,index, newValue):
        candies[index] = newValue
        return candies

    def kidsWithCandies(self, candies, extraCandies):
        maxCandies = max(candies)
        return [c + extraCandies >= maxCandies for c in candies]

s = Solution()

candies = [2,3,5,1]
extra = 3

candies = s.updateCandies(candies, 0,10)

result = s.kidsWithCandies(candies, extra)

print(result)