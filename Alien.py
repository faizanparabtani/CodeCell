def aliens(a, b):
    count = 0
    print(a, b)
    if a < b:
        count += a
        b = b - a + 1
        a = 1
        print(a, b)
        while a*2 != b:
            a = a*2
            count += 1
        a = a*2
        count += 1
        if a == b:
            count += a
            return count - 1
    elif a > b:
        count += b
        a -= b + 1
        b = 1
        while b*2 != a:
            b = b*2
            count += 1
        b = b*2
        count += 1
        if a == b:
            count += b
            return count - 1