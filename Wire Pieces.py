def wirepieces(n, x, y, z):
    lis = []
    lis.append(x)
    lis.append(y)
    lis.append(z)
    lis.sort()
    print(lis)
    for i in lis:
        if n % i == 0:
            ans = n / i
            return int(ans)
    else:
        return -1