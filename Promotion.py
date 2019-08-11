def DundeMifflin(n):
    lis = []
    ans1 = 0
    for i in n:
        if i == 0:
            continue
        else:
            for j in n:
                if j == 0:
                    continue
                elif i == 1 and j == 1:
                    ans1 += 1
                    lis.append(ans1)
                else:
                    if n.index(j) > n.index(i):
                        print(i, j)
                        ans = i & j
                        lis.append(ans)
                    else:
                        continue
    return sum(lis)


n = int(input('Enter T: '))
send = list(map(int, input().rstrip().split()))
ansu = DundeMifflin(send)
print(ansu)
