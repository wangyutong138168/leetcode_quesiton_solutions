class Solution:
    def mergeCommon(self, word1: str, word2: str) -> str:
        res = ""
        for a, b in zip(word1, word2):
            if a == b:
                res += a
        return res
