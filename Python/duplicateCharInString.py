from collections import Counter
def findDuplicats(s):
    """ find duplicate characters in a given string"""
    count = {}
    list1 = []
    list_of_string = list(s)
    print(list_of_string)

    count = Counter(list_of_string)
    print(count)
    
    for element in count:
        if count[element] > 1:
        
            list1.append(element)
    
    print(list1)

if __name__ == '__main__':
    string1 = 'anshuman'
    findDuplicats(string1)
        

