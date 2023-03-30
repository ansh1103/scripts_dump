
import re
"""
# Find the number of repeated words in a file/string
# Print words that are repeated odd number of times and have even number of characters
# input = "Hello my name is Praveen\nAre you done\nMy work is not done\nWhen I am done I will let you know\nIs that so\n"
# is = 3
# done = 3
"""

def func(input_s):
    word_dict = {}
    res = []

    word_list = re.split(' |\n', input_s.lower())
    # word_list = input_s.split(' |\n')

    print(word_list)
    for i in range(len(word_list)):
        if word_list[i] in word_dict.keys():
            word_dict[word_list[i]] += 1
        else:
            word_dict[word_list[i]] = 1
    print(word_dict)

    for key, value in word_dict.items():
        if value > 1 and value % 2 != 0 and len(key) % 2 == 0:
            res.append(key)

    return res

print(func("Hello my name is Praveen\nAre you done\nMy work is not done\nWhen I am done I will let you know\nIs that so\n"))