def beautifulDays(m, n, p):
    Reverse = 0
    count = 0
    temp = 0
    for a in range(m, n+1):
        temp = a
        while(a > 0):
            Remainder = a % 10
            Reverse = (Reverse * 10) + Remainder
            a = a // 10
        if (temp - Reverse) % p == 0:
            count += 1
            Reverse = 0
        else:
            Reverse = 0
    return count
