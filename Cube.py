def cubes(a):
    sum = 0
    for i in range(1, a+1):
        c = i*i*i
        if c > 9:
            if c % 3 == 0:
                sum += 9
            elif (c-1) % 3 == 0:
                sum += 8
            else:
                sum += 1
        else:
            sum += c
    return sum % 1000007
