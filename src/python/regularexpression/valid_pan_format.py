import re
n = int(input(""))
pattern = "^[A-Z]{5}[0-9]{4}[A-Z]$"
for x in range(n):
    a = input("")
    result = re.match(pattern,a)
    if result:
        print("YES")
    else:
        print("NO")    