# In this Designer Door Mat problem we need to develop a python program that can read two integers separated by space.
# and then we need to print a design pattern that contains a WELCOME message in between it.

def doormat():
    n, m = map(int,input().split())
    for i in range(n//2):
        j = int((2*i)+1)
        print(('.|.'*j).center(m, '-'))
    print('WELCOME'.center(m,'-'))
    for i in reversed(range(n//2)):
        j = int((2*i)+1)
        print(('.|.'*j).center(m, '-'))


if __name__ == '__main__':
    print(doormat())
