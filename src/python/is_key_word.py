x = {12:12}
y = {12:12}
z = 10*1
print(id(x))
print(id(y))
print(x is y)
print(x == y)
"""Conclusion 

is : it matches the address of the variables

== : it matches the value of the variables

Take away : mutable variable with same value will have different address.
Immutable variable with same value will have same address."""