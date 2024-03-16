def test_function(num):
    if num % 2 != 0:
        print(num)
    else:
        raise RecursionError("This is a even number")
if __name__ == "__main__":
    try:
        test_function(11)
        test_function(32)
        test_function(14)
        test_function(123)
    except Exception as e :
        print(e)
