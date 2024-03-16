class MyClass():
    class_variable = "MyClass"
    def __init__(self):
        print("constructor just got executed")
    def class_function(self):
        print("This is a class function")

if __name__ == "__main__":
    a = MyClass()
    print(a.class_variable)
    a.class_function()