# In this Designer Door Mat problem we need to develop a python program that can read two integers separated by space.
# and then we need to print a design pattern that contains a WELCOME message in between it.

def doormat(a, b):
    pattern = '.|.'
    for i in range(1, a, 2):
        print((i*pattern).center(b, '-'))
    print("WELCOME".center(b, '-'))
    for i in range(a-2, -1, -2):
        print((i*pattern).center(b, '-'))


if __name__ == '__main__':
    n, m = map(int, input('Enter values n & m :').split(' '))
    print(doormat(n, m))
