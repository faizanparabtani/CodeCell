def truth(a):
    maxo = max(a)
    count = 0
    no = len(a) - maxo
    for i in a:
        if i < no:
            count += 1
    if count < no:
        return 1
    else:
        return 0
