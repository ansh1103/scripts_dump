def add_nums(n, m):
    while m != 0:
        data = n & m
        n = n ^ m
        m = data << 1
    return n

print(add_nums(8,3))