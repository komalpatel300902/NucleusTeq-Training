# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(map(int,input("").split(" ")))
n = int(input(""))
num = 0
for x in range(n):
    set1 = set(map(int,input("").split(" ")))
    intersection = set1.intersection(a)
    if len(intersection) != len(set1):
        print(False)
        break
    num += 1
if num == n:
    print(True)