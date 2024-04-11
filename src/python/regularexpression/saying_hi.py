# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern = "^[hH][Ii]\s[^Dd].*"
n = int(input(""))
for x in range(n):
    a = input("")
    result = re.search(pattern,a)
    if result:
        print(result[0])