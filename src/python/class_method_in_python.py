class School:
    
    @classmethod
    def print_name(cls):
        return cls

if __name__ == "__main__":
    s = School()
    School.print_name()
    print(s.__class__)

# we will run this block of code from test_runner.py
s = School()
c = School.print_name()
print(c)
print(s.__class__ == c)

# hence the cls method cls holds filename.clssname