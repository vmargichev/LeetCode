class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for i in range(0, len(s)-1):
            val1 = ord(s[i])
            val2 = ord(s[i+1])
            if val1>val2:
                sum += val1 - val2
            else:
                sum += val2 - val1
        return sum