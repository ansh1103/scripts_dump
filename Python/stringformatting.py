"""
Given an integer,n , print the following values for each integer 1 from n to :

Decimal
Octal
Hexadecimal (capitalized)
Binary
"""


def stringFormat(n):
    for i in range(1, n+1):
        print(f"{i:d}\t{i:o}\t{i:X}\t{i:b}")


stringFormat(17)
