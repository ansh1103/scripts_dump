def reverseit(s):
    # print(s[::-1])

    newstr = []
    for i in range(len(s)):
        newstr.append((s[len(s)-i-1]))
    print(''.join(newstr))
if __name__ == '__main__':
    s = 'abcd'
    reverseit(s)