from pip._vendor.distlib.compat import raw_input


def largestPair(number):
    string = str(number)
    largest = 0
    for i in range(1, len(string)-1):
        number = string[i:i+2]
        if int(number) > int(largest):
            largest = number
    return largest


if __name__ == '__main__':
    print(largestPair(43288))
