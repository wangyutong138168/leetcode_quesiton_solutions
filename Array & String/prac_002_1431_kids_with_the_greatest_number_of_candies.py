class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxCandies = max(candies)
        reuslt = []
        for candy in candies: