from multipledispatch import dispatch

@dispatch(int,int)
def add(num1,num2):
    return num1+num2

@dispatch(int,int,int)
def add(num1,num2,num3):
    return num1+num2+num3

print(add(12,23))
print(add(12,23,34))