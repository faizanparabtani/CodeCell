def DundeMifflin(n):
    lis = []
    for i in n:
        if i == 0:
            continue
        else:
            for j in n:
                if j == 0:
                    continue
                else:
                    if n.index(j) > n.index(i):
                        print(i, j)
                        ans = i & j
                        lis.append(ans)
                    else:
                        continue
    return sum(lis)