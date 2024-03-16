class A:
    # creating protected variable
    _a = "komal"
    #creating a private variable
    __b = "name"
    def __init__(self):
        pass
    def get_b(self):
        return self.__b
    def set_b(self,name):
        self.__b = name

if __name__ == "__main__":
    try :
        a = A()
        print(a._a)
        a.set_b(23)
        print(a.get_b())

    except Exception as e:
        print(e)