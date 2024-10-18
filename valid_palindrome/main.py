import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)

        i, j = 0, len(s) - 1
        
        if len(s) == 0:
            return True
        elif len(s) == 1:
            return True

        while i < j:
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
            
        return True
                