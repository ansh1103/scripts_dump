"""
Louise joined a social networking site to stay in touch with her friends. The signup page required her to input a name
and a password. However, the password must be strong. The website considers a password to be strong if it satisfies the
following criteria:

Its length is at least .
It contains at least one digit.
It contains at least one lowercase English character.
It contains at least one uppercase English character.
It contains at least one special character. The special characters are: !@#$%^&*()-+
She typed a random string of length  in the password field but wasn't sure if it was strong. Given the string
she typed, can you find the minimum number of characters she must add to make her password strong?


"""
import math
import os
import random
import re
import sys


# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    count = 0
    regex_list = ['\d', '[A-Ba-b]', '[!@#$%^&*()-+]']
    for regex in regex_list:
        if not re.search(regex, password):
            count += 1
    return max(6 - n, count)


if __name__ == '__main__':
    

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    print(answer)
