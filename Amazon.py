def amazon(a):
    a.sort()
    element = a[0]
    count = a.count(a[0])
    for i in range(1, len(a) - 1):
        count1 = a.count(a[i])
        if count < count1:
            count = count1
            element = a[i]
        elif count1 == count:
            if a[i] < a[i+1]:
                continue
    return element