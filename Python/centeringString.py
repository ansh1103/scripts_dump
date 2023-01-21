"""
Write a function that takes a string as its first parameter,and the width of the terminal in characters(80)
 as its second parameter. The function should return a new string that consists of the original string
 padded by enough spaces on its left so that the original string will appear centered within the provided width when it
 is printed. Call your function via a main function.
"""
def center(string, width):
    if width < len(string):
        return string
