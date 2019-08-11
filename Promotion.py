def DundeMifflin(n):
    lis = []
    for i in n:
        for j in n:
            if n.index(j) > n.index(i):
                ans = i & j
                lis.append(ans)
    return sum(lis)%101


n = int(input('Enter T: '))
# for i in range(n):
send = list(map(int, input().rstrip().split()))
ansu = DundeMifflin(send)
print(ansu)