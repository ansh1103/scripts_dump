def checkBalancedParenthesis(string):
    """
     Check if parentheses are balanced in a string using Stack
    :param string:
    :return:
    """
    open_bracket_list = ['(', '{', '[']
    closed_bracket_list = [')', '}', ']']
    stack = []

    for char in string:
        if char in open_bracket_list:
            stack.append(char)
        elif char in closed_bracket_list:
            pos_of_char = closed_bracket_list.index(char)
            if len(stack) > 0 and open_bracket_list[pos_of_char] == stack[len(stack) - 1]:
                stack.pop()
            else:
                return 'unbalanced'

    if len(stack) == 0:
        return 'balanced'
    else:
        return 'unbalanced'


if __name__ == "__main__":
    print(checkBalancedParenthesis('[(c+d*2]'))
