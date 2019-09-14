def deck(a, k):
    lis = []
    finallis = []
    for i in range(1, a+1):
        for j in range(1, a+1):
            if abs(j - i) == k:
                lis.append(j)
    for i in lis:
        if i not in finallis:
            finallis.append(i)
    if len(finallis) == a:
        return finallis
    else:
        return -1
