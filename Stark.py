def stark(x, y, z):
    count = 0
    if y > x:
        if z <= y:
            return x - (z-1)
        else:
            return 0
    else:
        if z <= y:
            while x > 0:
                x -= y
                count += y - (z-1)
            if x > 0:
                y = x
                count += y - (z-1)
    return count
