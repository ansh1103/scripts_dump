def sum(n):
    if n <=1:
        return n
    else:
        answer = sum(n-1)
    return n + answer

def GCD(a,b):
    if b == 0:
        return a
    return GCD(b, a%b)

def fact(n):
    if n == 0:
        return 1  # Base case
    return (n * fact(n - 1))  # Not a tail-recursive call

def fibonacci(n):
    if n == 0:
        return 0
    elif n ==1 or n == 2:
        return 1
    return (fibonacci(n-1)+fibonacci(n-2))

res = 0
start = 1
def integerReversal(n):
    global res
    global start

    if n>0:
        integerReversal(int(n/10))
        res += (n % 10) * start
        start *= 10
    return res

if __name__ == '__main__':
    # print(sum(6))
    print(GCD(49, 35))
    print(fact(5))
    print(fibonacci(8))
    print(integerReversal(789))