class A:
    my_name = ""
    def __init__(self):
        print(self)
    def add(self,num1,num2):
        return num1+num2
    
obj = A()
print("below object obj ")

print(obj)
add = obj.add(12,23)
print(add)

obj2 = A()
A.my_name = "komal"
print(obj2.my_name)
print(obj.my_name)
def multiply(num1,num2):
    return num1*num2

print(multiply(5,23))

