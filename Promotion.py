def DundeMifflin(n):
    def DundeMifflin(n):
    lis = []
    for i in range(len(n)):
        for j in range(len(n)):
            if j > i:
                ans = n[i] & n[j]
                lis.append(ans)
    return sum(lis) % 101


n = int(input('Enter T: '))
send = list(map(int, input().rstrip().split()))
ansu = DundeMifflin(send)
print(ansu)
