lst = ["komal","patel","is","amazing","person"]
def capitalise_word(a):
    return a.capitalize()

new_lst = list(map(capitalise_word,lst))
print(new_lst)

def filter_word(val):
    if len(val) > 3:
        return val

filtered_lst = list(filter(filter_word,new_lst))
print(filtered_lst)

from functools import reduce
filtered_lst = ["asd"]
def reduce_list(first, second):
    print(first, second)
    return first+second

val = reduce(reduce_list, filtered_lst)
print(val)