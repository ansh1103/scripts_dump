def numberEncoding(string1):
    """
    Have the function NumberEncoding(str) take the str parameter and encode the message according to the following
    rule: encode every letter into its corresponding numbered position in the alphabet. Symbols and spaces will also be
     used in the input. For example: if str is "af5c a#!" then your program should return 1653 1#!.
    :param string:
    :return:
    """
    import string
    alphabet_list = [char for char in string.ascii_lowercase]
    print(alphabet_list)
    resultant_string = ""
    for s in string1.lower():
        if s.isalpha():
            resultant_string += str(alphabet_list.index(s) + 1)
        else:
            resultant_string += str(s)
    return resultant_string


print(numberEncoding("af5c a#!"))
