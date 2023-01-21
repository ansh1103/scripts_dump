def func(n):
    sum = 0

    for i in range(1, n+1):
        sum += n
        n = 10*n + n
    print(sum)


func(3)
