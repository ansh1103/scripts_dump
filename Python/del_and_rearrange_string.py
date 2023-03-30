from collections import Counter


def make_string(str1, str2):
    """
    Given two strings, find if we can make first string from second by deleting some characters from second and
     rearranging remaining characters.

    Examples:

    Input : s1 = ABHISHEKsinGH
        : s2 = gfhfBHkooIHnfndSHEKsiAnG
    Output : Possible

    Input : s1 = Hello
      : s2 = dnaKfhelddf
    Output : Not Possible
    :return: 
    """
    "using Counter"
    dict1 = Counter(str1)
    dict2 = Counter(str2)
    print(dict1)
    print(dict2)

    result = dict1 & dict2
    print(result)
    return result == dict1


if __name__ == "__main__":
    string1 = "Hello"
    string2 = "dnaKfHelddfol"
    if make_string(string1, string2):
        print("possible")
    else:
        print("Not possible")




