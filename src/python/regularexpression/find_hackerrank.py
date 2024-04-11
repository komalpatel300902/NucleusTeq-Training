# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern1 = "^hackerrank"
pattern2 = "hackerrank$"
pattern6 = ".*hackerrank"
n = int(input(""))
for x in range(n):
    a = input("")
    if re.search(pattern1,a) and re.search(pattern2,a):
        print(0)
        continue
    elif re.search(pattern1,a):
        print(1)
    elif re.search(pattern2,a):
        print(2)
    elif re.search(pattern6,a):
        print(-1)