class A:
    def __int__(self):
        pass
    def display(self):
        print("i am in class A")

class B:
    def __int__(self):
        pass
    def display(self):
        print("i am in class B")

class C(B,A):
    def __int__(self):
        pass
    def display(self):
        B.display(self)
        A.display(self)
        return super().display()
    
if __name__ == "__main__":
    c = C()
    C.display(c)