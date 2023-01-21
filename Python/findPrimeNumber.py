def isPrime(arr):
    primelist = []
    for element in arr:
        if element > 2:
            for i in range(2, element):
                if element % i == 0:
                    break
                else:
                    primelist.append(element)
                    break
    return primelist


print(isPrime([11, 14, 13, 17, 19, 23, 26]))
