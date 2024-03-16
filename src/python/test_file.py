from typing import List

def kp(): ...

print(... == "Ellipsis")

def add(num1: int, num2: List[int]) -> int:
    num = num1
    if len(num2) > 0:
        for x in range(len(num2)):
            num += num2[x]
    return num
print(add(56,[78,34,23]))
lst = [12,34,56,76,78,78]
lst.__iter__()