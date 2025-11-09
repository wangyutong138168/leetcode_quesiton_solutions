class Solution:
    def compress(self, chars: List[str]) -> int:
        i = j = 0
        while j < len(chars):
            ch = chars[j]
            count = 0
            while j < len(chars) and chars[j] == ch:
                j += 1
                count += 1
            chars[i] = ch
            i += 1
            if count > 1:
                for c in str(count):
                    chars[i] = c
                    i += 1
        return i
