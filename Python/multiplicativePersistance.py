def multiplicativePersistance(number):
    """
    Have the function MultiplicativePersistence(num) take the num parameter being passed which will always be
    a positive integer and return its multiplicative persistence which is the number of times you must multiply
    the digits in num until you reach a single digit. For example: if num is 39 then your program should return
    3 because 3 * 9 = 27 then 2 * 7 = 14 and finally 1 * 4 = 4 and you stop at 4.
    :param number:
    :return:
    """
    string_number = str(number)

    if len(string_number) == 1:
        return 0
    digits = [int(num) for num in string_number]
    result = 1
    for digit in digits:
        result = result * digit
    return 1+multiplicativePersistance(result)


if __name__ == '__main__':
    print(multiplicativePersistance(1))
