def cube(a):
    c = a*a*a
    if c % 3 == 0:
        return 9
    elif c % 4 == 0 or c % 10 == 0 or c % 7 == 0:
        return 1
    else:
        return 9
