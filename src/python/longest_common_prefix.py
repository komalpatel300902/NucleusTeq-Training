class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        condition = True
        index = 0
        ch = set({})
        while condition:                 
            for x in strs:
                if len(x) > index:
                    ch.add(x[index]) 
                else: 
                    return output
            if len(ch) == 1:
                ch = set({})
                output += x[index]
                index += 1
            else :
                return output
        return output