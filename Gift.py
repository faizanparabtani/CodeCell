def gifts(a):
    count = 1
    sumo = 0
    for i in range(len(a) - 1):
        term = a[i]
        if term > a[i + 1]:
            count += 1
            sumo += count
        else:
            sumo += 1
    if a[i] < a[len(a) - 1]:
        sumo += count
    else:
        sumo += 1
    return sumo
