def replacer(origstring, ch, ch_to_replace, char_occur):
    occurance = 0
    new_str = ""
    
    origstr = list(origstring.lower())
    # for element in ch:
    for element in ch:
        find_pos_list = []
        for i in range(len(origstr)):
            if element == origstr[i]:
                find_pos_list.append(i)
        print(find_pos_list)
        char_to_replace_index = origstring.find(element, find_pos_list[1])
        origstr[char_to_replace_index] = replacing_ch
    print(''.join(origstr))

            

if __name__ == '__main__':
    original_str= 'InterviewBit'
    ch = ['e', 't']
    occurrence = 2
    replacing_ch = '@'
    print(original_str.find(''.join(ch)))
    replacer(original_str, ch, replacing_ch, occurrence)