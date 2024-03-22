if __name__ == "__main__":

    try:
        a = 1.9/0
    except ZeroDivisionError as e1:
        print(e1)

    try:
        a = 10**10000
        print(a)
    except OverflowError as ovf:
        print(ovf)
       