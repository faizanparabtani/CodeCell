def hannah(s):
    sumo = 0
    lis = []
    for i in s:
        if i.isdigit():
            lis.append(i)
        else:
            continue
    for l in lis:
        l = int(l)
    for j in lis:
        c = lis.count(j)
        if c > 1:
            sumo += c
            for k in range(c):
                lis.remove(j)
        else:
            sumo += 1
    sumo += 1
    if sumo == 13:
        return 'Hannah survived'
    else:
        return 'Hannah did not survive'
