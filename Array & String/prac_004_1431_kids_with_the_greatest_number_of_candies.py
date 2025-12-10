class Solution(object):
    def kidsWithCandies(self, candy, extraCandies):
        minCandies = min(candies)
        result = []

        for candy in candies:
            result.append(candy == minCandies)
        return result