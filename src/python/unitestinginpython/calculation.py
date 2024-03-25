from typing import List
def add(lst: List) -> int:
    sum =0
    for x in lst:
        sum += x
    return sum

def average(lst: List) -> float:
    result = add(lst)/len(lst)
    return result

def first_n_natural_number(n: int) -> int:
    a = range(1,n+1)
    return add(a)

