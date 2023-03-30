# Program is find whether the target string would be available in the list of rotated string
# Exmaple: Is original string is "computer", find whether targetsubsrt = 'putercom' is available

import collections
def findRotation(orgStr, subStr):
    # d = collections.deque()

    if len(orgStr) != len(subStr):
        print("Both strings doesn't match is length")
        exit()

    substr_list = []
    # for i in range(len(orgStr)+1):
    #    substr_list.append(orgStr[i:]+orgStr[:i])
    substr_list = [orgStr[i:]+orgStr[:i] for i in range(len(orgStr)+1)]
    print(substr_list)
    if subStr in substr_list:
        print("Substring is available")
    else:
        print("Substring is not available")
    
if __name__ == '__main__':
    findRotation("computer", "utercomp")