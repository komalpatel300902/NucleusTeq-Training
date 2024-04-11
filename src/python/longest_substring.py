class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        output = ""
        length = len(s)
        for x in range(length):
            a = ""
            b = ""
            for y in range(x,length):
                a = a + s[y]
                b = s[y] + b
                if a == b and len(output) < len(a):
                    output = a
        return output
        