import time
def memoize_factorial(f):
    memory = {}
    def inner(num):
        if num not in memory:
            print("Adding number to memomy")
            memory[num] = f(num)
        return memory[num]
    return inner

@memoize_factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

starttime  = time.time()
print(factorial(5))
print(time.time() - starttime)

print(factorial(6))

