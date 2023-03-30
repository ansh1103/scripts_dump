from itertools import combinations


def generateSubstrings(s):
    print(f"Original string is {str(s)}")

    result = []
    # for x, y in combinations(range(len(s)+1), r=2):
    #     result.append(s[x: y])
    # return result

    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            result.append(s[i:j])

    return result


def minimum_substring(string, pattern):
    """
    Given two strings str and pattern, find the smallest substring in str containing all characters of pattern efficiently.
    :param string:
    :param pattern:
    :return:
    """
    char_index_in_string = []
    for i in range(len(pattern)):
        if pattern[i] in string:
            char_index_in_string.append(string.index(pattern[i]))
    print(char_index_in_string)
    print(sorted(char_index_in_string))
    substring = ''
    for i in range(char_index_in_string[0], char_index_in_string[-1]):
        substring += string[i]
    return substring


def get_substring_freq(s):
    """
    Given a String, extract all unique substrings with their frequency.
    :param s:
    :return:
    """
    print(f"Original string is {str(s)}")

    temp_list = []
    result = {}
    # for x, y in combinations(range(len(s)+1), r=2):
    #     result.append(s[x: y])
    # return result

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            temp_list.append(s[i:j])

    for element in temp_list:
        if element not in result.keys():
            result[element] = 1
        else:
            result[element] += 1

    return result

print(generateSubstrings('Geekforgeeks'))

print(minimum_substring('Geekforgeeks', 'rge'))

print(get_substring_freq('Geekforgeeks'))
