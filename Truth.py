def truth(a):
    maxo = max(a)
    lis = []
    for i in range(len(a)):
        if a[i] != 0:
            lis.append(a[i])
        else:
            continue
    if len(lis) < maxo:
        return 0
    else:
        return 1
