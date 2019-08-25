def cube(a):
        c = a*a*a
        print(c)
        if (c % 2  == 0 and c % 4 != 0) or (c % 5 == 0 and c % 10 != 0) or (c % 8 == 0 and c % 4 != 0):
            return 8
        elif c % 10 == 0 or c % 4 == 0 or c % 7 == 0:
            return 1
        elif c % 3 == 0 or c % 6 == 0 or c % 9 == 0:
            return 9
        else:
            return 'invalid input'