def nonrepeating_character(input_string):
    """
    Function NonrepeatingCharacter(str) take the str parameter being passed, which will contain only
    alphabetic characters and spaces, and return the first non-repeating character. For example: if str is
    "agettkgaeee" then your program should return k. The string will always contain at least one character and
    there will always be at least one non-repeating character.
    :param input_string:
    :return:
    """
    char_list = []
    counter_dict = {}
    for char in input_string:
        if char not in counter_dict.keys():
            counter_dict[char] = 1
            char_list.append(char)
        else:
            counter_dict[char] += 1
    for ch in char_list:
        if counter_dict[ch] == 1:
            return ch


if __name__ == "__main__":
    string = nonrepeating_character("abcdef")
    print(f"First non repeating_character is of 'abcdef' is {nonrepeating_character('abcdef')}")
    print(f"First non repeating_character is of 'hello world hi hey' is {nonrepeating_character('hello world hi hey')}")
    print(f"First non repeating_character is of 'agettkgaeee' is {nonrepeating_character('agettkgaeee')}")

