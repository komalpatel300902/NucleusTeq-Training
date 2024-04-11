class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        length = len(s)
        output = ""
        diff = 2*(numRows-1)
        condition = True
        # step1: Number of rows are fixed so create for loop for it
        for x in range(numRows):
            #step2: create for loop to get the first line
            a = 0
            b = 2*(numRows-1)
            i = x
            a += i*2
            b -= i*2
            if i < length and x != 0 and x != numRows -1:
                output += s[i]
            for y in range(length):
                if x == 0 or x == numRows-1:
                    if  i > length -1:
                        break
                    output += s[i]
                    i += diff
                else:
                    if i+b > length-1:
                        break
                    else:
                        output += s[i+b]

                    if i+b+a > length-1:
                        break
                    else:
                        output += s[i+b+a]
                    i += diff
        return output