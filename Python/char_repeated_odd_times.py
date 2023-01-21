"""
# Char sequences
# input: "aabbabccdddeee"
# print the chars that have repeated odd numbers of times in a continuous sequence
# valid output: b e
# invalid output: a b e
"""

def func(string):
    strng_c = {}
    l = []
    for i in range(len(string)-2):
        if string[i] == string[i+1] and string[i+1] == string[i+2]:
            if string[i] in strng_c.keys():
                strng_c[string[i]] += 1
            else:
                strng_c[string[i]] = 1

    for key, val in strng_c.items():
        if val % 2 != 0:
            l.append(key)
    print(', '.join(l))


func("aabbabbbbbccccccdcddeee")
